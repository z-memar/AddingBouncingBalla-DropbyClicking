# pygame demo using Ball class, bounce many balls

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random
from Ball import *  # bring in the Ball class code
from SimpleButton import *
from Drop import *

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_BALLS = 3

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  # set the speed (frames per second)

# 4 - Load assets: image(s), sounds, etc.
img_ball_down = 'images/newBallDown.png'
img_ball_up = 'images/newBallUp.png'
ball_btn = SimpleButton(window, (0,0,150, 50), img_ball_up,img_ball_down) 
img_Drop_up = 'images/newDropUp.png'
img_Drop_down = 'images/newDropDown.png'
drop_btn = SimpleButton(window, (490,0,150, 50),  img_Drop_up,img_Drop_down)
 
# 5 - Initialize variables
ballList = [] 
dropList = []
# 6 - Loop forever
while True:
    
    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        clicked = ball_btn.handleEvent(event)     
        if clicked:
            oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
            ballList.append(oBall)
            
        clicked = drop_btn.handleEvent(event)     
        if clicked:
            oDrop = Drop(window, WINDOW_WIDTH, WINDOW_HEIGHT)
            dropList.append(oDrop) 
        

    # 8 - Do any "per frame" actions
    for oBall in ballList:
        oBall.update()  # tell each ball to update itself
    for oDrop in dropList:
        oDrop.update()
        
   # 9 - Clear the screen before drawing it again
    window.fill(BLACK)

    # 10 - Draw the screen elements
    ball_btn.draw()
    drop_btn.draw()
    for oBall in ballList:
        oBall.draw()   # tell each ball to draw itself
    for oDrop in dropList:
        oDrop.draw() 
    # 11 - Update the screen
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make PyGame wait the correct amount


