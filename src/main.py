from pygame.locals import *
import pygame, sys
from settings import *

pygame.init()

clock = pygame.time.Clock()

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Correcaminos PedidosYa.")

#Images


#main display


while True:
    for event in pygame.event.get():
        
        if event.type == QUIT:
            sys.exit()
    pygame.display.flip()

