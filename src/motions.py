from moviepy.editor import VideoFileClip
from images import *
from pygame.locals import *
from settings import *
import time
from constructor import *

def motion_background(surface, list_images: list, bg_width: int, scroll_x: int, speed: int):
    """
    This function is responsible for creating a scrolling motion background using a list of images on a
    given surface with specified parameters.
    Args:
        param surface (Surface):
            Represents the surface or window where the images will be drawn or blitted. It is typically a
            pygame Surface object where you want to display the moving background.
        param list_images (list):
            Is a list containing images that will be displayed on the surface. Each image in the list will
            be scrolled horizontally based on the scroll_x and speed parameters to create a motion background effect.
        param bg_width (int):
            Represents the width of the background images that are being scrolled horizontally on the surface.
            It is used to calculate the position of the images based on the scrolling behavior defined in the function
        param scroll_x:
            Represents the current scroll position along the x-axis. This value is used to determine how much the
            background images should be shifted horizontally to create a scrolling effect. By adjusting the `scroll_x`
            value, you can control the movement of the
        param speed:
            Represents the speed at which the background images will scroll horizontally across the surface. Increasing
            the speed value will make the background scroll faster, while decreasing it will slow down the scrolling effect
    """
    for x in range(5):
        for i, img in enumerate(list_images):
            position_x = (x * bg_width) - (scroll_x * (speed + i * 0.2))
            surface.blit(img, (position_x, 0))
    
    for i, img in enumerate(list_images):
        position_x = ((5 * bg_width) - (scroll_x * (speed + i * 0.2)))
        surface.blit(img, (position_x, 0))



def mov_list_images(list_images: list, surface, delay_img=0.08) -> (None):
    """
    The function displays a list of images on a surface with a specified delay between
    each image.
    
    Args:
        param list_images (list):
            is a list containing images that you want to display on the `surface`. Each image in the 
            list will be displayed one after the other on the surface
        param surface (Surface): Function is typically a pygame Surface object where the images from the 
            `list_images` will be displayed. This is where the images will be blitted onto during the
            animation
        param delay_img:
            Is the time delay in seconds between displaying each image from the `list_images` on the `surface`.
            It is set to a default value of 0.08 seconds if not specified when calling the function
    """
    for image in list_images:
        surface.blit(image, (0,0))
        pygame.display.flip()
        time.sleep(delay_img)


def video_play(path_video: str) -> (None):
    """
    The function `video_play` plays a video file located at the specified path and displays it on the
    screen using Pygame.
    
    Args:
        param path_video (str):
            The `path_video` parameter is a string that represents the file path to the video
            that you want to play. This function seems to be attempting to play a video using the
            `VideoFileClip` class from a library like MoviePy and display it using Pygame
    """
    
    video = VideoFileClip(path_video)
    video_ok = video.resize(size_display)
    video_ok.preview()
    
    video_ok.close()

