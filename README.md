
# 🐖 Automated Pig Disease Detection System (Machine Learning-Powered)

A cutting-edge livestock health monitoring system for pig farms, leveraging ESP32-CAM for visual data acquisition, a Python Flask server for deep learning-based Machine Learning inference, and a Flutter mobile application for real-time monitoring and alerts.

---

## 🚀 Project Summary

This project addresses the critical need for early and efficient disease detection in pig farming. Moving beyond traditional manual inspections, our system automates the process by:
1.  **Capturing visual data** using a low-cost ESP32-CAM.
2.  **Transmitting images** to a powerful Python Flask server.
3.  **Employing a deep learning Machine Learning (ML) model** (MobileNetV2) on the server to analyze visual indicators of pig health, such as changes in skin color, presence of lesions, or altered behavior.
4.  **Triggering automated email alerts** to stakeholders upon high-confidence Machine Learning prediction.
5.  **Providing a real-time monitoring dashboard** via a Flutter mobile application.

This automated approach aims to significantly improve animal welfare, reduce operational costs, and enhance overall farm management efficiency, particularly vital for regions like Uganda.

---

## ✨ Key Features

* **Intelligent Image Acquisition:** ESP32-CAM captures high-quality images of pigs.
* **Toggleable Modes:** Seamlessly switch between **live MJPEG video streaming** to the Flutter app and **periodic image capture for Machine Learning inference** on the ESP32-CAM, optimizing resource usage.
* **Machine Learning-Powered Disease Classification:** Utilizes a fine-tuned MobileNetV2 deep learning model running on a Python Flask server for accurate identification of various pig health statuses.
* **Automated Email Alerts:** Sends instant email notifications to predefined recipients when a disease is detected with high confidence, preventing alert fatigue with a cooldown mechanism.
* **Real-Time Mobile Monitoring:** A cross-platform Flutter application provides a user-friendly dashboard to view the latest Machine Learning predictions, captured images, and system status in real-time.
* **Modular Architecture:** Separates hardware (ESP32-CAM), backend Machine Learning (Flask), and frontend (Flutter) for scalability and maintainability.

---

## 🧰 System Architecture

The system operates in a client-server model:
* **ESP32-CAM (Edge Device):** Captures images, hosts a small web server for control commands, and sends images to the Flask server.
* **Python Flask Server (Backend):** Receives images, runs the Machine Learning inference model, stores latest predictions, and sends email alerts.
* **Flutter Mobile App (Frontend):** Displays live stream, triggers image capture/prediction, and fetches/displays latest ML results.

<!-- Image Placeholder: System Architecture Diagram -->
<!-- To add your image, replace this comment with a Markdown image link like: -->
<!-- ![System Architecture](images/system_architecture.png) -->
<!-- Make sure 'images/system_architecture.png' is the correct path to your image file in your GitHub repo. -->

---

## 🛠 Installation & Deployment

This project requires setting up three main components:

### 1. ESP32-CAM Firmware

* **Prerequisites:**
    * Arduino IDE with ESP32 board support installed.
    * `AI Thinker ESP32-CAM` selected under `Tools > Board > ESP32 Arduino`.
    * `PSRAM: Enabled` selected under `Tools > PSRAM`.
    * A suitable `Partition Scheme` (e.g., `Huge APP` or `No OTA (Large APP)`).
    * A stable 5V power supply (at least 1A, preferably 2A) for the ESP32-CAM.
* **Files:** Ensure `app_httpd.cpp` and `camera_index.h` (from the original ESP32 CameraWebServer example) are in the same folder as your main `.ino` sketch.
* **Configuration:**
    * Open the `.ino` sketch.
    * Update your Wi-Fi `ssid` and `password`:
        ```cpp
        const char *ssid = "YourWiFiName";
        const char *password = "YourWiFiPassword";
        ```
    * Update the `SERVER_IP` to your PC's Flask server IP address:
        ```cpp
        const char* SERVER_IP = "YOUR_FLASK_SERVER_IP"; // e.g., "10.10.168.48"
        ```
* **Upload:** Flash the firmware to your ESP32-CAM via a USB-TTL adapter.

### 2. Python Flask Server (Machine Learning Backend)

* **Prerequisites:** Python 3.x, `pip` installed.
* **Setup:**
    1.  Clone the repository and navigate to the Flask server directory.
    2.  Install dependencies:
        ```bash
        pip install Flask tensorflow opencv-python-headless Pillow
        ```
    3.  Place your trained `pig_disease_detector_model.h5` file in the Flask server directory.
* **Run Server:**
    ```bash
    python inference_server.py
    ```
    Note the IP address printed (e.g., `http://10.10.168.48:5000`). This is your `YOUR_FLASK_SERVER_IP`.
* **Firewall:** Ensure your PC's firewall allows incoming connections on port `5000`.

<!-- Image Placeholder: Flask Server Running -->
<!-- ![Flask Server Running](images/flask_server_output.png) -->

### 3. Flutter Mobile Application (Frontend)

* **Prerequisites:** Flutter SDK installed, Android Studio/VS Code with Flutter/Dart extensions.
* **Setup:**
    1.  Clone the repository and navigate to the Flutter project directory (`pigcam2`).
    2.  Get dependencies:
        ```bash
        flutter pub get
        ```
