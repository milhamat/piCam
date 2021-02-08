from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.annotate_text = 'Hello World'
camera.annotate_text_size = 50
sleep(3)
camera.capture('/home/pi/piCam/camDoc/text.jpg')
camera.stop_preview()
