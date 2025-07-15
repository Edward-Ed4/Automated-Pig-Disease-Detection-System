import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2 # A good lightweight pre-trained model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
import os
import matplotlib.pyplot as plt
import numpy as np

# --- Configuration ---
# IMPORTANT: This path points to your 'sick pig database' folder.
DATASET_ROOT_PATH = 'C:/Users/Alfred/Desktop/sick pig database' # CONFIRMED PATH

# The specific subfolder within DATASET_ROOT_PATH that contains your class folders.
# This is 'category' because 'Healthy' is inside it.
DATA_SUBFOLDER = 'category' # This is where all your actual class folders are

IMAGE_SIZE = (224, 224) # Standard input size for MobileNetV2
BATCH_SIZE = 32         # Number of images processed per step during training
# --- CHANGE MADE HERE ---
EPOCHS = 500            # Increased number of times the model sees the entire training dataset
# --- END CHANGE ---
LEARNING_RATE = 0.0001 # Small learning rate for fine-tuning pre-trained models

# --- 1. Data Loading and Augmentation ---
print("--- Loading and Preprocessing Data ---")

# ImageDataGenerator for data augmentation and scaling
# We'll use validation_split to create train/validation sets from a single folder.
train_val_datagen = ImageDataGenerator(
    rescale=1./255,          # Normalize pixel values to 0-1
    rotation_range=20,       # Randomly rotate images by up to 20 degrees
    width_shift_range=0.2,   # Randomly shift images horizontally
    height_shift_range=0.2,  # Randomly shift images vertically
    shear_range=0.2,         # Apply shear transformation
    zoom_range=0.2,          # Randomly zoom into images
    horizontal_flip=True,    # Randomly flip images horizontally
    fill_mode='nearest',     # Strategy for filling in new pixels created by transformations
    validation_split=0.2     # Use 20% of the data for validation
)

# Create training generator
# CORRECTED PATH: Point to the 'category' folder, which contains all your classes
train_generator = train_val_datagen.flow_from_directory(
    os.path.join(DATASET_ROOT_PATH, DATA_SUBFOLDER), # Point to the 'category' folder
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical', # Use 'categorical' for one-hot encoded labels
    subset='training',        # Specify this is the training subset
    shuffle=True
)

# Create validation generator
# CORRECTED PATH: Point to the 'category' folder
validation_generator = train_val_datagen.flow_from_directory(
    os.path.join(DATASET_ROOT_PATH, DATA_SUBFOLDER), # Point to the same 'category' folder
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='validation',      # Specify this is the validation subset
    shuffle=False
)

NUM_CLASSES = len(train_generator.class_indices) # Automatically get number of classes from folder names
print(f"Detected {NUM_CLASSES} classes: {list(train_generator.class_indices.keys())}")
print(f"Found {train_generator.samples} training images belonging to {NUM_CLASSES} classes.")
print(f"Found {validation_generator.samples} validation images belonging to {NUM_CLASSES} classes.")


# --- 2. Model Selection (Transfer Learning with MobileNetV2) ---
print("\n--- Building Model with Transfer Learning ---")

# Load MobileNetV2 pre-trained on ImageNet, excluding the top (classification) layer
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(IMAGE_SIZE[0], IMAGE_SIZE[1], 3))

# Freeze the base model layers so they are not updated during initial training
# This preserves the powerful features learned from ImageNet
base_model.trainable = False

# Add custom classification layers on top of the base model
x = base_model.output
x = GlobalAveragePooling2D()(x) # GlobalAveragePooling2D converts the feature maps into a single vector per image
x = Dense(128, activation='relu')(x) # A dense (fully connected) layer
predictions = Dense(NUM_CLASSES, activation='softmax')(x) # Output layer with softmax for multi-class classification

model = Model(inputs=base_model.input, outputs=predictions)

# --- 3. Compile the Model ---
print("\n--- Compiling Model ---")
model.compile(optimizer=Adam(learning_rate=LEARNING_RATE),
              loss='categorical_crossentropy', # Use this for multi-class classification
              metrics=['accuracy'])

model.summary() # Print a summary of the model architecture

# --- 4. Train the Model ---
print("\n--- Starting Model Training ---")
history = model.fit(
    train_generator,
    epochs=EPOCHS, # Now set to 20
    validation_data=validation_generator,
    steps_per_epoch=train_generator.samples // BATCH_SIZE, # Number of batches per epoch
    validation_steps=validation_generator.samples // BATCH_SIZE # Number of validation batches per epoch
)

print("\n--- Training Finished ---")

# --- 5. Save the Trained Model ---
print("\n--- Saving Model ---")
model_save_path = 'pig_disease_detector_model.h5'
model.save(model_save_path)
print(f"Model saved to: {model_save_path}")

# --- 6. Plot Training History ---
print("\n--- Plotting Training History ---")
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

plt.tight_layout()
plt.show()
print("Training history plots displayed.")

