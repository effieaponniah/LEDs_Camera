# Written by Effiea Ponniah
# Date: August 5, 2020
# Program Function: Simple Python application to light a couple of LEDs following
# by capture photo and a short video to demonstrate how to communicate through GPIO 
# pins and camera using Python

import time
from picamera import PiCamera
from gpiozero import LED
from gpiozero import MotionSensor

my_led = LED(4)
camera = PiCamera()
camera.resolution = (640, 480)
camera.vflip = True
camera.hflip = True

for index in range(3):
    my_led.on()
    time.sleep(1)
    my_led.off()
    time.sleep(1)


'''
 while True:
    pir.wait_for_motion()
    print("Motion Detetced")
    my_led.on()
'''
camera.start_preview()
time.sleep(2)

camera.capture("effieademo.jpg")

camera.start_recording("effieademo_movie.h264")
time.sleep(5)
camera.stop_recording()
camera.close()

my_led.on()
time.sleep(1)
my_led.off()
time.sleep(1)
exit
