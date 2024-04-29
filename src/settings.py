from random import randrange


# Screen
WIDTH = 600
HEIGHT = 400
center_x = WIDTH // 2
center_y = HEIGHT // 2
center_display = (center_x, center_y)
size_display = (WIDTH, HEIGHT)
origin_display = (0, 0)


# Motion speed
FPS = 190


#Random color
def color_surprise() -> (tuple):
    """Create a tuple with code RGB
    Returns:
        tuple: tuple with three numbers from 0 to 255
    """
    r = randrange(0, 255)
    g = randrange(0, 255)
    b = randrange(0, 255)
    return (r, g, b)


#Move
UR = 9
DR = 3
UL = 7
DL = 1

dir = (UR, DR, UL, DL)

