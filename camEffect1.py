from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.image_effect = 'colorswap'
sleep(2)
camera.capture('/home/pi/piCam/camDoc/colorswap.jpg')
camera.stop_preview()




#none
#negative
#solarize
#sketch
#denoise
#emboss
#oilpaint
#hatch
#open
#pastel
#watercolor
#film
#blur
#saturation
#colorswap
#washedout
#posterise
#colorpoint
#colorbalance
#cartoon
#deinterlace1
#deinterlace2