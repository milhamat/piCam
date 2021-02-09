#Camera White Balance
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.awb_mode = 'sunlight'
sleep(3)
camera.capture('/home/pi/piCam/camDoc/sunlight.jpg')
camera.stop_preview()

#off
#auto
#sunlight
#cloudy
#shade
#tungsten
#flourescent
#incandescent
#flash
#horizon