* **Configuration:**
    * Open `lib/pages/camera_page.dart`.
    * Update the ESP32-CAM's IP address:
        ```dart
        final TextEditingController _esp32CamIpController = TextEditingController(
          text: 'YOUR_ESP32_CAM_IP_HERE', // e.g., '192.168.4.1' or '192.168.1.123'
        );
        ```
    * Update the Flask server's IP address in the `_sendImageBytesToPython` method:
        ```dart
        Uri.parse('http://YOUR_FLASK_SERVER_IP_HERE:5000/predict'), // e.g., '[http://10.10.168.48:5000/predict](http://10.10.168.48:5000/predict)'
        ```
* **Run App:**
    ```bash
    flutter run
    ```
    (Ensure your phone/emulator is connected to the same Wi-Fi network as your PC and ESP32-CAM).

<!-- Image Placeholder: Flutter App Home Screen (Healthy) -->
<!-- ![Flutter App Home Screen Healthy](images/flutter_app_healthy.png) -->
<!-- Image Placeholder: Flutter App Home Screen (Diseased) -->
<!-- ![Flutter App Home Screen Diseased](images/flutter_app_diseased.png) -->

---

## 🧠 Detection Methodology

The system's detection process involves:

1.  **Image Capture:** The ESP32-CAM captures a JPEG image.
2.  **Transmission:** The captured image (or stream) is sent over Wi-Fi.
3.  **Machine Learning Inference:** On the Flask server, the image is preprocessed (resized, normalized) and fed into the MobileNetV2 model.
4.  **Classification:** The trained model outputs a prediction (e.g., 'Healthy', 'skin changes', 'prolapses') and a confidence score.
5.  **Alerting & Display:**
    * If a disease is detected with high confidence, an email alert is sent.
    * The prediction and image are updated on the Flutter mobile app for real-time monitoring.

<!-- Image Placeholder: Example Email Alert -->
<!-- ![Example Email Alert](images/email_alert_screenshot.png) -->

---

## 📊 Dataset & Training

The Machine Learning model was fine-tuned using a custom dataset of pig images, including various visual symptoms.
* **Dataset Size:** Over 200+ labeled images (and growing).
* **Categories:** Includes images of pigs with skin rashes, redness, visible sores/lesions, unusual color tone changes, and a robust 'Healthy' class.
* **Model:** MobileNetV2, chosen for its efficiency and suitability for mobile/edge applications.

---

## 🐷 Field Deployment & Evaluation

* **Location:** Initial testing and data collection were conducted at a local pig farm in Uganda.
* **Environment:** Deployment involved real pigs in varying lighting and pen environments.
* **Monitoring:** The system was monitored to log detections and assess performance under practical conditions.

<!-- Image Placeholder: Physical Setup of ESP32-CAM on Farm (if available) -->
<!-- ![Physical Setup](images/physical_setup.png) -->

---

## 🚧 Known Limitations

* **Dataset Size & Diversity:** Current dataset, while custom, can be expanded for greater model generalization and accuracy across a wider range of disease symptoms and environmental conditions.
* **Environmental Robustness:** Accuracy can still be impacted by extreme lighting variations, dirt/debris on camera lenses, and dynamic animal movement.
* **Machine Learning Model Deployment:** The full Machine Learning model currently runs on a PC (Flask server). True on-device inference on the ESP32-CAM is not feasible due to resource constraints, requiring a more powerful edge device or highly optimized (and smaller) models for future iterations.
* **Single Camera View:** The system relies on a single camera view, which might miss symptoms not visible from that angle.

---

## 🔭 Future Work

* **Extensive Dataset Expansion:** Gather significantly larger and more diverse datasets for improved model generalization.
* **Advanced Model Exploration:** Integrate and optimize other state-of-the-art CNN architectures (e.g., EfficientNet, ResNet) for higher accuracy.
* **Edge Deployment:** Investigate deploying lightweight Machine Learning models (e.g., TensorFlow Lite) onto more powerful edge devices (ESP32-S3, Raspberry Pi with Coral ML accelerator) for on-device inference.
* **Multi-Camera & Behavioral Analysis:** Incorporate multiple camera views for comprehensive body coverage and integrate behavioral analysis from video streams as early disease indicators.
* **Robust Physical Integration:** Develop a durable, industrial-grade mechanical system for automated sorting, directly integrated with ML model output.
* **Cloud Integration:** Implement MQTT or cloud APIs for seamless integration with farm management software.

---

## 🧑‍💻 Contributors

* **Ssenyange Allan:** Project poster design, ESP32-CAM firmware (image capture, HTTP transmission), Flask server setup support.
* **Omara Emmanuel:** Flutter mobile application lead (UI/UX, data fetching from Flask, state management), Flask API integration support.
* **Kimera Dave David:** Overall system architecture design, Machine Learning model training dataset acquisition and preprocessing, Machine Learning model fine-tuning support.
* **Ebaju Edward:** Main technical report author, Python Flask server backend development (Machine Learning inference, API endpoints, alert logic, email integration).
* **Nabasirye Seanice:** Electronic components research and selection, hardware and physical materials procurement, overall documentation and testing support, GitHub repository management.

---

## 📜 License

This project is licensed under the MIT License – open for improvement and adaptation.

---

## 🔗 Useful Links

* [ESP32-CAM Documentation](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/camera.html)
* [Flutter Documentation](https://flutter.dev/docs)
* [Flask Documentation](https://flask.palletsprojects.com/en/latest/)
* [TensorFlow/Keras Documentation](https://www.tensorflow.org/api_docs/python/tf/keras)
* [Arduino IDE Setup for ESP32](https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html)
