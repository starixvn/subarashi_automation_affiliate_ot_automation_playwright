class StatisticsElements:
    # Main container
    div_customer_statistics = "//div[@class='customer-statistics']"
    div_app_container = "//div[@class='customer-statistics']/div[@class='app-container']"
    div_table_responsive = "//div[@class='customer-statistics']//div[@class='my-2 table-responsive']"
    
    # Statistics table
    tbl_statistics = "//table[@id='statistic-data-table']"
    
    # Table header
    thead_statistics = "//table[@id='statistic-data-table']/thead"
    tr_header = "//table[@id='statistic-data-table']/thead/tr"
    th_statistics = "//table[@id='statistic-data-table']/thead/tr/th[1]"
    th_month_picker = "//table[@id='statistic-data-table']/thead/tr/th[2]"
    th_up_to_now = "//table[@id='statistic-data-table']/thead/tr/th[3]"
    
    # Month picker
    div_month_picker_container = "//table[@id='statistic-data-table']/thead/tr/th[2]/div[@class='position-relative d-inline-block']"
    div_month_picker_main = "//table[@id='statistic-data-table']/thead/tr/th[2]//div[@class='rmp-main-container']"
    div_month_form = "//table[@id='statistic-data-table']/thead/tr/th[2]//div[@class='mp-form-container']"
    inp_month = "//table[@id='statistic-data-table']/thead/tr/th[2]//input[@class='mp-form-input']"
    spn_calendar_icon = "//table[@id='statistic-data-table']/thead/tr/th[2]//span[@class='oi oi-calendar icon-calendar ml-1']"
    
    # Month picker popup
    div_month_picker_popup = "//table[@id='statistic-data-table']/thead/tr/th[2]//div[@class='mp-container']"
    div_mp_header = "//table[@id='statistic-data-table']/thead/tr/th[2]//div[@class='mp-header']"
    sel_year = "//table[@id='statistic-data-table']/thead/tr/th[2]//select[@class='mp-select-year']"
    tbl_month = "//table[@id='statistic-data-table']/thead/tr/th[2]//table[@class='mp-month-table']"
    
    # Row selectors for months in picker
    tr_month_row1 = "//table[@id='statistic-data-table']/thead/tr/th[2]//table[@class='mp-month-table']/tbody/tr[1]"
    tr_month_row2 = "//table[@id='statistic-data-table']/thead/tr/th[2]//table[@class='mp-month-table']/tbody/tr[2]"
    tr_month_row3 = "//table[@id='statistic-data-table']/thead/tr/th[2]//table[@class='mp-month-table']/tbody/tr[3]"
    tr_month_row4 = "//table[@id='statistic-data-table']/thead/tr/th[2]//table[@class='mp-month-table']/tbody/tr[4]"
    
    # Loading spinner
    div_spinner = "//table[@id='statistic-data-table']/thead/tr/th[2]//div[@role='status']"
    
    # Table body
    tbody_statistics = "//table[@id='statistic-data-table']/tbody"
    
    # Statistics rows
    tr_new_signups = "//table[@id='statistic-data-table']/tbody/tr[1]"
    td_new_signups_label = "//table[@id='statistic-data-table']/tbody/tr[1]/td[1]"
    td_new_signups_month = "//table[@id='statistic-data-table']/tbody/tr[1]/td[2]"
    td_new_signups_total = "//table[@id='statistic-data-table']/tbody/tr[1]/td[3]"
    
    tr_active_players = "//table[@id='statistic-data-table']/tbody/tr[2]"
    td_active_players_label = "//table[@id='statistic-data-table']/tbody/tr[2]/td[1]"
    td_active_players_month = "//table[@id='statistic-data-table']/tbody/tr[2]/td[2]"
    td_active_players_total = "//table[@id='statistic-data-table']/tbody/tr[2]/td[3]"
    
    tr_qualified_players = "//table[@id='statistic-data-table']/tbody/tr[3]"
    td_qualified_players_label = "//table[@id='statistic-data-table']/tbody/tr[3]/td[1]"
    td_qualified_players_month = "//table[@id='statistic-data-table']/tbody/tr[3]/td[2]"
    td_qualified_players_total = "//table[@id='statistic-data-table']/tbody/tr[3]/td[3]"
    
    tr_sub_affiliates = "//table[@id='statistic-data-table']/tbody/tr[4]"
    td_sub_affiliates_label = "//table[@id='statistic-data-table']/tbody/tr[4]/td[1]"
    td_sub_affiliates_month = "//table[@id='statistic-data-table']/tbody/tr[4]/td[2]"
    td_sub_affiliates_total = "//table[@id='statistic-data-table']/tbody/tr[4]/td[3]"
    
    tr_deposits = "//table[@id='statistic-data-table']/tbody/tr[5]"
    td_deposits_label = "//table[@id='statistic-data-table']/tbody/tr[5]/td[1]"
    td_deposits_month = "//table[@id='statistic-data-table']/tbody/tr[5]/td[2]"
    td_deposits_total = "//table[@id='statistic-data-table']/tbody/tr[5]/td[3]"
    
    tr_fdm_deposit = "//table[@id='statistic-data-table']/tbody/tr[6]"
    td_fdm_deposit_label = "//table[@id='statistic-data-table']/tbody/tr[6]/td[1]"
    td_fdm_deposit_month = "//table[@id='statistic-data-table']/tbody/tr[6]/td[2]"
    td_fdm_deposit_total = "//table[@id='statistic-data-table']/tbody/tr[6]/td[3]"
    
    tr_turnover = "//table[@id='statistic-data-table']/tbody/tr[7]"
    td_turnover_label = "//table[@id='statistic-data-table']/tbody/tr[7]/td[1]"
    td_turnover_month = "//table[@id='statistic-data-table']/tbody/tr[7]/td[2]"
    td_turnover_total = "//table[@id='statistic-data-table']/tbody/tr[7]/td[3]"
    
    tr_ggr = "//table[@id='statistic-data-table']/tbody/tr[8]"
    td_ggr_label = "//table[@id='statistic-data-table']/tbody/tr[8]/td[1]"
    td_ggr_month = "//table[@id='statistic-data-table']/tbody/tr[8]/td[2]"
    td_ggr_total = "//table[@id='statistic-data-table']/tbody/tr[8]/td[3]"
    
    tr_tracking_pc = "//table[@id='statistic-data-table']/tbody/tr[9]"
    td_tracking_pc_label = "//table[@id='statistic-data-table']/tbody/tr[9]/td[1]"
    td_tracking_pc_month = "//table[@id='statistic-data-table']/tbody/tr[9]/td[2]"
    lnk_tracking_pc_month = "//table[@id='statistic-data-table']/tbody/tr[9]/td[2]/a"
    td_tracking_pc_total = "//table[@id='statistic-data-table']/tbody/tr[9]/td[3]"
    
    tr_tracking_mobile = "//table[@id='statistic-data-table']/tbody/tr[10]"
    td_tracking_mobile_label = "//table[@id='statistic-data-table']/tbody/tr[10]/td[1]"
    td_tracking_mobile_month = "//table[@id='statistic-data-table']/tbody/tr[10]/td[2]"
    lnk_tracking_mobile_month = "//table[@id='statistic-data-table']/tbody/tr[10]/td[2]/a"
    td_tracking_mobile_total = "//table[@id='statistic-data-table']/tbody/tr[10]/td[3]"
    
    # Dynamic methods for month selection
    @staticmethod
    def btn_month_by_name(month_name):
        month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        if month_name not in month_names:
            raise ValueError(f"Month name must be one of {month_names}")
        
        month_index = month_names.index(month_name)
        row = month_index // 3 + 1
        col = month_index % 3 + 1
        
        return f"//table[@id='statistic-data-table']/thead/tr/th[2]//table[@class='mp-month-table']/tbody/tr[{row}]/td[{col}]/button"
    
    @staticmethod
    def opt_year_by_value(year_value):
        return f"//table[@id='statistic-data-table']/thead/tr/th[2]//select[@class='mp-select-year']/option[@value='{year_value}']" 