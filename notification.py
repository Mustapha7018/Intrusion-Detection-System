import serial
import smtplib
from twilio.rest import Client
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# [Add your method for image capture here]

# Twilio setup
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_client = Client(account_sid, auth_token)
twilio_number = 'your_twilio_number'
your_number = 'your_phone_number'
emergency_number = 'emergency_phone_number'

# Email setup
smtp_server = 'smtp.gmail.com'
smtp_port = 587
email_address = 'your_email@gmail.com'
email_password = 'your_password'

# Serial setup
arduino = serial.Serial('COM_PORT', 9600)  # Replace 'COM_PORT' with your Arduino's COM port

def send_sms():
    message = twilio_client.messages.create(
        body="Intruder Detected!",
        from_=twilio_number,
        to=your_number
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
    call = twilio_client.calls.create(
        to=emergency_number,
        from_=twilio_number,
        url='http://demo.twilio.com/docs/voice.xml'  # This URL should be replaced with your own call handling logic
    )
    print(f"Emergency call made: {call.sid}")

while True:
    if arduino.readline().decode('utf-8').strip() == "INTRUDER DETECTED":
        # [Capture image and save to a path]
        image_path = 'path_to_captured_image.jpg'
        send_sms()
        send_email(image_path)
        make_emergency_call()
