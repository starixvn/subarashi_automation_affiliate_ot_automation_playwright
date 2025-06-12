class PowerBlockElements:
    
    # Block container
    div_block_power = "//div[@class='block block-power']"
    div_page_container = "//div[@class='block block-power']/div[@class='page-container']"
    div_group_page = "//div[@class='block block-power']/div[@class='page-container']/div[@class='group-page']"
    
    # Block title and description
    div_block_child_title = "//div[@class='block block-power']//div[@class='block-child-title']"
    div_block_child_description = "//div[@class='block block-power']//div[@class='block-child-description']"
    
    # Table elements
    div_table_custom = "//div[@class='block block-power']//div[@class='table-custom table-responsive']"
    table = "//div[@class='block block-power']//div[@class='table-custom table-responsive']/table"
    thead = "//div[@class='block block-power']//div[@class='table-custom table-responsive']/table/thead"
    tbody = "//div[@class='block block-power']//div[@class='table-custom table-responsive']/table/tbody"
    
    # Table header cells
    th_fdm = "//div[@class='block block-power']//table/thead/tr/th[1]"
    th_deposit = "//div[@class='block block-power']//table/thead/tr/th[2]"
    th_commission = "//div[@class='block block-power']//table/thead/tr/th[3]"
    th_max_commission = "//div[@class='block block-power']//table/thead/tr/th[4]"
    
    # Table rows
    tr_first = "//div[@class='block block-power']//table/tbody/tr[1]"
    tr_second = "//div[@class='block block-power']//table/tbody/tr[2]"
    tr_third = "//div[@class='block block-power']//table/tbody/tr[3]"
    tr_fourth = "//div[@class='block block-power']//table/tbody/tr[4]"