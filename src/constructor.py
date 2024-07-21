import pygame, sys
from pygame.locals import *
from settings import *
from random import randrange, choice


def const_fi(point_x = 0, point_y = 0, fig_w= 50, fig_h= 50, 
    color = (255, 255, 255), direction = 0, ratio = -1, image = None) -> (dict):
    """
        Build a dictionary with specific elements for create a block of type Rect with it color,
        dimensions and shape.
    Args:
        point_x (int): Point of reference in axe x. Defaults to 0,
        point_y (int): Point of reference in axe y. Defaults to 0,
        fig_w (int) = 50: Dimension of the block in it width,
        fig_y (int) = 50: Dimension of the block in it height,
        color : (tuple) = (0, 0, 0): Tuple with number of the code of it color in RGB,
        direction : (int) = 3: Direction that will follow the block according to programming in keyboard,
        ratio : (int) = 0: Shape that you want to take the block
        image = None: Image that to show.
    Returns:
        dict: dictionary with elemnts of the figure.
    """
    if image:
        image = pygame.transform.scale(image, (fig_w, fig_h))
    
    return {"block":pygame.Rect(point_x, point_y, fig_w, fig_h), "color":color, "direction":direction,
            "ratio":ratio, "img": image}


def make_coins(num_coun : int, list_coin : list, image= None) -> (list):
    """_summary_
    Args:
        num_coun (_type_, optional): _description_. Defaults to None)->(list.
    Returns:
        _type_: _description_
    """
    
    for fig in range(num_coun):
        fig = const_fi(randrange(0, WIDTH - coin_x), randrange(0, HEIGHT - coin_y),
                coin_x, coin_y, yellow, 0, 12, image)
        list_coin.append(fig)
    
    return list_coin


def ended_game():
    pygame.quit() # Esta es la inversa de pygame.init aca avisamos que vamos a salir del programa
    sys.exit() # Al momento de dar x a la pantalla va a salir sin mostrar error


def wait_player():
    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                ended_game()
            
            if e.type == KEYDOWN:
                if e.type == K_ESCAPE:
                    ended_game()
                return


def advisor_text(surfice, tex, font, coordenates, color_font, color_back= None):
    sup_text = font.render(tex, True, color_font, color_back)
    rect_tex = sup_text.get_rect()
    rect_tex.center = coordenates
    surfice.blit(sup_text, rect_tex)









