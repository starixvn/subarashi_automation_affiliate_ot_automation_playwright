class CommissionProcessElements:
    
    # Section container
    div_block_process = "//div[@class='block block-process']"
    div_page_container = "//div[@class='block block-process']/div[@class='page-container']"
    div_group_page = "//div[@class='block block-process']/div[@class='page-container']/div[@class='group-page']"
    
    # Process main container
    div_main_process = "//div[@class='block block-process']//div[@class='main-process']"
    
    # Process items
    div_items = "//div[@class='block block-process']//div[@class='main-process']/div[@class='items']"
    div_mask = "//div[@class='block block-process']//div[@class='main-process']/div[@class='items']/div[@class='mask']"
    
    # First process item - Customer win/loss
    div_customer_winloss = "//div[@class='block block-process']//div[@class='main-process']/div[@class='items'][1]"
    div_customer_icon = "//div[@class='block block-process']//div[@class='main-process']/div[@class='items'][1]//div[@class='icon']"
    img_customer_icon = "//div[@class='block block-process']//div[@class='main-process']/div[@class='items'][1]//div[@class='icon']/img"
    div_customer_heading = "//div[@class='block block-process']//div[@class='main-process']/div[@class='items'][1]//div[@class='heading']"
    
    # Second process item - Platform Fee
    div_platform_fee = "//div[@class='block block-process']//div[@class='main-process']/div[@class='items'][2]"
    div_platform_icon = "//div[@class='block block-process']//div[@class='main-process']/div[@class='items'][2]//div[@class='icon']"
    img_platform_icon = "//div[@class='block block-process']//div[@class='main-process']/div[@class='items'][2]//div[@class='icon']/img"
    div_platform_heading = "//div[@class='block block-process']//div[@class='main-process']/div[@class='items'][2]//div[@class='heading']"
    
    # Third process item - Banking Fee
    div_banking_fee = "//div[@class='block block-process']//div[@class='main-process']/div[@class='items'][3]"
    div_banking_icon = "//div[@class='block block-process']//div[@class='main-process']/div[@class='items'][3]//div[@class='icon']"
    img_banking_icon = "//div[@class='block block-process']//div[@class='main-process']/div[@class='items'][3]//div[@class='icon']/img"
    div_banking_heading = "//div[@class='block block-process']//div[@class='main-process']/div[@class='items'][3]//div[@class='heading']"
    
    # Fourth process item - Bonus
    div_bonus = "//div[@class='block block-process']//div[@class='main-process']/div[@class='items'][4]"
    div_bonus_icon = "//div[@class='block block-process']//div[@class='main-process']/div[@class='items'][4]//div[@class='icon']"
    img_bonus_icon = "//div[@class='block block-process']//div[@class='main-process']/div[@class='items'][4]//div[@class='icon']/img"
    div_bonus_heading = "//div[@class='block block-process']//div[@class='main-process']/div[@class='items'][4]//div[@class='heading']"
    
    # Fifth process item - Net Profit
    div_net_profit = "//div[@class='block block-process']//div[@class='main-process']/div[@class='items'][5]"
    div_net_profit_icon = "//div[@class='block block-process']//div[@class='main-process']/div[@class='items'][5]//div[@class='icon']"
    img_net_profit_icon = "//div[@class='block block-process']//div[@class='main-process']/div[@class='items'][5]//div[@class='icon']/img"
    div_net_profit_heading = "//div[@class='block block-process']//div[@class='main-process']/div[@class='items'][5]//div[@class='heading']"
    
    # Arrow elements
    span_process_arrow_1 = "//div[@class='block block-process']//span[@class='process-arrow arrow-1']"
    span_process_arrow_2 = "//div[@class='block block-process']//span[@class='process-arrow arrow-2']"
    span_process_arrow_3 = "//div[@class='block block-process']//span[@class='process-arrow arrow-3']"
    span_process_arrow_4 = "//div[@class='block block-process']//span[@class='process-arrow arrow-4']"
    
    # Bottom text
    div_bottom_text = "//div[@class='block block-process']//div[@class='bottom-text']"