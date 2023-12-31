# Intrusion Detection System 🚨

This project is an Intrusion Detection System that uses a combination of Python and Arduino to detect intruders and alert the user via SMS, email, and an emergency call.

## 🛠 Components

- 🐍 Python script for image capture and notifications (`capture.py`)
- 🤖 Arduino sketch for detecting motion and triggering alerts (`test2.ino`)
- 📦 List of Python dependencies (`requirements.txt`)


## 🚀 Setup and Installation

### Python Environment

1. **Install Python Dependencies**: Ensure you have Python installed on your system. Then, install the required packages using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt



## 🌐 Environment Variables

Set up the necessary environment variables for Twilio and email configurations. You can use a `.env` file or set them directly in your environment.

### Arduino Setup

*   **Arduino Sketch**: The `test2.ino` file contains the Arduino code. Upload this sketch to your Arduino board.
*   **Hardware Connections**: Connect the PIR sensor, buzzer, and LED to the Arduino as per the pin configurations in the sketch.

  
## 🏃 Running the System

*   **Start the Python Script**: Run the `capture.py` script. This script will communicate with the Arduino and wait for the intrusion detection signal.
*   **Intrusion Detection**: Once the PIR sensor detects motion, the Arduino sends a signal to the Python script, which then captures an image, sends an SMS and email, and makes an emergency call.


## 🖥 Simulating on Tinkercad

To simulate this project on Tinkercad, follow these steps:

1.  **Create a New Circuit**: Go to Tinkercad and create a new circuit.
2.  **Add Components**: Place an Arduino board, PIR sensor, buzzer, and LED on the breadboard.
3.  **Wire the Components**: Connect them according to the pin configurations in the `test2.ino` sketch.
4.  **Upload the Arduino Code**: Copy the contents of `test2.ino` into the Arduino code editor in Tinkercad and upload it to the virtual Arduino.
5.  **Simulate**: Start the simulation. The PIR sensor in Tinkercad should now be able to trigger the buzzer and LED, simulating the intrusion detection.


## 📁 Repository Contents

*   `capture.py`: Python script for capturing images and sending alerts.
*   `requirements.txt`: List of Python dependencies.
*   `test2.ino`: Arduino sketch for motion detection.
