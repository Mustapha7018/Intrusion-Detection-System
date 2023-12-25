import os
import cv2
import time
import serial
import smtplib
from dotenv import load_dotenv
from twilio.rest import Client
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from twilio.base.exceptions import TwilioRestException

# Function to capture an image using the laptop's camera
def capture_image(image_path):
    cap = cv2.VideoCapture(0)  # Start the camera

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera")
        return False

    # Capture a single frame
    ret, frame = cap.read()

    if ret:
        # Save the captured image to the specified path
        cv2.imwrite(image_path, frame)
    else:
        print("Error: Could not capture an image")

    # Release the camera
    cap.release()
    return ret

# Twilio setup
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_client = Client(account_sid, auth_token)
twilio_number = os.getenv('TWILIO_NUMBER')
my_number = os.getenv('MY_NUMBER')

# emergency number here is security
emergency_number = os.getenv('EMERGENCY_NUMBER')

# Email setup
smtp_server = os.getenv('SMTP_SERVER')
smtp_port = os.getenv('SMTP_PORT')
email_address = os.getenv('EMAIL_ADDRESS')
email_password = os.getenv('EMAIL_PASSWORD')

# Serial setup
arduino = serial.Serial('/dev/cu.usbmodem141201', 9600)  # Arduino's COM port


def send_sms():
    message = twilio_client.messages.create(
        body="Intruder Detected!",
        from_=twilio_number,
        to=my_number
    )
    print(f"SMS sent: {message.sid}")


def send_email(image_path):
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = email_address
    msg['Subject'] = "Intruder Alert!"

    with open(image_path, 'rb') as f:
        img = MIMEImage(f.read())
        msg.attach(img)

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_address, email_password)
    server.send_message(msg)
    server.quit()
    print("Email sent with image")

    
def make_emergency_call():
    try:
        call = twilio_client.calls.create(
            url='http://demo.twilio.com/docs/voice.xml',
            to=emergency_number,
            from_=twilio_number,
        )
        print(f"Emergency call made: {call.sid}")
    except TwilioRestException as e:
        print(f"TwilioRestException: {e}")
        print(f"Error code: {e.code}")
        print(f"Error message: {e.msg}")
        print(f"More info: {e.info}")

              
while True:
    if arduino.readline().decode('utf-8').strip() == "INTRUDER DETECTED":
        image_path = 'captured_image.jpg'
        if capture_image(image_path):
            send_sms()
            send_email(image_path)
            make_emergency_call()


try:
    arduino = serial.Serial('/dev/cu.usbmodem141201', 9600, timeout=1) 
    time.sleep(2)  
    for i in range(10):
        if arduino.in_waiting > 0:
            line = arduino.readline().decode('utf-8').rstrip()
            print(line)
        time.sleep(1)

except serial.SerialException as e:
    print("Error:", e)
finally:
    arduino.close()