#Camera Exposure Mode
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.exposure_mode = 'beach'
sleep(2)
camera.capture('/home/pi/piCam/camDoc/beach.jpg')
camera.stop_preview()

#off
#auto
#night
#nightpreview
#backlight
#spotlight
#sport
#snow
#beach
#verylong
#fixedfps
#antishake
#fireworks

