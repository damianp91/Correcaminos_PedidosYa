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

# vehicles
vec_1 = pygame.image.load("./src/images_cars/auto1.png")
vec_2 = pygame.image.load("./src/images_cars/auto2.png")
vec_3 = pygame.image.load("./src/images_cars/auto3.png")
vec_4 = pygame.image.load("./src/images_cars/auto4.png")
vec_5 = pygame.image.load("./src/images_cars/auto5.png")
vec_6 = pygame.image.load("./src/images_cars/auto6.png")

# menus
title_menu = pygame.transform.scale(pygame.image.load("./src/images_menu/corre-caminos.png"), size_botton)
info_menu = pygame.transform.scale(pygame.image.load("./src/images_menu/informacion.png"), size_botton)
play_menu = pygame.transform.scale(pygame.image.load("./src/images_menu/jugar.png"), size_botton)
levels_menu = pygame.transform.scale(pygame.image.load("./src/images_menu/niveles.png"), size_botton)
top_menu = pygame.transform.scale(pygame.image.load("./src/images_menu/top_riders.png"), size_botton)
logo_menu = pygame.transform.scale(pygame.image.load("./src/images_menu/logo.png"), size_botton)


# # videos
# video_pikc_up = VideoFileClip('./src/videos/Pickup.mp4')
# video_pikc_out = VideoFileClip('./src/videos/Pickout.mp4')


# App ingreso
init_app = [pygame.transform.scale(pygame.image.load("./src/images_app_init/CELU00.png"), (WIDTH, HEIGHT)),
            pygame.transform.scale(pygame.image.load("./src/images_app_init/CELU01.png"), (WIDTH, HEIGHT)),
            pygame.transform.scale(pygame.image.load("./src/images_app_init/CELU02.png"), (WIDTH, HEIGHT)),
            pygame.transform.scale(pygame.image.load("./src/images_app_init/CELU03.png"), (WIDTH, HEIGHT)),
            pygame.transform.scale(pygame.image.load("./src/images_app_init/CELU04.png"), (WIDTH, HEIGHT)),
            pygame.transform.scale(pygame.image.load("./src/images_app_init/CELU05.png"), (WIDTH, HEIGHT)),
            pygame.transform.scale(pygame.image.load("./src/images_app_init/CELU06.png"), (WIDTH, HEIGHT)),
            pygame.transform.scale(pygame.image.load("./src/images_app_init/CELU07.png"), (WIDTH, HEIGHT)),
            pygame.transform.scale(pygame.image.load("./src/images_app_init/CELU08.png"), (WIDTH, HEIGHT)),
            pygame.transform.scale(pygame.image.load("./src/images_app_init/CELU09.png"), (WIDTH, HEIGHT)),
            pygame.transform.scale(pygame.image.load("./src/images_app_init/CELU10.png"), (WIDTH, HEIGHT))]