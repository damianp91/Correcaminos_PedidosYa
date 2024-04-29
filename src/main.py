from pygame.locals import *
import pygame, sys
from settings import *
from random import randrange, choice
#import images
from constructor import *

pygame.init()

clock = pygame.time.Clock()

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Correcaminos PedidosYa.")

coin_x = 20
coin_y = 20
nun_coin = 6

coins = []

block = const_fi(point_x=randrange(0, WIDTH - coin_x), point_y=randrange(0, HEIGHT - coin_y),
                direction= choice(dir))

for coin in range(nun_coin):
    coins.append(const_fi(randrange(0, WIDTH - coin_x), randrange(0, HEIGHT - coin_y),
                coin_x, coin_y, (255, 255, 100), 45))

while True:
    
    clock.tick(FPS)
    
    for event in pygame.event.get():
        
        if event.type == QUIT:
            sys.exit()
    
    # Impact of the scuare
    if block["block"].right >= WIDTH:
        if block["direction"] == DR:
            block["direction"] = DL
        elif block["direction"] == UR:
            block["direction"] = UL
        block["color"] = color_surprise()
    elif block["block"].bottom >= HEIGHT:
        if block["direction"] == DR:
            block["direction"] = UR
        elif block["direction"] == DL:
            block["direction"] = UL
        block["color"] = color_surprise()
    elif block["block"].left <= 0:
        if block["direction"] == UL:
            block["direction"] = UR
        elif block["direction"] == DL:
            block["direction"] = DR
        block["color"] = color_surprise()
    elif block["block"].top <= 0:
        if block["direction"] == UL:
            block["direction"] = DL
        elif block["direction"] == UR:
            block["direction"] = DR
        block["color"] = color_surprise()
    
    # Direction of the scare
    if block["direction"] == DR:
        block["block"].top += 1
        block["block"].left +=  1
    elif block["direction"] == UR:
        block["block"].top -= 1
        block["block"].left +=  1
    elif block["direction"] == UL:
        block["block"].top -= 1
        block["block"].left -=  1
    elif block["direction"] == DL:
        block["block"].top += 1
        block["block"].left -=  1
    
    display.fill((0, 0, 0))
    
    for coin in coins:
        pygame.draw.rect(display, coin["color"], coin["block"])
    
    pygame.draw.rect(display, block["color"], block["block"])
    
    pygame.display.flip()

