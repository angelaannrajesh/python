import pygame
import random
import math
from pygame import mixer
# to initialize python module we write init
pygame.init()
# making screen
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Game")
icon = pygame.image.load("spaceship_imgs/spaceimg.png")
pygame.display.set_icon(icon)

