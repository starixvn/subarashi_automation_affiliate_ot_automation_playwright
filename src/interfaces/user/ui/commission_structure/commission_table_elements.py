class CommissionTableElements:
    
    # Section container
    div_block_commission = "//div[@class='block block-commission']"
    div_page_container = "//div[@class='block block-commission']/div[@class='page-container']"
    
    # Table heading
    div_heading_table = "//div[@class='block block-commission']//div[@class='heading-table']"
    
    # Table container
    div_table_custom = "//div[@class='block block-commission']//div[@class='table-custom table-responsive']"
    table = "//div[@class='block block-commission']//div[@class='table-custom table-responsive']/table"
    
    # Table header
    thead = "//div[@class='block block-commission']//table/thead"
    tr_header = "//div[@class='block block-commission']//table/thead/tr"
    th_revenue_share = "//div[@class='block block-commission']//table/thead/tr/th[1]"
    th_tier = "//div[@class='block block-commission']//table/thead/tr/th[2]"
    th_company_net_win = "//div[@class='block block-commission']//table/thead/tr/th[3]"
    th_qualifying_members = "//div[@class='block block-commission']//table/thead/tr/th[4]"
    th_commission = "//div[@class='block block-commission']//table/thead/tr/th[5]"
    
    # Table body
    tbody = "//div[@class='block block-commission']//table/tbody"
    
    # First row with products
    tr_products = "//div[@class='block block-commission']//table/tbody/tr[1]"
    td_all_products = "//div[@class='block block-commission']//table/tbody/tr[1]/td[1]"
    p_all_products = "//div[@class='block block-commission']//table/tbody/tr[1]/td[1]/p[@class='all-products']"
    p_more_detail = "//div[@class='block block-commission']//table/tbody/tr[1]/td[1]/p/a[@class='more-detail']"
    
    # Tier rows
    tr_tier_1 = "//div[@class='block block-commission']//table/tbody/tr[1]"
    tr_tier_2 = "//div[@class='block block-commission']//table/tbody/tr[2]"
    tr_tier_3 = "//div[@class='block block-commission']//table/tbody/tr[3]"
    tr_tier_4 = "//div[@class='block block-commission']//table/tbody/tr[4]"
    tr_tier_5 = "//div[@class='block block-commission']//table/tbody/tr[5]"
    tr_tier_6 = "//div[@class='block block-commission']//table/tbody/tr[6]"