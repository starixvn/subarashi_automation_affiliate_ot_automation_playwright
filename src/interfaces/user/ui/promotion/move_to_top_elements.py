"""
Move To Top Elements

This file contains XPath locators for move to top button elements on the Affiliate page.
"""

class MoveToTopElements:
    """
    Class containing XPath locators for move to top button elements.
    """
    
    # Container
    div_moving_block = "//div[@class='moving-block']"
    
    # Button with onclick event
    btn_move_top = "//button[@type='button'][@aria-label='Move To Top'][@class='btn btn-move-top'][@id='moveToTop']"
    btn_move_top_hidden = "//button[@type='button'][@aria-label='Move To Top'][@class='btn btn-move-top'][@id='moveToTop'][@style='display: none;']"
    
    # SVG components
    svg_icon = "//button[@id='moveToTop']/svg[@width='32'][@height='32'][@viewBox='0 0 32 32'][@fill='none']"
    g_clip_path = "//button[@id='moveToTop']/svg/g[@clip-path='url(#clip0_7756_22538)']"
    path_arrow = "//button[@id='moveToTop']/svg/g/path[@d='M6.66602 12.0003L8.54602 13.8803L14.666 7.77366V29.3337H17.3327V7.77366L23.4527 13.8937L25.3327 12.0003L15.9993 2.66699L6.66602 12.0003Z'][@fill='white']"
    
    # Defs and clipPath
    defs = "//button[@id='moveToTop']/svg/defs"
    clip_path = "//button[@id='moveToTop']/svg/defs/clipPath[@id='clip0_7756_22538']"
    rect = "//button[@id='moveToTop']/svg/defs/clipPath/rect[@width='32'][@height='32'][@fill='white']" 