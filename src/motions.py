from images import *
from pygame.locals import *
from settings import *

def motion_background(surface, list_images, bg_width, scroll_x, speed):
    """
    This function scrolls a series of images horizontally on a surface to create a motion background
    effect.
    
    :param surface: The `surface` parameter in the `motion_background` function is typically a pygame
    Surface object where the images will be drawn onto
    :param list_images: `list_images` is a list containing images that will be used for the motion
    background effect in the `motion_background` function
    :param bg_width: The `bg_width` parameter in the `motion_background` function represents the width
    of the background image or surface over which the motion effect is applied. It is used to calculate
    the position of the images being scrolled based on the scrolling speed and other factors in the
    function
    :param scroll_x: `scroll_x` is the current scroll position along the x-axis of the background. It is
    used to determine how much the background should be shifted horizontally to create a scrolling
    effect
    :param speed: The `speed` parameter in the `motion_background` function represents the speed at
    which the background images will scroll horizontally on the surface. It affects how fast the
    background appears to move as the `scroll_x` value changes
    Args:
        surface (_type_): _description_
        list_images (_type_): _description_
        bg_width (_type_): _description_
        scroll_x (_type_): _description_
        speed (_type_): _description_
    """
    for x in range(5):
        for i, img in enumerate(list_images):
            position_x = (x * bg_width) - (scroll_x * (speed + i * 0.2))
            surface.blit(img, (position_x, 0))
    
    for i, img in enumerate(list_images):
        position_x = ((5 * bg_width) - (scroll_x * (speed + i * 0.2)))
        surface.blit(img, (position_x, 0))




