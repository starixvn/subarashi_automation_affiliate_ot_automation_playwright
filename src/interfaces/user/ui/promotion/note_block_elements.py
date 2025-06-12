class NoteBlockElements:
    
    # Block container
    div_block_note = "//div[@class='block block-note']"
    div_page_container = "//div[@class='block block-note']/div[@class='page-container']"
    div_group_page = "//div[@class='block block-note']/div[@class='page-container']/div[@class='group-page']"
    
    # Block title
    div_block_child_title = "//div[@class='block block-note']//div[@class='block-child-title title-spcing']"
    
    # Content container
    div_main_content = "//div[@class='block block-note']//div[@class='main-content']"
    div_items = "//div[@class='block block-note']//div[@class='main-content']/div[@class='items']"
    div_items_description = "//div[@class='block block-note']//div[@class='main-content']/div[@class='items']/div[@class='items-description']" 