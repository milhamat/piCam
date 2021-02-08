from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.brightness = 70
sleep(2)
camera.capture('/home/pi/piCam/camDoc/bright.jpg')
camera.stop_preview()