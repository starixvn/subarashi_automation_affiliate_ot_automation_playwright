class DailyEarningElements:

    # Container elements
    div_daily_earning = "//div[.//ol[@id='dailyEarningBreadcrumb']]"
    div_breadcrumb_container = "//div[@class='breadcrumb-container']"
    ol_breadcrumb = "//ol[@id='dailyEarningBreadcrumb']"
    li_statement_history = "//ol[@id='dailyEarningBreadcrumb']/li"
    a_statement_history = "//ol[@id='dailyEarningBreadcrumb']/li/a"
    
    # Filter form elements
    div_form_filter = "//div[.//select[@id='ProductId']]/div[@class='form-inline form-filter']"
    
    # Product type filter
    div_form_group_product = "//div[.//select[@id='ProductId']]//div[@class='form-group']"
    label_product_id = "//label[@for='ProductId']"
    select_product_id = "//select[@id='ProductId']"
    option_all = "//select[@id='ProductId']/option[@value='0']"
    
    # Base currency filter (second occurrence)
    div_form_group_currency = "//div[.//select[@id='base-currency'] and .//label[@class='w120']]//div[@class='form-group']"
    label_base_currency = "//div[.//select[@id='base-currency'] and .//label[@class='w120']]//label[@for='base-currency']"
    select_base_currency = "//div[.//select[@id='base-currency'] and .//label[@class='w120']]//select[@id='base-currency']"
    
    # Daily earning table
    div_daily_earning_content = "//div[@id='dailyEarningContent']"
    div_table_responsive = "//div[@id='dailyEarningContent'][@class='table table-responsive']"
    table = "//div[@id='dailyEarningContent']//table"
    
    # Table header elements
    thead = "//div[@id='dailyEarningContent']//table/thead"
    tr_header = "//div[@id='dailyEarningContent']//table/thead/tr"
    th_number = "//div[@id='dailyEarningContent']//table/thead/tr/th[1]"
    th_date = "//div[@id='dailyEarningContent']//table/thead/tr/th[2]"
    th_deposited = "//div[@id='dailyEarningContent']//table/thead/tr/th[3]"
    th_turnover = "//div[@id='dailyEarningContent']//table/thead/tr/th[4]"
    th_ggr = "//div[@id='dailyEarningContent']//table/thead/tr/th[5]"
    th_bonus = "//div[@id='dailyEarningContent']//table/thead/tr/th[6]"
    th_rebate = "//div[@id='dailyEarningContent']//table/thead/tr/th[7]"
    
    # Table body elements
    tbody = "//div[@id='dailyEarningContent']//table/tbody"
    tr_row = "//div[@id='dailyEarningContent']//table/tbody/tr[not(contains(@class, 'total'))]"
    tr_total = "//div[@id='dailyEarningContent']//table/tbody/tr[@class='total']"
    
    # Total row cells
    td_total_label = "//div[@id='dailyEarningContent']//table/tbody/tr[@class='total']/td[1]"
    td_total_deposited = "//div[@id='dailyEarningContent']//table/tbody/tr[@class='total']/td[3]"
    td_total_turnover = "//div[@id='dailyEarningContent']//table/tbody/tr[@class='total']/td[4]"
    td_total_ggr = "//div[@id='dailyEarningContent']//table/tbody/tr[@class='total']/td[5]"
    td_total_bonus = "//div[@id='dailyEarningContent']//table/tbody/tr[@class='total']/td[6]"
    td_total_rebate = "//div[@id='dailyEarningContent']//table/tbody/tr[@class='total']/td[7]"