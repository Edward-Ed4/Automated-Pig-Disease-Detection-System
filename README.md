
# 🐖 Real-Time Pig Disease Detection System (ESP32-CAM Based)

A smart livestock health monitoring system for pig farms that detects visual symptoms of disease using real-time image analysis powered by ESP32-CAM.

---

## 🧠 Project Summary

This system is designed to assist pig farmers in identifying early visual indicators of pig diseases—such as skin discoloration, lesions, or unusual physical changes—by using a low-cost ESP32-CAM module. By automating visual inspections, farmers can reduce manual labor, improve early intervention, and prevent the spread of illness across the herd.

This project is deployed and tested using **real-world datasets** and evaluated in a **live pig farm setting** in Uganda.

---

## 📸 Key Features

- 🔍 **Real-time image capture and classification** using ESP32-CAM.
- 🎯 **Color pattern analysis** to detect disease-like visual traits.
- 🌐 **Wi-Fi-enabled** for transmitting alerts or logging detection events.
- 🚫 No Arduino or external MCU — all processing is done on the ESP32-CAM.

---

## 🧰 System Components

| Component      | Description |
|----------------|-------------|
| **ESP32-CAM**  | Captures and processes images using onboard camera. |
| **5V Power Source** | Powers the ESP32-CAM (battery bank or regulated supply). |
| **Dataset**    | Custom dataset collected from live pigs on a Ugandan farm. |
| **Wi-Fi Access Point** | Optional: Used to send detection results or upload logs. |

---

## 🧠 Detection Methodology

- Captures frames using ESP32-CAM's integrated camera.
- Converts image to RGB565 and isolates region of interest (ROI).
- Analyzes dominant color or pixel features for disease symptoms (e.g. excessive redness, lesion spots).
- Sends result via serial or wireless transmission for action or logging.

---

## 🛠 Installation & Deployment

### Flash Firmware

1. Install [Arduino IDE](https://www.arduino.cc/en/software) with ESP32 board support.
2. Open the `pig_disease_detect.ino` sketch.
3. Select **AI Thinker ESP32-CAM** as board.
4. Flash firmware via USB-TTL adapter.

### Configure Wi-Fi (optional)
Update these lines in the sketch before flashing:
```cpp
const char* ssid = "YourWiFiName";
const char* password = "YourPassword";
```

---

## 📊 Dataset & Training

We collected over **200+ labeled images** of pigs with visible disease symptoms including:

- Skin rashes and redness
- Visible sores or lesions
- Unusual color tone changes

Images were manually labeled and can be used to train a lightweight model in Edge Impulse, TensorFlow Lite, or similar tools for future upgrades.

---

## 🐷 Field Deployment & Evaluation

- 📍 Location: Local pig farm in Uganda
- 🧪 Deployment involved real pigs in different lighting and pen environments.
- 📷 Camera mounted above walkway; system monitored and logged detections.

---

## 🚧 Known Limitations

- 📸 Accuracy affected by poor lighting or camera angle.
- 🧪 No deep-learning model in current version (uses rule-based RGB thresholding).
- ⚡ ESP32-CAM has limited processing power for complex ML inferences.

---

## 🔭 Future Work

- ✅ Integrate Edge Impulse-trained ML model.
- ✅ Automate alerts via MQTT/HTTP (IoT dashboard).
- ✅ Add behavioral tracking from video (activity, posture).
- ✅ Field-scale deployment in larger herds.

---

## 🧑‍💻 Contributors

- Ssenyange Allan – Hardware Integration & Camera Setup  
- Omara Emmanuel – Deployment, Data Collection  
- Kimera Dave David – System Design & Architecture  
- Ebaju Edward – Image Processing & Classification Logic  
- Nabasirye Seanice – Field Research & Documentation

---

## 📜 License

This project is licensed under the MIT License – open for improvement and adaptation.

---

## 🔗 Useful Links

- [ESP32-CAM Docs](https://randomnerdtutorials.com/esp32-cam-video-streaming-web-server-camera-home-surveillance/)
- [Edge Impulse](https://www.edgeimpulse.com/)
- [Arduino IDE Setup for ESP32](https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html)
