import pygame, sys
from pygame.locals import *

main_window_width = 400
main_window_height = 300

pygame.init()
DISPLAYSURF = pygame.display.set_mode((main_window_width,main_window_height))
pygame.display.set_caption('Hello World!')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
