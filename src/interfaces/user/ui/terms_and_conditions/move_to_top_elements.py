class MoveToTopElements:
    
    # Container
    div_moving_block = "//div[@class='moving-block']"
    
    # Button and SVG components
    btn_move_top = "//button[@type='button'][@aria-label='Move To Top'][@class='btn btn-move-top'][@id='moveToTop']"
    svg_icon = "//button[@id='moveToTop']/svg"
    g_clip_path = "//button[@id='moveToTop']/svg/g[@clip-path='url(#clip0_1_338)']"
    path_arrow = "//button[@id='moveToTop']/svg/g/path"
    defs = "//button[@id='moveToTop']/svg/defs"
    clip_path = "//button[@id='moveToTop']/svg/defs/clipPath[@id='clip0_1_338']"
    rect = "//button[@id='moveToTop']/svg/defs/clipPath/rect" 