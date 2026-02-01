# 🐍 Python Projects Collection

A collection of fun and useful Python projects created by **Rehan**. These projects demonstrate various Python concepts including face recognition, text-to-speech, API integration, and more.

---

## 📋 Table of Contents

1. [Face Recognition Attendance System](#1-face-recognition-attendance-system)
2. [Weather App](#2-weather-app)
3. [Guess the Number Game](#3-guess-the-number-game)
4. [Password Generator](#4-password-generator)
5. [Joke Speaker](#5-joke-speaker)
6. [QR Code Generator](#6-qr-code-generator)
7. [Robo Speaker](#7-robo-speaker)
8. [Installation](#installation)
9. [Requirements](#requirements)

---

## 1. 👤 Face Recognition Attendance System

**File:** `Face_Recognition_Attendance_System..py`

An automated attendance system using facial recognition technology. It captures video from your webcam, identifies registered faces, and logs attendance with timestamps.

### Features:
- ✅ Real-time face detection and recognition using webcam
- ✅ Automatic attendance marking with date and time
- ✅ Saves attendance to a CSV file (named by current date)
- ✅ Displays "Present" status on screen when face is recognized
- ✅ Supports multiple registered users

### How to Use:
1. Add face images to the `Faces/` folder (e.g., `Rehan.jpg`, `Wafiya.png`)
2. Update the code to include new face encodings
3. Run the script
4. Press **'Q'** to quit

### Dependencies:
```
face_recognition, opencv-python, numpy
```

---

## 2. 🌤️ Weather App

**File:** `Weather_App.py`

A voice-enabled weather application that fetches real-time weather data for any Indian city using the OpenWeatherMap API.

### Features:
- ✅ Fetches current weather conditions (sunny, cloudy, rainy, etc.)
- ✅ Displays temperature in Celsius
- ✅ Shows "Feels Like" temperature
- ✅ Reports visibility in kilometers
- ✅ **Text-to-Speech** - speaks all weather information aloud
- ✅ Error handling for invalid cities and network issues

### How to Use:
1. Run the script
2. Enter the city name (Indian cities)
3. Listen to and view the weather report

### Dependencies:
```
requests, pywin32
```

---

## 3. 🎯 Guess the Number Game

**File:** `Guess_number.py`

A classic number guessing game where players try to guess a randomly generated number within a custom range.

### Features:
- ✅ Custom range selection (lower and upper limits)
- ✅ Hints provided (higher/lower feedback)
- ✅ Input validation for invalid entries
- ✅ Option to quit mid-game by pressing 'Q'
- ✅ Play again functionality
- ✅ Prevents invalid ranges (lower > upper)

### How to Use:
1. Run the script
2. Enter lower and upper limits
3. Start guessing!
4. Press **'Q'** to quit or **'Y'** to play again

### Dependencies:
```
None (uses built-in modules only)
```

---

## 4. 🔐 Password Generator

**File:** `Guess_password.py`

A secure random password generator that creates strong passwords using letters, numbers, and special characters.

### Features:
- ✅ Custom password length
- ✅ Includes uppercase & lowercase letters (A-Z, a-z)
- ✅ Includes digits (0-9)
- ✅ Includes special characters (!@#$%^&* etc.)
- ✅ Cryptographically random selection

### How to Use:
1. Run the script
2. Enter desired password length
3. Copy your generated secure password

### Dependencies:
```
None (uses built-in modules only)
```

---

## 5. 😂 Joke Speaker

**File:** `Joke_Speaker.py`

A fun application that tells programming jokes and speaks them aloud using text-to-speech technology.

### Features:
- ✅ Fetches random programming/tech jokes
- ✅ **Text-to-Speech** - reads jokes aloud
- ✅ Custom number of jokes selection
- ✅ Option to continue or quit after each joke
- ✅ Input validation for positive numbers
- ✅ Friendly goodbye message

### How to Use:
1. Run the script
2. Enter how many jokes you want to hear
3. Enjoy the jokes!
4. Press **'Q'** to quit or any key to continue

### Dependencies:
```
pyjokes, pywin32
```

---

## 6. 📱 QR Code Generator

**File:** `QR_Code generator.py`

A simple QR code generator that creates customizable QR codes for any URL or text.

### Features:
- ✅ High error correction level (readable even if partially damaged)
- ✅ Customizable colors (fill and background)
- ✅ Adjustable box size and border
- ✅ Saves QR code as PNG image
- ✅ Currently configured for GitHub profile

### How to Use:
1. Modify the URL/data in the script
2. Run the script
3. Find the generated QR code image in the project folder

### Dependencies:
```
qrcode, Pillow
```

---

## 7. 🤖 Robo Speaker

**File:** `Robo_Speaker.py`

A text-to-speech application that converts any text input into spoken words using Windows SAPI.

### Features:
- ✅ Converts text to speech in real-time
- ✅ Adjustable speaking speed
- ✅ Continuous input mode (speak multiple texts)
- ✅ Exit by pressing 'Q'
- ✅ Friendly farewell message

### How to Use:
1. Run the script
2. Type any text and press Enter to hear it
3. Press **'Q'** to exit

### Dependencies:
```
pywin32
```

---

## 📦 Installation

### Install All Dependencies:

```bash
pip install face_recognition opencv-python numpy requests pyjokes qrcode Pillow pywin32
```

### For Face Recognition (Windows):
If you encounter issues installing `face_recognition`, try:
```bash
pip install dlib-bin
pip install --no-deps face_recognition face-recognition-models Click Pillow
```

---

## 📋 Requirements

| Project | Python Packages |
|---------|-----------------|
| Face Recognition Attendance | `face_recognition`, `opencv-python`, `numpy` |
| Weather App | `requests`, `pywin32` |
| Guess the Number | *Built-in modules only* |
| Password Generator | *Built-in modules only* |
| Joke Speaker | `pyjokes`, `pywin32` |
| QR Code Generator | `qrcode`, `Pillow` |
| Robo Speaker | `pywin32` |

---

## 🖥️ System Requirements

- **Operating System:** Windows (for text-to-speech features using SAPI)
- **Python Version:** 3.8 or higher recommended
- **Webcam:** Required for Face Recognition Attendance System

---

## 📁 Project Structure

```
Python Projects/
├── Face_Recognition_Attendance_System..py
├── Weather_App.py
├── Guess_number.py
├── Guess_password.py
├── Joke_Speaker.py
├── QR_Code generator.py
├── Robo_Speaker.py
├── Faces/
│   ├── Rehan.jpg
│   └── Wafiya.png
├── README.md
└── YYYY-MM-DD.csv (attendance files)
```

---

## 👨‍💻 Author

**Rehan**

- GitHub: [MdRehan76](https://github.com/MdRehan76)

---

## 📄 License

This project is open source and available for learning purposes.

---

*Happy Coding! 🚀*

