

def point_in_block(point : tuple, figure) -> (bool):
    """_summary_
    Args:
        point (tuple, figure): _description_
    Returns:
        _type_: _description_
    """
    x, y = point
    
    return x <= figure.right and x >= figure.left and y >= figure.top and y <= figure.bottom


def detected_colition(block_1, block_2) -> (bool):
    """_summary_
    Args:
        block_1 (_type_): _description_
    Returns:
        _type_: _description_
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
    """_summary_
    Args:
        figure (_type_): _description_
    Returns:
        _type_: _description_
    """
    return figure.height // 2


def distance_between_points(point_1 : tuple, point_2 : tuple) -> (float):
    """_summary_
    Args:
        point_1 (_type_): _description_
    Returns:
        _type_: _description_
    """
    x1, y1 = point_1
    x2, y2 = point_2
    
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def detected_colition_circle(figure_1, figure_2) -> (bool):
    """_summary_
    Args:
        figure_1 (_type_): _description_
    Returns:
        _type_: _description_
    """
    colition = False
    
    r1 = cal_ratio(figure_1)
    r2 = cal_ratio(figure_2)
    
    distance = distance_between_points(figure_1.center, figure_2.center)
    
    if distance <= (r1 + r2):
        colition = True
    
    return colition