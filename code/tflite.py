from time import sleep
import pygame
import pygame.camera
from lobe import ImageModel
from pygame.locals import *
import os 


pygame.camera.init()
pygame.mixer.init()

model = ImageModel.load('/home/pi/Desktop/model') # model 


pygame.mixer.music.load("/home/pi/Python-3.7.4/face3/Audio.wav")

#print(pygame.camera.list_cameras())


def take_photo():

    #camlist = pygame.camera.list_cameras()
    #cam = pygame.camera.Camera(camlist[0],(640,480))
    cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
    cam.start()
    sleep(1)
    image = cam.get_image()
    pygame.image.save(image, '/home/pi/images/image1.jpg') # save image 
    cam.stop()
    sleep(2)

def label_select(label):
    print(label)
    if label == "without_mask":
        pygame.mixer.music.play()
        sleep(1)

    else:
        #label == "with_mask":
        #pygame.mixer.pause()
        sleep(2)
        

while True: 
    take_photo()
    label = model.predict_from_file('/home/pi/images/image1.jpg') # save image file dictonary 
    label_select(label.prediction)
    sleep(2)
