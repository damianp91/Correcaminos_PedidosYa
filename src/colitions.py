

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