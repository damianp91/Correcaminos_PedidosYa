

def point_in_block(point : tuple, figure) -> (bool):
    """
    The function `point_in_block` checks if a given point lies within a specified block figure.
    Args:
        param point (tuple):
            A tuple representing the coordinates of a point in a 2D plane
        param figure (Rect):
            A rect that will be detect with points of coordinate tuple 'point'.
    Returns:
        a boolean value indicating whether the given point is inside the specified figure block.
    """
    x, y = point
    
    return x <= figure.right and x >= figure.left and y >= figure.top and y <= figure.bottom


def detected_colition(block_1, block_2) -> (bool):
    """
    The function `detected_colition` checks for collision between two blocks by verifying if any of the
    corners of one block are inside the other block.
    Args:
        param block_1 (Rect):
            Rect with coordinates points for detected
            
        param block_2 (Rect):
            Rect with coordinates points for detected
        Return: 
            Returning a boolean value indicating whether a
            collision has been detected between two blocks (`block_1` and `block_2`). If a collision is
            detected, it returns `True`; otherwise, it returns `False`.
    """
    colition = False
    
    for r1, r2 in [(block_1, block_2), (block_2, block_1)]:
        if point_in_block(r1.topleft, r2) or \
            point_in_block(r1.topright, r2) or \
            point_in_block(r1.bottomleft, r2) or \
            point_in_block(r1.bottomright, r2):
                colition = True
    
    return colition


def cal_ratio(figure) -> (int):
    """
    The function `cal_ratio` calculates the ratio of the height of a figure to 2.
    Args:
        param figure (Rect):
            Structure that has a `height` attribute. The function then calculates
            and returns half of the `height` attribute of the `figure` object
    Return:
        The function `cal_ratio` is returning half of the height of the input figure.
    """
    return figure.height // 2


def distance_between_points(point_1 : tuple, point_2 : tuple) -> (float):
    """
    The function calculates the Euclidean distance between two points in a 2D plane.
    Args:
        param point_1 (tuple):
            The `point_1` parameter is a tuple representing the coordinates of the first point
            in a 2D plane. It should be in the format `(x1, y1)`, where `x1` and `y1` are the x and y
            coordinates of the first point respectively
        param point_2 (tuple):
            The `point_2` parameter is a tuple representing the coordinates of the second point
            in a two-dimensional space. It typically consists of two values: the x-coordinate and the
            y-coordinate of the point
    Return: 
        The formula: sqrt((x2 - x1)^2 + (y2 - y1)^2). The function returns the
        calculated distance as a float value.
    """
    x1, y1 = point_1
    x2, y2 = point_2
    
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def detected_colition_circle(figure_1, figure_2) -> (bool):
    """
    This Python function detects collision between two circles based on their radii and distances
    between their centers.
    Args:
        param figure_1 (Rect):
            Rect with coordinates points for detected
        param figure_2 (Rect):
            Rect with coordinates points for detected
    Return:
        Returning a boolean value indicating whether there is a collision between two circles
        represented by `figure_1` and `figure_2`. If there is a
        collision, it returns `True`, otherwise it returns `False`.
    """
    colition = False
    
    r1 = cal_ratio(figure_1)
    r2 = cal_ratio(figure_2)
    
    distance = distance_between_points(figure_1.center, figure_2.center)
    
    if distance <= (r1 + r2):
        colition = True
    
    return colition