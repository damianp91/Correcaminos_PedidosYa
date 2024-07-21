import pygame
from settings import *

# Backgraud day
skay_day = [pygame.transform.scale(pygame.image.load("./src/images/day.png"), (skay_w, HEIGHT)),
            pygame.transform.scale(pygame.image.load("./src/images/cloud_day.png"), (skay_w, HEIGHT)),
            pygame.transform.scale(pygame.image.load("./src/images/buildings.png"), (skay_w, HEIGHT)),
            pygame.transform.scale(pygame.image.load("./src/images/soil.png"), (skay_w, HEIGHT)),
            pygame.transform.scale(pygame.image.load("./src/images/buildings_front.png"), (skay_w, HEIGHT))]

# Backgraund sunset
# skay_sunset = [pygame.transform.scale(pygame.image.load("./images/skay_sunset.png"), (skay_w, HEIGHT)),
#             pygame.transform.scale(pygame.image.load("./images/cloud_sunset.png"), (skay_w, HEIGHT)),
#             pygame.transform.scale(pygame.image.load("./images/towers_back.png"), (skay_w, HEIGHT)),
#             pygame.transform.scale(pygame.image.load("./images/soil.png"), (skay_w, HEIGHT)),
#             pygame.transform.scale(pygame.image.load("./images/towers_front.png"), (skay_w, HEIGHT))]

# Backgraund night
# skay_night = [pygame.transform.scale(pygame.image.load("./images/skay_night.png"), (skay_w, HEIGHT)),
#             pygame.transform.scale(pygame.image.load("./images/cloud_night.png"), (skay_w, HEIGHT)),
#             pygame.transform.scale(pygame.image.load("./images/towers_back.png"), (skay_w, HEIGHT)),
#             pygame.transform.scale(pygame.image.load("./images/soil.png"), (skay_w, HEIGHT)),
#             pygame.transform.scale(pygame.image.load("./images/towers_front.png"), (skay_w, HEIGHT))]

# Objects
image_coin = pygame.image.load("./src/images/coin.png")

# rider
moto_bike = pygame.image.load("./src/images/rider.png")
