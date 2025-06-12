class RevenueReportTableElements:

    # Report container
    div_report_container = "//div[@class='report-container']"
    div_table_commission_report = "//div[@class='table commission-report overview-table']"
    table_data = "//table[@id='dataTable']"
    
    # Table header
    thead = "//table[@id='dataTable']/thead"
    tr_header = "//table[@id='dataTable']/thead/tr"
    
    # Header columns
    th_number = "//table[@id='dataTable']/thead/tr/th[1]"
    th_month = "//table[@id='dataTable']/thead/tr/th[2]"
    th_turnover = "//table[@id='dataTable']/thead/tr/th[3]"
    th_ggr = "//table[@id='dataTable']/thead/tr/th[4]"
    th_royalty_fee = "//table[@id='dataTable']/thead/tr/th[5]"
    th_deposit_fee = "//table[@id='dataTable']/thead/tr/th[6]"
    th_withdrawal_fee = "//table[@id='dataTable']/thead/tr/th[7]"
    th_bonus = "//table[@id='dataTable']/thead/tr/th[8]"
    th_rebate = "//table[@id='dataTable']/thead/tr/th[9]"
    th_revenue_rate = "//table[@id='dataTable']/thead/tr/th[10]"
    th_revenue_share = "//table[@id='dataTable']/thead/tr/th[11]"
    th_earning_by = "//table[@id='dataTable']/thead/tr/th[12]"
    th_total_revenue_share = "//table[@id='dataTable']/thead/tr/th[13]"
    
    # Table body
    tbody = "//table[@id='dataTable']/tbody[@id='reportData']"
    
    # Month summary rows (sumrow)
    tr_sumrow = "//table[@id='dataTable']/tbody[@id='reportData']/tr[contains(@class, 'sumrow')]"
    
    # Detail rows
    tr_detail = "//table[@id='dataTable']/tbody[@id='reportData']/tr[not(contains(@class, 'sumrow')) and not(contains(@class, 'total'))]"
    
    # Total row
    tr_total = "//table[@id='dataTable']/tbody[@id='reportData']/tr[@class='total']"
    
    # Sort indicators
    span_default_sorting = "//span[@id='defaultSorting']"
    span_caret_asc = "//div[@class='icon-container']/span[@class='caret asc']"
    span_caret_desc = "//div[@class='icon-container']/span[@class='caret desc']"
    
    # Expand/collapse indicators
    span_chevron_bottom = "//span[@class='chevron toggleDetailRow bottom']"
    span_chevron_left = "//span[@class='chevron toggleDetailRow left']"
    
    # JavaScript resources
    script_lang_resource = "//script[contains(text(), 'langResource')]"
    script_commission_report = "//script[contains(@src, 'commission-report.js')]"