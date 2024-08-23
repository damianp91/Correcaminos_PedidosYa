from pygame.locals import *
from settings import *
from random import randrange
from images import *
from constructor import *
from colitions import *
from motions import *


pygame.init()

clock = pygame.time.Clock()

# Settings of font
source = pygame.font.Font(None, 40)

# Create rider
block = const_fi(0, 700, bici_w, bici_h, white, 0, -1, moto_bike)

avance = WIDTH + 100

# Music 
playing_music = True

# Create coins
for coin in range(nun_coin):
    coins.append(const_fi(randrange(0, WIDTH - coin_x), randrange(800, 1000 - coin_y),
                coin_x, coin_y, yellow, 0, 12, image_coin))

scroll = 0
playing = True

menu_init()

pygame.mixer.music.load("./src/sounds/while_game.mp3") # Fondo de juego
pygame.mixer.music.play(-1, 2000)
pygame.mixer.music.set_volume(0.2)

mov_list_images(init_app, display)

#video_play('./src/videos/Pickup.mp4')

while playing:
    
    clock.tick(FPS)
    
    for event in pygame.event.get():
        print(event)
        if event.type == QUIT:
            playing = False
        
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                move_rig = True
            if event.key == K_LEFT:
                move_lef = True
            if event.key == K_UP:
                move_up = True
            if event.key == K_DOWN:
                move_dw = True
            
            if event.key == K_m:
                if playing_music:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                playing_music = not playing_music
            
            if event.key == K_p:
                if playing_music:
                    pygame.mixer.music.pause()
                advisor_text(display, "Pause", source, center_display, red, black)
                pygame.display.flip()
                wait_player()
                if playing_music:
                    pygame.mixer.music.unpause()
        
        
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                move_rig = False
            if event.key == K_LEFT:
                move_lef = False
            if event.key == K_UP:
                move_up = False
            if event.key == K_DOWN:
                move_dw = False 
    
    # Direction of the screen
    if move_up and block["block"].top >= limit_road_rider:
        block["block"].top -= up_down_rider
    elif move_dw and block["block"].bottom < HEIGHT:
        block["block"].bottom +=  up_down_rider
    elif move_lef and block["block"].left >= 0:
        block["block"].left -= SPEED
    elif move_rig and block["block"].right <= WIDTH:
        block["block"].right += SPEED
    
    # for coin in coins[:]:
    #     if detected_colition(coin["block"], block["block"]):
    #         coins.remove(coin)
    #         count_coins += 1
    #         if count_coins >= nun_coin:
    #             count_coins = 0
    #             make_coins(nun_coin, coins, image_coin)
    
    
    # Blit text in the screen
    
    
    
    text = source.render(f"Coins: {count_coins}", True, yellow)
    rect_text = text.get_rect()
    rect_text.center = (center_x, 12)
    
    scroll += SPEED
    
    motion_background(display, skay_day, skay_w, scroll, 1)
    
    display.blit(text, rect_text)
    
    # Coins
    # for coin in coins:
    #     display.blit(coin["img"], coin["block"])
    
    # Vehicles
    v_1 = const_fi(avance, 700, 200, 100, white, 0, -1, vec_1)
    v_2 = const_fi(avance + 1000, 810, 200, 100, white, 0, -1, vec_2)
    v_3 = const_fi(avance + 2000, 895, 200, 100, white, 0, -1, vec_3)
    v_4 = const_fi(avance + 2100, 810, 200, 100, white, 0, -1, vec_4)
    v_5 = const_fi(avance + 3300, 700, 200, 100, white, 0, -1, vec_5)
    v_6 = const_fi(avance + 3800, 895, 200, 100, white, 0, -1, vec_6)
    display.blit(v_1["img"], v_1["block"])
    display.blit(v_2["img"], v_2["block"])
    display.blit(v_3["img"], v_3["block"])
    display.blit(v_4["img"], v_4["block"])
    display.blit(v_5["img"], v_5["block"])
    display.blit(v_6["img"], v_6["block"])
    avance -= 4
    
    # Rider
    display.blit(block["img"], block["block"])
    
    # verificar imagen
    #pygame.draw.rect(display, (255, 0, 0), block["block"], 2)
    
    pygame.display.flip()

pygame.quit()

