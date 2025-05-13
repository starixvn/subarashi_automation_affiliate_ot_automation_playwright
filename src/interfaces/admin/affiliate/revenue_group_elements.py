class RevenueGroupElements:
    """
    Element selectors for the Revenue Group page in the admin interface.
    
    Follows these criteria:
    - Each XPath selector targets a unique element
    - Uses IDs and unique classes where available
    - Avoids selectors that rely on text content where possible
    - Follows a clear DOM structure
    - Simple and direct XPath without unnecessary conditions
    """
    # Loader elements
    div_loader = "//div[@class='loader']"
    div_backdrop = "//div[@class='backdrop']"
    div_spinner = "//div[@class='spinner']"
    
    # Filter section
    div_filter_container = "//div[@class='filter-container']"
    lbl_group_name = "//div[@class='filter-container']//label[contains(text(), 'Group Name')]"
    inp_group_name = "//div[@class='filter-container']//input[@name='groupName']"
    btn_search = "//div[@class='filter-container']//button[contains(@class, 'btn-outline-primary')]"
    icon_search = "//div[@class='filter-container']//span[@class='oi oi-magnifying-glass']"
    
    # Main content area
    div_data_content = "//div[@class='data-content']"
    btn_add_new_group = "//div[@class='data-content']//button[contains(text(), 'Add New Group')]"
    
    # Table elements
    div_table_responsive = "//div[@class='table-responsive table-group-setting']"
    div_table_container = "//div[@class='table-container']"
    div_header_content = "//div[@class='header-content']"
    div_body_content = "//div[@class='body-content']"
    
    # Table header
    tbl_header = "//div[@class='header-content']//table"
    th_name = "//div[@class='header-content']//th[text()='Name']"
    th_no_aff = "//div[@class='header-content']//th[text()='No.Aff']"
    th_description = "//div[@class='header-content']//th[text()='Description']"
    th_creation = "//div[@class='header-content']//th[text()='Creation']"
    th_group_details = "//div[@class='header-content']//th[text()='Group Details']"
    th_deposit_fee = "//div[@class='header-content']//th[text()='Deposit Fee']"
    th_withdrawal_fee = "//div[@class='header-content']//th[text()='Withdrawal Fee']"
    th_sub_affiliate_comm_rate = "//div[@class='header-content']//th[text()='Sub-Affiliate Comm Rate']"
    th_qp_turnover = "//div[@class='header-content']//th[text()='QP Turnover']"
    th_action = "//div[@class='header-content']//th[text()='Action']"
    
    # Table body and row elements (generic first row selectors)
    tbl_body = "//div[@class='body-content']//table"
    td_row_number = "//div[@class='body-content']//td[@class='text-center' and @rowspan]"
    td_row_name = "//div[@class='body-content']//td[@class='text-center' and @rowspan and @title]"
    td_row_no_aff = "//div[@class='body-content']//td[@class='text-center' and @rowspan]/a"
    td_row_description = "//div[@class='body-content']//td[@class='text-center' and @rowspan and contains(text(), 'DONT EDIT')]"
    td_row_creation = "//div[@class='body-content']//td[@class='text-center' and @rowspan]/p[1]"
    td_row_creation_date = "//div[@class='body-content']//td[@class='text-center' and @rowspan]/p[2]"
    
    # Group details columns
    td_product_group = "//div[@class='body-content']//td[@class='cell-deduction']/div/strong"
    td_royalty_fee = "//div[@class='body-content']//td[@class='cell-deduction']/div"
    td_tier_column = "//div[@class='body-content']//td[@class='font-weight-bold text-center cell-deduction' and text()='Tier']"
    td_min_net_win_column = "//div[@class='body-content']//td[@class='font-weight-bold text-center cell-deduction' and text()='Min Net Win']"
    td_min_qualified_player_column = "//div[@class='body-content']//td[@class='font-weight-bold text-center cell-deduction' and text()='Min Qualified Player']"
    td_rev_share_column = "//div[@class='body-content']//td[@class='font-weight-bold text-center cell-deduction' and text()='Rev. Share%']"
    
    # Values in table
    td_deposit_fee = "//div[@class='body-content']//td[@class='text-right' and @title and contains(@title, '%')]"
    td_withdrawal_fee = "//div[@class='body-content']//td[@class='text-right' and @title and contains(@title, '%')][2]"
    td_sub_affiliate_comm_rate = "//div[@class='body-content']//td[@class='text-right' and @title and contains(@title, '%')][3]"
    td_qp_turnover = "//div[@class='body-content']//td[@class='text-right' and @title and contains(@title, '.')]"
    
    # Action buttons
    td_action = "//div[@class='body-content']//td[@class='text-center' and @rowspan]/button"
    btn_edit = "//div[@class='body-content']//button[@title='Edit']"
    icon_edit = "//div[@class='body-content']//span[@class='oi oi-pencil text-secondary']"
    btn_copy = "//div[@class='body-content']//button[@title='Copy']"
    icon_copy = "//div[@class='body-content']//span[@class='oi icon-copy text-secondary']"
    
    # Pagination
    div_page_container = "//div[@class='page-container center-align']"
    lnk_page_first = "//a[@class='icon page-first disable']"
    lnk_page_prev = "//a[@class='icon page-prev disable']"
    div_page_input = "//div[@class='page-input']"
    inp_page = "//input[@class='page-form']"
    lnk_page_next = "//a[@class='icon page-next disable']"
    lnk_page_last = "//a[@class='icon page-last disable']"
    sel_page_size = "//select[@class='pagesize-select']"
    spn_page_info = "//span[@class='page-info']"
    
    # Add/Edit Revenue Group Modal
    div_modal_dialog = "//div[@class='modal-dialog modal-lg']"
    div_modal_content = "//div[@class='modal-content']"
    div_modal_header = "//div[@class='modal-header']"
    h5_modal_title = "//h5[@class='modal-title']"
    btn_modal_close = "//button[@class='close']"
    
    # Form elements in modal
    div_modal_body = "//div[@class='modal-body']"
    div_modal_body_wrapper = "//div[@class='modal-body-wrapper commission-group']"
    lbl_group_name_modal = "//label[@for='GroupName']"
    inp_group_name_modal = "//input[@id='GroupName']"
    lbl_description = "//label[@for='Description']"
    inp_description = "//input[@id='Description']"
    
    # Sub-Affiliate Comm Rate section
    h6_sub_affiliate_comm_rate = "//h6[contains(text(), 'Sub-Affiliate Comm Rate')]"
    lbl_fixed_rate = "//label[text()='Fixed Rate']"
    sel_sub_aff_comm_rate = "//select[@name='SubAffCommRate']"
    
    # QP Turnover section
    h6_qp_turnover = "//h6[contains(text(), 'QP Turnover')]"
    lbl_usd = "//label[@for='QmTurnover']"
    inp_qm_turnover = "//input[@id='QmTurnover']"
    
    # Tier Rated Products Deduction section
    h6_tier_rated_products = "//h6[contains(text(), 'Tier Rated Products Deduction')]"
    p_product_groups = "//p[@class='font-weight-bold mr-5']"
    chk_count_qualified_player = "//input[@name='IsActivePlayerSum']"
    lbl_count_qualified_player = "//label[contains(text(), 'Count Qualified Player')]"
    
    # Product group selection
    div_multiple_select = "//div[@id='multiple-select-6']"
    btn_multiple_select = "//div[@id='multiple-select-6']/button"
    spn_multiple_select_text = "//span[@class='text-display']"
    div_multiple_select_options = "//div[@class='multiple-select-default multiple-select-options-container']"
    ul_multiple_select_options = "//ul[@class='multiple-select-options']"
    
    # Royalty Fee fields
    lbl_royalty_fee = "//label[@class='font-weight-bold pr-2']"
    sel_deducted_percentage = "//select[@name='DeductedPercentage']"
    lbl_gross_game_revenue = "//label[@class='ml-3 x-content']"
    
    # Tier setting table
    tbl_tier_setting = "//table[@class='table table-bordered tier-setting-table']"
    th_tier = "//table[@class='table table-bordered tier-setting-table']//th[text()='Tier']"
    th_min_net_win = "//table[@class='table table-bordered tier-setting-table']//th[text()='Min Net Win']"
    th_min_qualified_player = "//table[@class='table table-bordered tier-setting-table']//th[text()='Min Qualified Player']"
    th_rev_share = "//table[@class='table table-bordered tier-setting-table']//th[text()='Rev. Share%']"
    th_action = "//table[@class='table table-bordered tier-setting-table']//th[text()='Action']"
    
    # First tier row elements
    td_tier_1 = "//table[@class='table table-bordered tier-setting-table']//td[@class='text-center' and text()='1']"
    chk_infinity = "//input[@class='form-check-input' and ancestor::form[@class='group-input-infinity form-inline']]"
    lbl_infinity = "//label[@class='form-check-label' and contains(text(), '-∞')]"
    inp_min_amount = "//input[@id='MinAmount1']"
    inp_min_qm = "//input[@id='MinQm1']"
    sel_commission = "//select[@name='Commission']"
    btn_tier_action = "//table[@class='table table-bordered tier-setting-table']//button[@class='btn btn-action']"
    
    # Add Product Group button
    btn_add_product_group = "//button[@class='btn btn-action' and contains(text(), 'Add Product Group')]"
    
    # Banking Fee section
    p_banking_fee = "//p[@class='font-weight-bold pt-3']"
    lbl_deposit_fee = "//label[@class='font-weight-bold col-sm-3 col-form-label' and contains(text(), 'Deposit Fee')]"
    sel_deposit_fee = "(//select[@name='DeductedPercentage'])[2]"
    lbl_deposit = "//label[@class='ml-3 x-content' and text()='Deposit']"
    chk_deposit_fixed_amount = "//input[@name='IsDeductionPercent' and following-sibling::text()[contains(., 'Fixed Amount')]]"
    lbl_deposit_fixed_amount = "//label[@class='form-check-label' and contains(text(), 'Fixed Amount')][1]"
    
    lbl_withdrawal_fee = "//label[@class='font-weight-bold col-sm-3 col-form-label' and contains(text(), 'Withdrawal Fee')]"
    sel_withdrawal_fee = "(//select[@name='DeductedPercentage'])[3]"
    lbl_withdrawal = "//label[@class='ml-3 x-content' and text()='Withdrawal']"
    chk_withdrawal_fixed_amount = "(//input[@name='IsDeductionPercent'])[2]"
    lbl_withdrawal_fixed_amount = "//label[@class='form-check-label' and contains(text(), 'Fixed Amount')][2]"
    
    # Footer note and save button
    p_note = "//p[@class='text-danger']"
    btn_save = "//button[@class='my-2 btn btn-success btn-save']"
    
    # Helper methods for dynamic elements
    @staticmethod
    def li_product_option_by_index(index):
        return f"//li[@class='multiple-select-item'][{index}]"
    
    @staticmethod
    def chk_product_option_by_index(index):
        return f"//input[@id='multiple-select-6-optionItem-{index}']"
    
    @staticmethod
    def lbl_product_option_by_index(index):
        return f"//span[@class='option-label'][@for='multiple-select-6-optionItem-{index}']"
    
    @staticmethod
    def opt_percentage_by_value(value):
        return f"//select[@name='DeductedPercentage']/option[@value='{value}']"
    
    @staticmethod
    def opt_commission_by_value(value):
        return f"//select[@name='Commission']/option[@value='{value}']"
    
    @staticmethod
    def opt_sub_aff_rate_by_value(value):
        return f"//select[@name='SubAffCommRate']/option[@value='{value}']"
    
    @staticmethod
    def td_tier_by_number(tier_number):
        return f"//table[@class='table table-bordered tier-setting-table']//td[@class='text-center' and text()='{tier_number}']" 