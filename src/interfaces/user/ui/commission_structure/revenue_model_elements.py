class RevenueModelElements:
    
    # Section container
    div_block_revenue = "//div[@class='block block-revenue']"
    div_page_container = "//div[@class='block block-revenue']/div[@class='page-container']"
    div_group_page = "//div[@class='block block-revenue']/div[@class='page-container']/div[@class='group-page']"
    
    # Title
    div_top_title = "//div[@class='block block-revenue']//div[@class='top-title']"
    
    # Description paragraphs
    div_description = "//div[@class='block block-revenue']//div[@class='description']"
    first_paragraph = "//div[@class='block block-revenue']//div[@class='description'][1]"
    second_paragraph = "//div[@class='block block-revenue']//div[@class='description'][2]"