import pygame, sys
from pygame.locals import *

def draw_ship(color, coord):
    pygame.draw.polygon(DISPLAYSURF, color,((coord[0],coord[1]),(coord[0]+5,coord[1]+5),(coord[0],coord[1]-5),(coord[0]-5,coord[1]+5)))

main_window_width = 500
main_window_height = 400

pygame.init()

FPS = 10
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((main_window_width,main_window_height),0,32)
pygame.display.set_caption('Drawing')

BLACK = (  0,  0,  0)
WHITE = (255,255,255)
RED   = (255,  0,  0)
GREEN = (  0,255,  0)
BLUE  = (  0,  0,255)


shipx = 250
shipy = 200

direction = 'right'


while True:
    DISPLAYSURF.fill(BLACK)
    draw_ship(GREEN,(shipx,shipy))
    
    if direction == 'right':
        shipx += 5
        if shipx >= 400:
            direction = 'down'
    elif direction == 'down':
        shipy += 5
        if shipy >= 300:
            direction = 'left'
    elif direction == 'left':
        shipx -= 5
        if shipx <= 100:
            direction = 'up'
    elif direction == 'up':
        shipy -= 5
        if shipy <= 100:
            direction = 'right'
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)

