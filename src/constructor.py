import pygame, sys
from pygame.locals import *
from settings import *
from random import randrange


def const_fi(point_x = 0, point_y = 0, fig_w = 50, fig_h = 50, 
    color = (255, 255, 255), direction = 3, ratio : int = 0, image = None) -> (dict):
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











