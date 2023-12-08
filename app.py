from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import time
import threading
import mjpeg_server as cam
import pigpio
from time import sleep


# using PIGPIO library to control servo
servo=18
feeder=pigpio.pi()
# Set gpio mode from pin to output
feeder.set_mode(servo, pigpio.OUTPUT)
# Sets frequency in hertz of servo
feeder.set_PWM_frequency(servo, 50)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings (False)
GPIO.setup(PIN, GPIO.OUT)

# used to debug errors
COUNT=0


# generate Flask App
app = Flask(__name__)


# turns camera on            
@app.route("/camera_on", methods=["POST"])
def camera_on():
    global COUNT
    COUNT+=1
    try:
        # create address to be used in live stream
        address = ('', 8000)
        # server created to put camera on webpage
        server=cam.StreamingServer(address,cam.StreamingHandler)
        # server will stay on until the host is gone
        server.serve_forever()
        print ('Stop server')
        return "Stop Stream"
    finally:
        # catches faultey initial click to stream
        if COUNT==2:
            print("Stop fin")
            return "Stop Stream"
        else:
            # avoids issues that may be resulted in the server address already in use
            print(COUNT)
            return "Stop Stream"

# Camera Off
@app.route("/Stop_Stream", methods=["POST"])
def Stop_stream():
    print("Click to Stream")
    return "Click to Stream"

# Dispense Treats
@app.route("/Dispense", methods=["POST"])
def dispense():
    # Creating movement of servo, 90 degrees-180 degrees
    feeder.set_servo_pulsewidth(servo,500)
    sleep(.5)
    feeder.set_servo_pulsewidth(servo,1500)
    sleep(.5)
    feeder.set_servo_pulsewidth(servo, 2500)
    sleep(1)
    # Stops Pulses to GPIO
    feeder.set_PWM_dutycycle(servo, 0)
    # If PWM is currently active on the GPIO it will be switched off and then back on at the new frequency.
    feeder.set_PWM_frequency(servo,0)
    return "Dispense Another"

# Dispense more Treats
@app.route("/Dispense_Another", methods=["POST"])
def dispense_another():
    # Same format as Dispense()
    # Creating movement of servo, 90 degrees-180 degrees
    feeder.set_servo_pulsewidth(servo,500)
    sleep(.5)
    feeder.set_servo_pulsewidth(servo,1500)
    sleep(.5)
    feeder.set_servo_pulsewidth(servo, 2500)
    sleep(1)
    # Stops Pulses to GPIO
    feeder.set_PWM_dutycycle(servo, 0)
    # If PWM is currently active on the GPIO it will be switched off and then back on at the new frequency.
    feeder.set_PWM_frequency(servo,0)
    return "Dispense"

# Home page 
@app.route("/", methods=["GET"])
def home():
    # Render main.html to be the webpage, server will need to be deployed for production
    return render_template("main.html", title="main", name="Abigail Wright")


# Server using flask, will need to generate different port for production
if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000)
