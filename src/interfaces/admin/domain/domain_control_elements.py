class DomainControlElements:
    # Filter section elements
    div_filter_container = "//div[@class='filter-container my-2']"
    div_form_inline = "//div[@class='form-inline']"
    
    # Target Country field
    div_target_country = "//div[@class='mr-sm-2 form-group']"
    lbl_target_country = "//label[text()='Target Country']"
    sel_target_country = "//select[@name='targetCountry']"
    opt_all = "//select[@name='targetCountry']/option[@value='']"
    
    # Aff Sub-domain field
    div_aff_subdomain = "//div[@class='mr-sm-3 form-group']"
    lbl_aff_subdomain = "//label[text()='Aff Sub-domain']"
    div_multiple_select = "//div[@class='multiple-select-container']"
    btn_select_dropdown = "//button[@class='multiple-select-default multiple-select-label']"
    span_text_display = "//span[@class='text-display']"
    div_options_container = "//div[@class='multiple-select-default multiple-select-options-container']"
    ul_option_all = "//ul[@class='multiple-select-options multiple-select-option-all']"
    chk_option_all = "//input[@id='multiple-select-1-optionItemAll']"
    span_option_all = "//span[@class='option-label' and text()='All']"
    ul_options = "//ul[@class='multiple-select-options']"
    
    # Search button
    btn_search = "//button[contains(@class, 'btn-outline-primary')]"
    icn_search = "//span[@class='oi oi-magnifying-glass']"
    
    # Data content
    div_data_content = "//div[@class='data-content']"
    
    # Add New button
    div_actions = "//div[@class='my-2']"
    btn_add_new = "//button[text()='Add New ']"
    icn_add_new = "//span[@class='oi oi-plus ml-2']"
    
    # Table elements
    div_domain_list = "//div[@class='domain-list-content table-responsive table-striped my-2']"
    div_table_container = "//div[@class='table-container']"
    
    # Table headers
    tbl_domains = "//table[@class='table']"
    th_number = "//th[@title='#']"
    th_target_country = "//th[@title='Target Country']"
    th_aff_domain = "//th[@title='Aff Domain']"
    th_redirect_domain = "//th[@title='Redirect Domain']"
    th_creator = "//th[@title='Creator']"
    th_created_date = "//th[@title='Created Date']"
    th_status = "//th[@title='Status']"
    th_edit = "//th[@title='Edit']"
    th_delete = "//th[@title='Delete']"
    
    # Table row elements
    td_row_number = "//td[@class='text-center' and @title]"
    td_target_country = "//td[@class='text-center' and @title]"
    td_aff_domain = "//td[@class='text-center' and @title]"
    td_redirect_domain = "//td[@class='text-center' and @title]"
    td_creator = "//td[@class='text-center' and @title]"
    td_created_date = "//td[@class='text-center' and @title]"
    
    chk_status = "//td[@class='text-center']/input[@type='checkbox']"
    
    td_edit = "//td[@class='text-center' and @title='Edit Domain']"
    btn_edit = "//td[@title='Edit Domain']/button"
    icn_edit = "//td[@title='Edit Domain']/button/span[@class='oi oi-pencil text-secondary']"
    
    td_delete = "//td[@class='text-center' and @title='Delete Domain']"
    btn_delete = "//td[@title='Delete Domain']/button"
    icn_delete = "//td[@title='Delete Domain']/button/span[@class='oi oi-x text-danger']"
    
    # Add Modal elements
    mdl_add_domain = "//div[@class='modal-content']"
    mdl_header = "//div[@class='modal-header']"
    mdl_title = "//h5[@class='modal-title']"
    icn_popup = "//span[@class='iconpopup']"
    txt_add_title = "//h5[contains(text(), 'Add New Domain Control')]"
    btn_close = "//button[@class='close']"
    icn_close = "//button[@class='close']/span"
    
    mdl_body = "//div[@class='modal-body']"
    div_body_wrapper = "//div[@class='modal-body-wrapper']"
    div_form_container = "//div[@class='domain-form-container']"
    frm_domain = "//form[@autocomplete='off']"
    
    # Aff Domain dropdown in modal
    div_aff_domain = "//div[@class='align-items-center mb-2 row form-group'][1]"
    lbl_aff_domain = "//label[@for='affDomainId']"
    div_select_aff_domain = "//div[@id='select-affDomain']"
    btn_select_aff_domain = "//div[@id='select-affDomain']/button"
    span_aff_domain_display = "//div[@id='select-affDomain']//span[@class='text-display']"
    div_aff_domain_options = "//div[@id='select-affDomain']/div[@class='select-options-container']"
    inp_aff_domain_filter = "//div[@id='select-affDomain']//input[@name='inputOption']"
    ul_aff_domain_options = "//div[@id='select-affDomain']/div[@class='select-options-container']/ul[@class='select-options'][2]"
    
    # Redirect Domain dropdown in modal
    div_redirect_domain = "//div[@class='align-items-center mb-2 row form-group'][2]"
    lbl_redirect_domain = "//label[@for='redirectDomainId']"
    div_select_redirect_domain = "//div[@id='select-redirectDomain']"
    btn_select_redirect_domain = "//div[@id='select-redirectDomain']/button"
    span_redirect_domain_display = "//div[@id='select-redirectDomain']//span[@class='text-display']"
    div_redirect_domain_options = "//div[@id='select-redirectDomain']/div[@class='select-options-container']"
    inp_redirect_domain_filter = "//div[@id='select-redirectDomain']//input[@name='inputOption']"
    ul_redirect_domain_options = "//div[@id='select-redirectDomain']/div[@class='select-options-container']/ul[@class='select-options'][2]"
    
    # Target Country dropdown in modal
    div_target_country_modal = "//div[@class='align-items-center mb-2 row form-group'][3]"
    lbl_target_country_modal = "//label[@for='targetCountryCode']"
    sel_target_country_modal = "//select[@name='targetCountryCode']"
    
    # Status checkbox in modal
    div_status = "//div[@class='align-items-center mb-2 row form-group'][4]"
    lbl_status = "//label[text()='Status']"
    chk_status_modal = "//input[@name='isUsed']"
    
    # Action buttons
    btn_add = "//button[contains(@class, 'btn-success') and text()='Add']"
    btn_cancel = "//button[contains(@class, 'btn-info') and text()='Cancel']"
    
    # Delete confirmation dialog
    mdl_delete_confirm = "//div[@class='modal-dialog']"
    div_notification_content = "//div[@class='notification-popup-content p-3']"
    h5_domain_name = "//h5[contains(text(), 'aff-12bet.nexdev.net')]"
    div_confirm_message = "//div[@style='white-space: pre-line;']"
    div_button_container = "//div[@class='float-right mt-4']"
    btn_confirm_ok = "//button[contains(@class, 'btn-primary')]"
    btn_confirm_cancel = "//button[contains(@class, 'btn-light')]"
    
    # Helper methods for dynamic selectors
    def get_option_by_text(self, option_text):
        return f"//span[@class='option-label' and text()='{option_text}']"
    
    def get_checkbox_by_index(self, index):
        return f"//input[@id='multiple-select-1-optionItem-{index}']"
    
    def get_row_by_number(self, row_number):
        return f"//td[@class='text-center' and @title='{row_number}']/parent::tr"
    
    def get_row_by_domain(self, domain_name):
        return f"//td[@class='text-center' and @title='{domain_name}']/parent::tr"
    
    def get_edit_button_by_row(self, row_number):
        return f"//td[@class='text-center' and @title='{row_number}']/parent::tr//td[@title='Edit Domain']/button"
    
    def get_delete_button_by_row(self, row_number):
        return f"//td[@class='text-center' and @title='{row_number}']/parent::tr//td[@title='Delete Domain']/button" 