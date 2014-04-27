import pygame, sys
from pygame.locals import *

def draw_ship(color, coord):
    pygame.draw.polygon(DISPLAYSURF, color,((coord[0],coord[1]),(coord[0]+5,coord[1]+5),(coord[0],coord[1]-5),(coord[0]-5,coord[1]+5)))

main_window_width = 500
main_window_height = 400

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((main_window_width,main_window_height),0,32)
pygame.display.set_caption('Drawing')

BLACK = (  0,  0,  0)
WHITE = (255,255,255)
RED   = (255,  0,  0)
GREEN = (  0,255,  0)
BLUE  = (  0,  0,255)

DISPLAYSURF.fill(BLACK)
draw_ship(GREEN,(250,200))


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

