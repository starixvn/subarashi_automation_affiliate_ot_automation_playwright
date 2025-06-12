class AffiliateInfoElements:
    # Loader elements
    div_loader = "//div[@class='loader']"
    div_backdrop = "//div[@class='backdrop']"
    div_spinner = "//div[@class='spinner']"
    
    # Filter section - Revenue Groups dropdown
    div_filter_container = "//div[@class='filter-container']"
    div_form_inline = "//div[@class='filter-container']/div[@class='form-inline']"
    lbl_search_by = "//label[@for='SearchBy']"
    div_revenue_groups = "//div[@id='multiple-select-1']"
    btn_revenue_groups = "//div[@id='multiple-select-1']/button"
    spn_revenue_groups_text = "//div[@id='multiple-select-1']/button/span[@class='text-display']"
    div_revenue_groups_options = "//div[@id='multiple-select-1']/div[@class='multiple-select-default multiple-select-options-container']"
    ul_revenue_groups_all = "//div[@id='multiple-select-1']/div/ul[@class='multiple-select-options multiple-select-option-all']"
    chk_revenue_groups_all = "//input[@id='multiple-select-1-optionItemAll']"
    lbl_revenue_groups_all = "//span[@for='multiple-select-1-optionItemAll']"
    ul_revenue_groups_options = "//div[@id='multiple-select-1']/div/ul[@class='multiple-select-options']"
    
    # Target Country dropdown
    sel_target_country = "//select[@id='targetCountry']"
    opt_all_target_countries = "//select[@id='targetCountry']/option[@value='']"
    
    # Language dropdown
    sel_language = "//select[@id='language']"
    opt_all_languages = "//select[@id='language']/option[@value='']"
    
    # Status dropdown
    sel_status = "//select[@id='status']"
    opt_all_statuses = "//select[@id='status']/option[@value='']"
    
    # Filter input fields
    inp_parent_affiliate = "//input[@id='parentAffName']"
    inp_username = "//input[@id='username']"
    inp_email = "//input[@id='email']"
    inp_affiliate_code = "//input[@id='affCode']"
    inp_affiliate_player = "//input[@id='affPlayer']"
    
    # Sort By section
    lbl_sort_by = "//label[@for='SortBy']"
    sel_sort_by = "//select[@id='SortBy']"
    opt_sort_username = "//select[@id='SortBy']/option[@value='1']"
    opt_sort_registration_date = "//select[@id='SortBy']/option[@value='2']"
    opt_sort_approval_date = "//select[@id='SortBy']/option[@value='3']"
    opt_sort_balance = "//select[@id='SortBy']/option[@value='4']"
    opt_sort_player = "//select[@id='SortBy']/option[@value='5']"
    
    # A-Z checkbox
    lbl_az = "//div[@class='form-check-label']"
    chk_az = "//div[@class='form-check-label']/input[@type='checkbox']"
    
    # Displayed columns dropdown
    lbl_displayed_columns = "//label[text()='Displayed Columns']"
    div_displayed_columns = "//div[@id='multiple-select-2']"
    btn_displayed_columns = "//div[@id='multiple-select-2']/button"
    spn_displayed_columns_text = "//div[@id='multiple-select-2']/button/span[@class='text-display']"
    div_displayed_columns_options = "//div[@id='multiple-select-2']/div[@class='multiple-select-default multiple-select-options-container']"
    ul_displayed_columns_all = "//div[@id='multiple-select-2']/div/ul[@class='multiple-select-options multiple-select-option-all']"
    chk_displayed_columns_all = "//input[@id='multiple-select-2-optionItemAll']"
    lbl_displayed_columns_all = "//span[@for='multiple-select-2-optionItemAll']"
    ul_displayed_columns_options = "//div[@id='multiple-select-2']/div/ul[@class='multiple-select-options']"
    
    # Search button
    btn_search = "//button[@class='my-2 btn btn-outline-primary']"
    spn_search_icon = "//button[@class='my-2 btn btn-outline-primary']/span[@class='oi oi-magnifying-glass']"
    
    # Report section
    div_data_content = "//div[@class='data-content my-2']"
    div_report_title_container = "//div[@class='report-title-container']"
    div_report_title = "//div[@class='report-title']"
    div_report_flex = "//div[@class='report-title']/div[@class='d-flex align-items-center']"
    btn_export_excel = "//button[@class='ml-auto btn btn-link btn-excel']"
    spn_excel_icon = "//button[@class='ml-auto btn btn-link btn-excel']/span[@class='oi icon-excel']"
    
    # Table container
    div_table_container = "//div[@class='table-responsive table-striped aff-info-table-container']"
    tbl_affiliate_info = "//table[@class='freeze-table table']"
    
    # Table header
    tr_header = "//table[@class='freeze-table table']/thead/tr[@class='freeze-row']"
    th_number = "//th[@class='freeze-column-header freeze-column-header-0']"
    th_parent_affiliate = "//th[@class='freeze-column-header freeze-column-header-1']"
    th_username = "//th[@class='freeze-column-header freeze-column-header-2']"
    th_affiliate_code = "//th[@title='Affiliate Code']"
    th_status = "//th[@title='Status']"
    th_first_name = "//th[@title='First Name']"
    th_last_name = "//th[@title='Last Name']"
    th_target_country = "//th[@title='Target Country']"
    th_language = "//th[@title='Language']"
    th_mobile_phone = "//th[@title='Mobile Phone']"
    th_email = "//th[@title='Email']"
    th_registration_date = "//th[@title='Registration Date']"
    th_approval_date = "//th[@title='Approval Date']"
    th_approved_by = "//th[@title='Approved By']"
    th_revenue_group = "//th[@title='Revenue Group']"
    th_balance = "//th[@title='Balance B/F']"
    th_aff_currency = "//th[@title='Aff. Currency']"
    th_aff_player = "//th[@title='Aff. Player']"
    th_aff_player_currency = "//th[@title='Aff. Player Currency']"
    th_player = "//th[@title='Player']"
    th_sub_affiliate = "//th[@title='Sub-Affiliate']"
    th_password = "//th[@title='Password']"
    
    # Table body and row cells (first/only row in the example)
    tbody = "//table[@class='freeze-table table']/tbody"
    td_number = "//table[@class='freeze-table table']/tbody/tr/td[@class='text-center freeze-column-body freeze-column-body-0']"
    td_parent_affiliate = "//table[@class='freeze-table table']/tbody/tr/td[@class='freeze-column-body freeze-column-body-1']"
    td_username = "//table[@class='freeze-table table']/tbody/tr/td[@class='freeze-column-body freeze-column-body-2']"
    lnk_username = "//table[@class='freeze-table table']/tbody/tr/td[@class='freeze-column-body freeze-column-body-2']/a"
    spn_favor_uncheck = "//table[@class='freeze-table table']/tbody/tr/td[@class='freeze-column-body freeze-column-body-2']/span[@class='favor-uncheck']"
    td_affiliate_code = "//table[@class='freeze-table table']/tbody/tr/td[@title='10000']"
    td_status = "//table[@class='freeze-table table']/tbody/tr/td[@title='Approved']"
    td_first_name = "//table[@class='freeze-table table']/tbody/tr/td[@title='Nina']"
    td_last_name = "//table[@class='freeze-table table']/tbody/tr/td[@title='Testing']"
    td_target_country = "//table[@class='freeze-table table']/tbody/tr/td[@title='Bangladesh']"
    td_language = "//table[@class='freeze-table table']/tbody/tr/td[@title='English (Bangladesh)']"
    td_mobile_phone = "//table[@class='freeze-table table']/tbody/tr/td[@title='012345647896546']"
    td_email = "//table[@class='freeze-table table']/tbody/tr/td[@title='nina.nguyen1111@starixsoft.com']"
    td_registration_date = "//table[@class='freeze-table table']/tbody/tr/td[@title='05/22/2008 06:49:00']"
    td_approval_date = "//table[@class='freeze-table table']/tbody/tr/td[@title='06/23/2008 22:59:55']"
    td_approved_by = "//table[@class='freeze-table table']/tbody/tr/td[@title='sa']"
    td_revenue_group = "//table[@class='freeze-table table']/tbody/tr/td[@title='StarixNina']"
    td_balance = "//table[@class='freeze-table table']/tbody/tr/td[@class='text-right'][@title='5,997,150.19']"
    td_aff_currency = "//table[@class='freeze-table table']/tbody/tr/td[@title='USD']"
    td_aff_player = "//table[@class='freeze-table table']/tbody/tr/td[@title='mrchen']"
    td_aff_player_currency = "//table[@class='freeze-table table']/tbody/tr/td[@title='CNY']"
    td_player = "//table[@class='freeze-table table']/tbody/tr/td[@class='text-right'][@title='50,329']"
    lnk_player = "//table[@class='freeze-table table']/tbody/tr/td[@class='text-right'][@title='50,329']/a"
    td_sub_affiliate = "//table[@class='freeze-table table']/tbody/tr/td[@class='text-right'][@title='0']"
    btn_sub_affiliate = "//table[@class='freeze-table table']/tbody/tr/td[@class='text-right'][@title='0']/button"
    td_change_password = "//table[@class='freeze-table table']/tbody/tr/td[@class='text-center'][@title='Change Password']"
    btn_change_password = "//table[@class='freeze-table table']/tbody/tr/td[@class='text-center'][@title='Change Password']/button"
    spn_password_icon = "//table[@class='freeze-table table']/tbody/tr/td[@class='text-center'][@title='Change Password']/button/span[@class='oi oi-pencil text-secondary']"
    
    # Pagination section
    div_page_container = "//div[@class='page-container center-align']"
    lnk_page_first = "//a[@class='icon page-first disable']"
    lnk_page_prev = "//a[@class='icon page-prev disable']"
    div_page_input = "//div[@class='page-input']"
    inp_page = "//input[@class='page-form']"
    lnk_page_next = "//a[@class='icon page-next disable']"
    lnk_page_last = "//a[@class='icon page-last disable']"
    sel_page_size = "//select[@class='pagesize-select']"
    opt_page_size_10 = "//select[@class='pagesize-select']/option[@value='10']"
    opt_page_size_20 = "//select[@class='pagesize-select']/option[@value='20']"
    opt_page_size_50 = "//select[@class='pagesize-select']/option[@value='50']"
    opt_page_size_100 = "//select[@class='pagesize-select']/option[@value='100']"
    opt_page_size_200 = "//select[@class='pagesize-select']/option[@value='200']"
    opt_page_size_500 = "//select[@class='pagesize-select']/option[@value='500']"
    spn_page_info = "//span[@class='page-info']"
    
    # Generic methods for dynamic elements
    @staticmethod
    def chk_revenue_group_by_index(index):
        return f"//input[@id='multiple-select-1-optionItem-{index}']"
    
    @staticmethod
    def lbl_revenue_group_by_index(index):
        return f"//span[@for='multiple-select-1-optionItem-{index}']"
    
    @staticmethod
    def chk_displayed_column_by_index(index):
        return f"//input[@id='multiple-select-2-optionItem-{index}']"
    
    @staticmethod
    def lbl_displayed_column_by_index(index):
        return f"//span[@for='multiple-select-2-optionItem-{index}']"
    
    @staticmethod
    def opt_target_country_by_value(value):
        return f"//select[@id='targetCountry']/option[@value='{value}']"
    
    @staticmethod
    def opt_language_by_value(value):
        return f"//select[@id='language']/option[@value='{value}']"
    
    @staticmethod
    def opt_status_by_value(value):
        return f"//select[@id='status']/option[@value='{value}']"
    
    @staticmethod
    def tr_by_index(index):
        return f"//table[@class='freeze-table table']/tbody/tr[{index}]" 