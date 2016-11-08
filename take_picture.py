import pygame
import pygame.camera
import argparse

pygame.camera.init()
camera_list = pygame.camera.list_camera() # Get list of camera devices
cam = pygame.camera.Camera(camera_list[0],(640,480))
cam.start()
img = cam.get_image()
pygame.image.save(img,"filename.jpg")


