class MoveToTopElements:
    
    # Moving block container
    div_moving_block = "//div[@class='moving-block']"
    
    # Move to top button
    btn_move_top = "//div[@class='moving-block']/button[@class='btn btn-move-top'][@id='moveToTop']"
    
    # SVG icon
    svg_icon = "//div[@class='moving-block']/button[@class='btn btn-move-top']/svg"
    g_clip_path = "//div[@class='moving-block']/button[@class='btn btn-move-top']/svg/g"
    path_arrow = "//div[@class='moving-block']/button[@class='btn btn-move-top']/svg/g/path"
    
    # Defs and clipPath
    defs_element = "//div[@class='moving-block']/button[@class='btn btn-move-top']/svg/defs"
    clip_path_element = "//div[@class='moving-block']/button[@class='btn btn-move-top']/svg/defs/clipPath"
    rect_element = "//div[@class='moving-block']/button[@class='btn btn-move-top']/svg/defs/clipPath/rect" 