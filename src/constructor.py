import pygame, sys
from pygame.locals import *
from settings import *
from random import randrange
from images import *

def const_fi(point_x = 0, point_y = 0, fig_w= 50, fig_h= 50, 
    color = (255, 255, 255), direction = 0, ratio = -1, image = None) -> (dict):
    """
        Build a dictionary with specific elements for create a block of type Rect with it color,
        dimensions and shape.
    Args:
        point_x (int):
            Point of reference in axe x. Defaults to 0,
        point_y (int):
            Point of reference in axe y. Defaults to 0,
        fig_w (int) = 50:
            Dimension of the block in it width,
        fig_y (int) = 50:
            Dimension of the block in it height,
        color (tuple) = (0, 0, 0):
            Tuple with number of the code of it color in RGB,
        direction (int) = 3:
            Direction that will follow the block according to programming in keyboard,
        ratio (int) = 0:
            Shape that you want to take the block
        image = None:
            Image that to show.
    Returns:
        dict: dictionary with elemnts of the figure.
    """
    if image:
        image = pygame.transform.scale(image, (fig_w, fig_h))
    
    return {"block":pygame.Rect(point_x, point_y, fig_w, fig_h), "color":color, "direction":direction,
            "ratio":ratio, "img": image}


def make_coins(num_coun : int, list_coin : list, image= None) -> (list):
    """
    Creates a specified number of coin objects and adds them to a list.
    
    Args:
        param num_coun (int):
            The `num_coun` parameter in the `make_coins` function represents the number of
            coins you want to create. It is an integer value that specifies how many coins will be generated
        param list_coin (list):
            The `list_coin` parameter is a list that will store the coin objects created in
            the `make_coins` function. Each coin object will be added to this list so that they can be accessed
            and used later in the program
        param image:
            The `image` parameter in the `make_coins` function is used to specify an image that
            will be associated with the coins being created. This image could be used to visually represent the
            coins in a graphical user interface or game environment. If an image is provided, it will be used
            when creating
    Return:
        Returning a list of coins (`list_coin`).
    """
    for fig in range(num_coun):
        fig = const_fi(randrange(0, WIDTH - coin_x), randrange(0, HEIGHT - coin_y),
                coin_x, coin_y, yellow, 0, 12, image)
        list_coin.append(fig)
    
    return list_coin


def ended_game():
    """
    Quits the Pygame module and exits the program when the user
    closes the window.
    """
    pygame.quit() # Esta es la inversa de pygame.init aca avisamos que vamos a salir del programa
    sys.exit() # Al momento de dar x a la pantalla va a salir sin mostrar error


def wait_player():
    """
    Uses a while loop to continuously check for player input events in
    Pygame, such as quitting the game or pressing a key, and calls the `ended_game` function
    accordingly.
    Return:
        In the `wait_player()` function, the return statement is used to exit the function when a
        KEYDOWN event is detected. However, there seems to be a mistake in the code where `e.type ==
        K_ESCAPE` should be `e.key == K_ESCAPE` to properly check for the Escape key press.
    """
    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                ended_game()
            
            if e.type == KEYDOWN:
                if e.type == K_ESCAPE:
                    ended_game()
                return


def advisor_text(surfice, tex, font, coordenates, color_font, color_back= None):
    """
    Renders text on a surface with specified font, coordinates, and colors.
    Args:
        param surfice (Surface):
            This is where the text will be displayed
        param tex (str):
            Is the text that you want to render on the surface. It is the actual
            content of the text that will be displayed
        param font:
            Is used to specify the font style and size for rendering the text. It is the font
            object that will be used to render the text onto the
            surface
        param coordenates (tuple):
            Is used to specify the coordinates where the text will be centered on the surface.
            It is a tuple containing the x and y coordinates.
            (e.g., (x, y)) where the text will be positioned
        param color_font (tuple):
            Is used to specify the color of the text that will be rendered on the surface.
            It should be a tuple representing the RGB values of the color, for example, (255, 0, 0)
            for red
        param color_back (tuple):
            Is used to specify the background color of the text being rendered. If a background color
            is provided, it will be used; otherwise, the text will have a transparent background
    """
    sup_text = font.render(tex, True, color_font, color_back)
    rect_tex = sup_text.get_rect()
    rect_tex.center = coordenates
    surfice.blit(sup_text, rect_tex)


def menu_init() -> (None):
    """
    The function `menu_ini` displays menu elements on the screen, plays background music, and waits for
    player input.
    """
    display.fill(deep_blue)
    display.blit(title_menu, (170, 200))
    display.blit(info_menu, (170, 260))
    display.blit(top_menu, (170, 320))
    display.blit(levels_menu, (170, 380))
    display.blit(play_menu, (170, 440))
    display.blit(logo_menu, (170, (HEIGHT - 220)))
    pygame.display.flip()
        # Music
    pygame.mixer.music.load("./src/sounds/starting_game.mp3") # Fondo de juego
    pygame.mixer.music.play(-1, 2000)
    pygame.mixer.music.set_volume(0.2)
    wait_player()
    pygame.mixer.music.unload()


def created_btn():
    
    pass




