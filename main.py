import pygame, sys
from pygame.locals import *

main_window_width = 500
main_window_height = 400

pygame.init()
DISPLAYSURF = pygame.display.set_mode((main_window_width,main_window_height),0,32)
pygame.display.set_caption('Drawing')

BLACK = (  0,  0,  0)
WHITE = (255,255,255)
RED   = (255,  0,  0)
GREEN = (  0,255,  0)
BLUE  = (  0,  0,255)

DISPLAYSURF.fill(BLACK)

pygame.draw.polygon(DISPLAYSURF, GREEN,((250,200),(245,210),(250,206),(255,210)))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
