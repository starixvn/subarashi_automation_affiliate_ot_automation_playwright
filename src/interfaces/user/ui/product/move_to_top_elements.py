"""
Move To Top Elements

This file contains XPath locators for the move to top button elements.
"""

class MoveToTopElements:
    """
    Class containing XPath locators for the move to top button elements.
    """
    
    # Container
    div_moving_block = "//div[@class='moving-block']"
    
    # Button
    btn_move_top = "//button[@class='btn btn-move-top'][@id='moveToTop']"
    
    # Icon
    svg_icon = "//button[@class='btn btn-move-top'][@id='moveToTop']/svg"
    
    # SVG components
    g_clip_path = "//button[@class='btn btn-move-top'][@id='moveToTop']/svg/g"
    path_arrow = "//button[@class='btn btn-move-top'][@id='moveToTop']/svg/g/path"
    defs = "//button[@class='btn btn-move-top'][@id='moveToTop']/svg/defs"
    clip_path = "//button[@class='btn btn-move-top'][@id='moveToTop']/svg/defs/clipPath"
    rect = "//button[@class='btn btn-move-top'][@id='moveToTop']/svg/defs/clipPath/rect" 