class HomeElements:

    # App container and header
    div_intro_text = "//div[@class='pt-2 pb-2']"
    
    # Tasks waiting section
    div_home_container = "//div[@class='home col-xl-7']"
    div_waiting_approval = "//div[@class='waiting-approval']"
    spn_waiting_approval_title = "//div[@class='waiting-approval']//span[@class='home-title']"
    div_background_gray = "//div[@class='waiting-approval']//div[@class='background-gray col-sm-12']"
    div_affiliate_label = "//div[@class='waiting-approval']//div[@class='text-border col-sm-3']"
    div_affiliate_count = "//div[@class='waiting-approval']//div[@class='text-border col-sm-2'][1]"
    lnk_pending_affiliates = "//div[@class='waiting-approval']//div[@class='text-border col-sm-2'][1]/a"
    div_payment_request_label = "//div[@class='waiting-approval']//div[@class='text-border col-sm-5']"
    div_payment_request_count = "//div[@class='waiting-approval']//div[@class='text-border col-sm-2'][2]"
    lnk_payment_requests = "//div[@class='waiting-approval']//div[@class='text-border col-sm-2'][2]/a"
    
    # Banner statistics section
    div_banner_statistics = "//div[@class='banner-statistics']"
    spn_banner_statistics_title = "//div[@class='banner-statistics']//span[@class='home-title']"
    div_banner_statistics_content = "//div[@class='banner-statistics']//div[@class='background-gray border row']"
    lnk_total_banners = "//div[@class='banner-statistics']//div[@class='col-sm-12'][1]//a"
    lnk_player_banners = "//div[@class='banner-statistics']//div[@class='col-sm-12'][2]//a[1]"
    lnk_subaffiliate_banners = "//div[@class='banner-statistics']//div[@class='col-sm-12'][2]//a[2]"
    
    # Affiliate statistics panels
    div_affiliate_stats_now = "//div[@class='home-panel col-sm-6'][1]"
    spn_affiliate_stats_now_title = "//div[@class='home-panel col-sm-6'][1]//span[@class='home-panel-header-right home-title']"
    div_affiliate_now_count = "//div[@class='home-panel col-sm-6'][1]//div[@class='pl-4 col-sm-12'][1]"
    div_affiliate_now_status = "//div[@class='home-panel col-sm-6'][1]//div[@class='pl-4 col-sm-12'][2]"
    lnk_pending_affiliates_stats = "//div[@class='home-panel col-sm-6'][1]//div[@class='pl-4 col-sm-12'][2]//a[1]"
    lnk_approved_affiliates = "//div[@class='home-panel col-sm-6'][1]//div[@class='pl-4 col-sm-12'][2]//a[2]"
    lnk_disapproved_affiliates = "//div[@class='home-panel col-sm-6'][1]//div[@class='pl-4 col-sm-12'][2]//a[3]"
    lnk_suspended_affiliates = "//div[@class='home-panel col-sm-6'][1]//div[@class='pl-4 col-sm-12'][2]//a[4]"
    
    div_affiliate_stats_month = "//div[@class='home-panel home-right col'][1]"
    spn_affiliate_stats_month_title = "//div[@class='home-panel home-right col'][1]//span[@class='home-panel-header-right home-title']"
    div_affiliate_month_count = "//div[@class='home-panel home-right col'][1]//div[@class='pl-4 col-sm-12'][1]"
    div_affiliate_month_status = "//div[@class='home-panel home-right col'][1]//div[@class='pl-4 col-sm-12'][2]"
    
    # Player statistics panels
    div_player_stats_now = "//div[@class='home-panel col-sm-6'][2]"
    spn_player_stats_now_title = "//div[@class='home-panel col-sm-6'][2]//span[@class='home-panel-header-right home-title']"
    div_player_now_count = "//div[@class='home-panel col-sm-6'][2]//div[@class='pl-4 col-sm-12'][1]"
    div_player_now_deposit_status = "//div[@class='home-panel col-sm-6'][2]//div[@class='pl-4 col-sm-12'][2]"
    tbl_player_now_statistics = "//div[@class='home-panel col-sm-6'][2]//table[@class='member-statistics-table table']"
    td_total_deposits_label = "//div[@class='home-panel col-sm-6'][2]//td[@class='title'][1]"
    td_total_deposits_value = "//div[@class='home-panel col-sm-6'][2]//td[@class='content'][1]"
    td_total_psp_fees_label = "//div[@class='home-panel col-sm-6'][2]//td[@class='title'][2]"
    td_total_psp_fees_value = "//div[@class='home-panel col-sm-6'][2]//td[@class='content'][2]"
    td_total_ggr_label = "//div[@class='home-panel col-sm-6'][2]//td[@class='title'][3]"
    td_total_ggr_value = "//div[@class='home-panel col-sm-6'][2]//td[@class='content'][3]"
    td_total_bonus_label = "//div[@class='home-panel col-sm-6'][2]//td[@class='title'][4]"
    td_total_bonus_value = "//div[@class='home-panel col-sm-6'][2]//td[@class='content'][4]"
    td_total_rebate_label = "//div[@class='home-panel col-sm-6'][2]//td[@class='title'][5]"
    td_total_rebate_value = "//div[@class='home-panel col-sm-6'][2]//td[@class='content'][5]"
    td_company_net_win_label = "//div[@class='home-panel col-sm-6'][2]//td[@class='title-total']"
    td_company_net_win_value = "//div[@class='home-panel col-sm-6'][2]//td[@class='content-total']"
    
    div_player_stats_month = "//div[@class='home-panel home-right col'][2]"
    spn_player_stats_month_title = "//div[@class='home-panel home-right col'][2]//span[@class='home-panel-header-right home-title']"
    div_player_month_count = "//div[@class='home-panel home-right col'][2]//div[@class='pl-4 col-sm-12'][1]"
    div_player_month_deposit_status = "//div[@class='home-panel home-right col'][2]//div[@class='pl-4 col-sm-12'][2]"
    tbl_player_month_statistics = "//div[@class='home-panel home-right col'][2]//table[@class='member-statistics-table table']"
    
    # Online List section
    div_data_content = "//div[@class='data-content mb-5 mt-3']"
    div_filter_container = "//div[@class='filter-container']"
    spn_online_list_title = "//div[@class='filter-container']//span[@class='text-primary']"
    sel_refresh_interval = "//div[@class='filter-container']//select"
    btn_timer = "//button[@class='home-btn-link btn btn-link']"
    spn_timer_icon = "//button[@class='home-btn-link btn btn-link']/span[@class='icontime']"
    
    # Online List table
    div_table_responsive = "//div[@class='table-responsive table-striped my-2']"
    div_table_container = "//div[@class='table-container']"
    div_header_content = "//div[@class='header-content']"
    tbl_header = "//div[@class='header-content']//table"
    th_number = "//div[@class='header-content']//th[1]"
    th_username = "//div[@class='header-content']//th[2]"
    th_logged_in = "//div[@class='header-content']//th[3]"
    th_last_request = "//div[@class='header-content']//th[4]"
    th_ip = "//div[@class='header-content']//th[5]"
    th_role = "//div[@class='header-content']//th[6]"
    
    div_body_content = "//div[@class='body-content']"
    tbl_body = "//div[@class='body-content']//table"
    
    # Dynamic method for user row by index (1-based)
    @staticmethod
    def tr_user_by_index(index):
        return f"//div[@class='body-content']//table//tr[{index + 1}]"
    
    # Dynamic method for username cell by index (1-based)
    @staticmethod
    def td_username_by_index(index):
        return f"//div[@class='body-content']//table//tr[{index + 1}]/td[2]"
    
    # Dynamic method for username link by index (1-based)
    @staticmethod
    def lnk_username_by_index(index):
        return f"//div[@class='body-content']//table//tr[{index + 1}]/td[2]/a"
    
    # Pagination controls
    div_pagination = "//div[@class='page-container center-align']"
    lnk_first_page = "//div[@class='page-container center-align']/a[@class='icon page-first']"
    lnk_prev_page = "//div[@class='page-container center-align']/a[@class='icon page-prev']"
    div_page_input = "//div[@class='page-container center-align']/div[@class='page-input']"
    inp_page_number = "//div[@class='page-container center-align']//input[@class='page-form']"
    spn_total_pages = "//div[@class='page-container center-align']/div[@class='page-input']/span[2]"
    lnk_next_page = "//div[@class='page-container center-align']/a[@class='icon page-next']"
    lnk_last_page = "//div[@class='page-container center-align']/a[@class='icon page-last']"
    sel_page_size = "//div[@class='page-container center-align']/select[@class='pagesize-select']"
    spn_page_info = "//div[@class='page-container center-align']/span[@class='page-info']"
    
    # Dynamic method for page size option
    @staticmethod
    def opt_page_size_by_value(size_value):
        return f"//select[@class='pagesize-select']/option[@value='{size_value}']" 