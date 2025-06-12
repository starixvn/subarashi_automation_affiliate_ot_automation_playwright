class ExampleBlockElements:
    
    # Block container
    div_block_example = "//div[@class='block block-example']"
    div_page_container = "//div[@class='block block-example']/div[@class='page-container']"
    div_group_page = "//div[@class='block block-example']/div[@class='page-container']/div[@class='group-page']"
    
    # Block title
    div_block_child_title = "//div[@class='block block-example']//div[@class='block-child-title title-spcing']"
    
    # Description paragraphs
    div_description_first = "//div[@class='block block-example']//div[@class='description'][1]"
    div_description_second = "//div[@class='block block-example']//div[@class='description'][2]"
    div_description_third = "//div[@class='block block-example']//div[@class='description'][3]"
    div_description_fourth = "//div[@class='block block-example']//div[@class='description'][4]"
    
    # Red-bold spans within descriptions
    span_red_bold_first = "//div[@class='block block-example']//div[@class='description'][1]/span[@class='red-bold'][1]"
    span_red_bold_second = "//div[@class='block block-example']//div[@class='description'][1]/span[@class='red-bold'][2]"
    span_red_bold_third = "//div[@class='block block-example']//div[@class='description'][1]/span[@class='red-bold'][3]"