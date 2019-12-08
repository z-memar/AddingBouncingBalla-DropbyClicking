import pygame
from pygame.locals import *
import random

# Drop CLASS 
class Drop():

    def __init__(self, window, windowWidth, windowHeight):
        self.window = window  # remember the window, so we can draw later
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.dropImage = pygame.image.load("images/drop.png")
        # A rect is made up of [x, y, width, height]
        dropRect = self.dropImage.get_rect()
        self.width = dropRect[1]
        self.height = dropRect[2]
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height
        
        # Pick a random starting position 
        self.x = random.randrange(0, self.maxWidth)
        self.y = 0

        # Choose a random speed in both the x and y directions
        self.xSpeed = random.randrange(3, 6)       
        self.ySpeed = random.randrange(3, 6)

    def update(self):
        # check for hitting a floor.  If so, come from the top again 
        if self.y == self.windowHeight:
            self.y = 0
            self.x = random.randrange(0, self.maxWidth)
        
        # update the balls x and y, based on the speed in two directions
        self.y = self.y + self.ySpeed

    def draw(self):
        self.window.blit(self.dropImage, (self.x, self.y))
