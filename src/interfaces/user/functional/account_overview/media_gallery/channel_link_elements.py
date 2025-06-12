class ChannelLinkElements:
    
    # Main container elements
    div_link_statistic = "//div[@id='linkStatistic']"
    div_channel_table = "//div[@id='linkStatistic']//div[@class='channel-table']"
    
    # Table elements
    table_channels = "//div[@id='linkStatistic']//table[@class='channels-table']"
    thead_channels = "//div[@id='linkStatistic']//table[@class='channels-table']/thead"
    tbody_channels = "//div[@id='linkStatistic']//table[@class='channels-table']/tbody"
    
    # Table header elements
    th_stt = "//div[@id='linkStatistic']//thead/tr/th[contains(@class, 'stt')]"
    th_channel = "//div[@id='linkStatistic']//thead/tr/th[contains(@class, 'channel')]"
    th_number_of_link = "//div[@id='linkStatistic']//thead/tr/th[contains(@class, 'number-of-link')]"
    th_lang = "//div[@id='linkStatistic']//thead/tr/th[contains(@class, 'lang')]"
    th_action = "//div[@id='linkStatistic']//thead/tr/th[contains(@class, 'action')]"
    
    # Table row elements
    tr_channel = "//div[@id='linkStatistic']//tbody/tr[contains(@class, 'parent-row')]"
    
    # Channel details elements
    td_stt = "//div[@id='linkStatistic']//tbody/tr[contains(@class, 'parent-row')]/td[contains(@class, 'stt')]"
    td_channel = "//div[@id='linkStatistic']//tbody/tr[contains(@class, 'parent-row')]/td[contains(@class, 'channel')]"
    td_number_of_link = "//div[@id='linkStatistic']//tbody/tr[contains(@class, 'parent-row')]/td[contains(@class, 'number-of-link')]"
    td_lang = "//div[@id='linkStatistic']//tbody/tr[contains(@class, 'parent-row')]/td[contains(@class, 'lang')]"
    td_action = "//div[@id='linkStatistic']//tbody/tr[contains(@class, 'parent-row')]/td[contains(@class, 'action')]"
    
    # Channel action buttons
    button_expand = "//div[@id='linkStatistic']//tbody/tr[contains(@class, 'parent-row')]/td[contains(@class, 'action')]//button[contains(@class, 'btn-expand')]"
    
    # Child link elements
    tr_child_link = "//div[@id='linkStatistic']//tbody/tr[contains(@class, 'child-row')]"
    div_child_content = "//div[@id='linkStatistic']//tbody/tr[contains(@class, 'child-row')]/td/div[contains(@class, 'child-content')]"
    div_link_item = "//div[@id='linkStatistic']//div[contains(@class, 'link-item')]"
    
    # Link details elements
    div_link_main = "//div[@id='linkStatistic']//div[contains(@class, 'link-main')]"
    div_link_url = "//div[@id='linkStatistic']//div[contains(@class, 'link-url')]"
    input_link_url = "//div[@id='linkStatistic']//input[contains(@class, 'url-input')]"
    button_copy_url = "//div[@id='linkStatistic']//button[contains(@class, 'btn-copy-url')]"
    
    # Link info elements
    div_link_info = "//div[@id='linkStatistic']//div[contains(@class, 'link-info')]"
    span_link_id = "//div[@id='linkStatistic']//span[contains(@class, 'link-id')]"
    span_link_market = "//div[@id='linkStatistic']//span[contains(@class, 'link-market')]"
    span_link_clicks = "//div[@id='linkStatistic']//span[contains(@class, 'link-clicks')]"
    