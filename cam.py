import picamera
from time import sleep

camera = picamera.PiCamera()

for i in range(10):
    camera.capture('image.jpeg')
    sleep(2)

