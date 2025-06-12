class PlayerDetailTableElements:
    
    # Table container
    div_table = "//div[@class='table player-detail-table']"
    
    # Table element
    table_player_detail = "//table[@id='player-detail-table']"
    
    # Table head section
    thead = "//table[@id='player-detail-table']/thead"
    tr_header = "//table[@id='player-detail-table']/thead/tr[@class='player-detail-table-header']"
    
    # Header columns
    th_no = "//table[@id='player-detail-table']/thead/tr/th[1]" # No. column
    th_username = "//table[@id='player-detail-table']/thead/tr/th[@data-name='Username']" # Username column
    th_registered_date = "//table[@id='player-detail-table']/thead/tr/th[@data-name='RegisteredDate']" # Registered Date column
    th_fdm_date = "//table[@id='player-detail-table']/thead/tr/th[@data-name='FdmDate']" # FDM Date column
    th_fdm_amt = "//table[@id='player-detail-table']/thead/tr/th[@data-name='FdmAmt']" # FDM Amt column
    th_turnover = "//table[@id='player-detail-table']/thead/tr/th[@data-name='Turnover']" # Turnover column
    th_ggr = "//table[@id='player-detail-table']/thead/tr/th[@data-name='GGR']" # GGR column
    th_deposit = "//table[@id='player-detail-table']/thead/tr/th[@data-name='Deposit']" # Deposited column
    th_withdrawal = "//table[@id='player-detail-table']/thead/tr/th[@data-name='Withdrawal']" # Withdrawal column
    th_bonus = "//table[@id='player-detail-table']/thead/tr/th[@data-name='Bonus']" # Bonus column
    th_rebate = "//table[@id='player-detail-table']/thead/tr/th[@data-name='Rebate']" # Rebate column
    th_deposit_fee = "//table[@id='player-detail-table']/thead/tr/th[@data-name='DepositFee']" # Deposit Fee column
    th_withdrawal_fee = "//table[@id='player-detail-table']/thead/tr/th[@data-name='WithdrawalFee']" # Withdrawal Fee column
    
    # Column widths
    width_no = "5%"
    width_data_columns = "9%"
    
    # Column header components
    div_th_wrapper = "//table[@id='player-detail-table']/thead/tr/th/div[@class='th-wrapper']"
    span_column_title = "//table[@id='player-detail-table']/thead/tr/th/div[@class='th-wrapper']/span"
    div_icon_container = "//table[@id='player-detail-table']/thead/tr/th/div[@class='th-wrapper']/div[@class='icon-container']"
    span_caret_asc = "//table[@id='player-detail-table']/thead/tr/th/div[@class='th-wrapper']/div[@class='icon-container']/span[@class='caret asc']"
    span_caret_desc = "//table[@id='player-detail-table']/thead/tr/th/div[@class='th-wrapper']/div[@class='icon-container']/span[@class='caret desc']"
    span_default_sorting = "//table[@id='player-detail-table']/thead/tr/th/div[@class='th-wrapper']/div[@class='icon-container']/span[@id='defaultSorting']"
    span_current_sort = "//table[@id='player-detail-table']/thead/tr/th/div[@class='th-wrapper']/div[@class='icon-container']/span[@class='caret desc current']"
    
    # Table body section
    tbody = "//table[@id='player-detail-table']/tbody[@id='player-detail-content']"
    tr_no_info = "//table[@id='player-detail-table']/tbody/tr[td[contains(text(), 'No information is available')]]"
    td_no_info = "//table[@id='player-detail-table']/tbody/tr/td[@class='text-center'][contains(text(), 'No information is available')]"
    
    # Hidden inputs
    input_has_scroll = "//input[@id='HasScroll']"
    input_total_item = "//input[@id='TotalItem']"