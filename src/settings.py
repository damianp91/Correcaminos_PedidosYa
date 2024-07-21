from random import randrange
import pygame


# Screen
WIDTH = 600
HEIGHT = 1000
center_x = WIDTH // 2
center_y = HEIGHT // 2
center_display = (center_x, center_y)
size_display = (WIDTH, HEIGHT)
origin_display = (0, 0)
limit_road_rider = 601
up_down_rider = 50

# Motion speed
FPS = 60


# Speed 
SPEED = 10 # velocidad por pixeles


# Random color
def color_surprise() -> (tuple):
    """Create a tuple with code RGB
    Returns:
        tuple: tuple with three numbers from 0 to 255
    """
    r = randrange(0, 255)
    g = randrange(0, 255)
    b = randrange(0, 255)
    return (r, g, b)

green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
yellow = (255, 255, 100)
white = (255, 255, 255)
blue = (0, 0, 255)
costume = (78, 87, 146)


# Este ya no lo uso para movimiento
DL = 7
DR = 9
UR = 3
UL = 1

# Move
move_up = False
move_dw = False
move_rig = False
move_lef = False


# Coins
coin_x = 30
coin_y = 30
nun_coin = 25
count_coins = 0
coins = []


# Size characters
bici_w = 150
bici_h = 150


# Size background
skay_w = pygame.image.load("./src/images/day.png").get_width()


