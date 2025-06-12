class SummarySectionElements:
    
    # Summary section container
    div_summary_section = "//div[@id='summary-section']"
    
    # Referral stats container
    div_referral_stats = "//div[@id='summary-section']/div[@class='referral-stats']"
    
    # Referral stats items
    div_item_signups = "//div[@class='referral-stats']/div[@class='item'][1]"
    div_item_depositors = "//div[@class='referral-stats']/div[@class='item'][2]"
    div_item_revenue = "//div[@class='referral-stats']/div[@class='item'][3]"
    
    # Signups item elements
    p_signups_title = "//div[@class='referral-stats']/div[@class='item'][1]/p[@class='title']"
    p_signups_value = "//div[@class='referral-stats']/div[@class='item'][1]/p[@class='value']"
    p_signups_desc = "//div[@class='referral-stats']/div[@class='item'][1]/p[@class='desc']"
    
    # Depositors item elements
    p_depositors_title = "//div[@class='referral-stats']/div[@class='item'][2]/p[@class='title']"
    p_depositors_value = "//div[@class='referral-stats']/div[@class='item'][2]/p[@class='value']"
    p_depositors_desc = "//div[@class='referral-stats']/div[@class='item'][2]/p[@class='desc']"
    
    # Revenue item elements
    p_revenue_title = "//div[@class='referral-stats']/div[@class='item'][3]/p[@class='title']"
    p_revenue_value = "//div[@class='referral-stats']/div[@class='item'][3]/p[@class='value']"
    p_revenue_desc = "//div[@class='referral-stats']/div[@class='item'][3]/p[@class='desc']"
    
    # Account info container
    div_account_info = "//div[@id='summary-section']/div[@class='account-info']"
    
    # Account info items
    div_item_commission = "//div[@class='account-info']/div[@class='item'][1]"
    div_item_deposit = "//div[@class='account-info']/div[@class='item'][2]"
    div_item_turnover = "//div[@class='account-info']/div[@class='item'][3]"
    
    # Commission item elements
    p_commission_title = "//div[@class='account-info']/div[@class='item'][1]/p[@class='title']"
    p_commission_value = "//div[@class='account-info']/div[@class='item'][1]/p[@class='value']"
    p_commission_desc = "//div[@class='account-info']/div[@class='item'][1]/p[@class='desc']"
    
    # Deposit item elements
    p_deposit_title = "//div[@class='account-info']/div[@class='item'][2]/p[@class='title']"
    p_deposit_value = "//div[@class='account-info']/div[@class='item'][2]/p[@class='value']"
    p_deposit_desc = "//div[@class='account-info']/div[@class='item'][2]/p[@class='desc']"
    
    # Turnover item elements
    p_turnover_title = "//div[@class='account-info']/div[@class='item'][3]/p[@class='title']"
    p_turnover_value = "//div[@class='account-info']/div[@class='item'][3]/p[@class='value']"
    p_turnover_desc = "//div[@class='account-info']/div[@class='item'][3]/p[@class='desc']"
    
    # Daily stats container
    div_daily_stats = "//div[@id='summary-section']/div[@class='daily-stats']"
    h4_daily_stats_title = "//div[@class='daily-stats']/h4[@class='title']"
    
    # Daily stats table
    table_daily_stats = "//div[@class='daily-stats']/table[@class='table table-striped']"
    thead_daily_stats = "//div[@class='daily-stats']/table/thead"
    tr_header = "//div[@class='daily-stats']/table/thead/tr"
    
    # Table header cells
    th_date = "//div[@class='daily-stats']/table/thead/tr/th[1]"
    th_click = "//div[@class='daily-stats']/table/thead/tr/th[2]"
    th_signup = "//div[@class='daily-stats']/table/thead/tr/th[3]"
    th_depositor = "//div[@class='daily-stats']/table/thead/tr/th[4]"
    th_deposit = "//div[@class='daily-stats']/table/thead/tr/th[5]"
    th_turnover = "//div[@class='daily-stats']/table/thead/tr/th[6]"
    th_revenue = "//div[@class='daily-stats']/table/thead/tr/th[7]"
    th_net_revenue = "//div[@class='daily-stats']/table/thead/tr/th[8]"
    
    # Table body
    tbody_daily_stats = "//div[@class='daily-stats']/table/tbody"
    