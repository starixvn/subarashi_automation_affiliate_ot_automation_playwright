class DetailsSectionElements:
    
    # Details section container
    div_details_section_content = "//div[@class='details-section-content'][@id='details-section-content']"
    
    # Table container
    div_table = "//div[@class='details-section-content']/div[@class='table player-detail-table']"
    
    # Table element
    table_player_detail = "//div[@class='details-section-content']//table[@id='player-detail-table']"
    
    # Table head section
    thead = "//div[@class='details-section-content']//table[@id='player-detail-table']/thead"
    tr_header = "//div[@class='details-section-content']//table[@id='player-detail-table']/thead/tr[@class='player-detail-table-header']"
    
    # Header columns
    th_no = "//div[@class='details-section-content']//table/thead/tr/th[1]" # No. column
    th_username = "//div[@class='details-section-content']//table/thead/tr/th[2][@data-name='Username']" # Username column
    th_registered_date = "//div[@class='details-section-content']//table/thead/tr/th[3][@data-name='RegisteredDate']" # Registered Date column
    th_fdm_date = "//div[@class='details-section-content']//table/thead/tr/th[4][@data-name='FdmDate']" # FDM Date column
    th_fdm_amt = "//div[@class='details-section-content']//table/thead/tr/th[5][@data-name='FdmAmt']" # FDM Amt column
    th_turnover = "//div[@class='details-section-content']//table/thead/tr/th[6][@data-name='Turnover']" # Turnover column
    th_ggr = "//div[@class='details-section-content']//table/thead/tr/th[7][@data-name='GGR']" # GGR column
    th_deposit = "//div[@class='details-section-content']//table/thead/tr/th[8][@data-name='Deposit']" # Deposited column
    th_withdrawal = "//div[@class='details-section-content']//table/thead/tr/th[9][@data-name='Withdrawal']" # Withdrawal column
    th_bonus = "//div[@class='details-section-content']//table/thead/tr/th[10][@data-name='Bonus']" # Bonus column
    th_rebate = "//div[@class='details-section-content']//table/thead/tr/th[11][@data-name='Rebate']" # Rebate column
    th_deposit_fee = "//div[@class='details-section-content']//table/thead/tr/th[12][@data-name='DepositFee']" # Deposit Fee column
    th_withdrawal_fee = "//div[@class='details-section-content']//table/thead/tr/th[13][@data-name='WithdrawalFee']" # Withdrawal Fee column
    
    # Sorting elements in column headers
    div_th_wrapper = "//div[@class='details-section-content']//table/thead/tr/th/div[@class='th-wrapper']"
    span_column_title = "//div[@class='details-section-content']//table/thead/tr/th/div[@class='th-wrapper']/span"
    div_icon_container = "//div[@class='details-section-content']//table/thead/tr/th/div[@class='th-wrapper']/div[@class='icon-container']"
    span_caret_asc = "//div[@class='details-section-content']//table/thead/tr/th/div[@class='th-wrapper']/div[@class='icon-container']/span[@class='caret asc']"
    span_caret_desc = "//div[@class='details-section-content']//table/thead/tr/th/div[@class='th-wrapper']/div[@class='icon-container']/span[@class='caret desc']"
    span_default_sorting = "//div[@class='details-section-content']//table/thead/tr/th/div[@class='th-wrapper']/div[@class='icon-container']/span[@id='defaultSorting']"
    span_current_sort = "//div[@class='details-section-content']//table/thead/tr/th/div[@class='th-wrapper']/div[@class='icon-container']/span[@class='caret desc current']"
    
    # Table body section
    tbody = "//div[@class='details-section-content']//table[@id='player-detail-table']/tbody[@id='player-detail-content']"
    tr_no_info = "//div[@class='details-section-content']//table/tbody/tr[td[contains(text(), 'No information is available')]]"
    td_no_info = "//div[@class='details-section-content']//table/tbody/tr/td[@class='text-center'][contains(text(), 'No information is available')]"
    
    # Hidden inputs
    input_has_scroll = "//div[@class='details-section-content']//input[@id='HasScroll']"
    input_total_item = "//div[@class='details-section-content']//input[@id='TotalItem']"
    