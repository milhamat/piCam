from picamera import PiCamera
from time import sleep

camera = PiCamera()

def resCam():
    res = input('choose max or std : ')
    if res == 'Max' or res == 'max':
        camera.resolution = (2592, 1994)
        #using (2592,1994) will make the shot result more square than rectangle
    elif res == 'Std' or res == 'std':
        camera.resolution = (1920,1080)
        #using (1920,1080) will make the shot result more rectangle than rectangle
    
    camera.framerate = 15
    camera.start_preview()
    sleep(3)
    camera.capture('/home/pi/piCam/camDoc/max1.jpg')
    camera.stop_preview()
    
resCam()