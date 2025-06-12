class AffiliateReportElements:
    
    # Filter section elements
    inp_affiliate = "//input[@id='Affiliate']"
    sel_base_currency = "//select[@id='BaseCurrency']"
    btn_linked_account_currency = "//div[@id='multiple-select-1']//button"
    btn_currency = "//div[@id='multiple-select-2']//button"
    sel_language = "//select[@name='selectedLanguage']"
    btn_products = "//div[@id='multiple-select-3']//button"
    btn_revenue_groups = "//div[@id='multiple-select-4']//button"
    chk_date_picker = "//input[@name='isCheckedDatePicker']"
    inp_from_date = "//div[./label[text()='From']]/div//input"
    inp_to_date = "//div[./label[text()='To']]/div//input"
    sel_status = "//select[@name='selectedStatus']"
    sel_sort_by = "//select[@id='SortBy']"
    chk_sort_ascending = "//input[@name='isSortAscending']"
    chk_exclude_negative_balance = "//input[@name='isExcludeNegvBBF']"
    chk_exclude_negative_current_balance = "//input[@name='isExcludeNegvCurrentBBF']"
    btn_search = "//button[.//span[contains(@class, 'oi-magnifying-glass')]]"
    
    # Dropdown options
    opt_currency_all = "//div[@id='multiple-select-1']//li[.//span[text()='All']]//input"
    opt_products_all = "//div[@id='multiple-select-3']//li[.//span[text()='All']]//input"
    opt_revenue_groups_all = "//div[@id='multiple-select-4']//li[.//span[text()='All']]//input"
    
    # Report header and export
    lbl_report_title = "//div[@class='report-title']//div"
    btn_export_excel = "//button[contains(@class, 'btn-excel')]"
    
    # Table elements
    tbl_affiliate_report = "//table[@class='freeze-table table']"
    tbl_header_affiliate = "//th[@class='freeze-column-header' and @title='Affiliate']"
    tbl_header_status = "//th[@title='Status']"
    tbl_header_language = "//th[@title='Language']"
    tbl_header_linked_currency = "//th[@title='Linked Account Currency']"
    tbl_header_revenue_group = "//th[@title='Revenue Group']"
    tbl_header_total_click = "//th[@title='Total Click']"
    tbl_header_unique_click = "//th[@title='Unique Click']"
    tbl_header_signup = "//th[@title='Signup']"
    tbl_header_fdm = "//th[@title='FDM']"
    tbl_header_fdm_amount = "//th[@title='FDM Amt']"
    tbl_header_player_statistics = "//th[@title='Player Statistics']"
    tbl_header_affiliate_statistics = "//th[@title='Affiliate Statistics']"
    
    # Table data cells (first row)
    tbl_cell_affiliate = "//tbody/tr[1]/td[@class='freeze-column']"
    tbl_cell_status = "//tbody/tr[1]/td[@class='text-center' and @title='Approved']"
    tbl_cell_language = "//tbody/tr[1]/td[@title='English (Bangladesh)']"
    tbl_cell_linked_currency = "//tbody/tr[1]/td[@class='text-center' and @title='CNY']"
    tbl_cell_revenue_group = "//tbody/tr[1]/td[@title='StarixNina']"
    
    # Action buttons in table
    btn_view_month_on_month = "//tbody/tr[1]/td[contains(@class, 'text-center')]/button[text()='View']"
    btn_view_player_ggr = "//tbody/tr[1]/td[last()]/button[text()='View']"
    
    # Pagination controls
    btn_page_first = "//a[contains(@class, 'page-first')]"
    btn_page_prev = "//a[contains(@class, 'page-prev')]"
    inp_page_number = "//input[@class='page-form']"
    btn_page_next = "//a[contains(@class, 'page-next')]"
    btn_page_last = "//a[contains(@class, 'page-last')]"
    sel_page_size = "//select[@class='pagesize-select']"
    lbl_page_info = "//span[@class='page-info']"
    
    # Loader
    div_loader = "//div[@class='loader']" 