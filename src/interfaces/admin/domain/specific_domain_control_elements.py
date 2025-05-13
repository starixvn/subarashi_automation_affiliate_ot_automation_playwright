class SpecificDomainControlElements:
    # Filter section elements
    div_filter_container = "//div[@class='filter-container my-2']"
    div_form_inline = "//div[@class='form-inline']"
    
    # Affiliate field
    div_affiliate = "//div[@class='mr-sm-3 form-group'][1]"
    lbl_affiliate = "//label[text()='Affiliate']"
    inp_affiliate = "//input[@name='affUsername']"
    
    # Aff Domain field
    div_aff_domain = "//div[@class='mr-sm-3 form-group'][2]"
    lbl_aff_domain = "//label[text()='Aff Domain']"
    inp_aff_domain = "//input[@name='affDomain']"
    
    # Redirect Domain field
    div_redirect_domain = "//div[@class='mr-sm-3 form-group'][3]"
    lbl_redirect_domain = "//label[text()='Redirect Domain']"
    inp_redirect_domain = "//input[@name='redirectDomain']"
    
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
    th_affiliate = "//th[@title='Affiliate']"
    th_aff_domain = "//th[@title='Aff Domain']"
    th_redirect_domain = "//th[@title='Redirect Domain']"
    th_creator = "//th[@title='Creator']"
    th_created_date = "//th[@title='Created Date']"
    th_updated_by = "//th[@title='Updated By']"
    th_updated_date = "//th[@title='Updated Date']"
    th_status = "//th[@title='Status']"
    th_edit = "//th[@title='Edit']"
    th_delete = "//th[@title='Delete']"
    
    # Table row elements
    td_row_number = "//td[@class='text-center' and @title]"
    td_affiliate = "//td[@class='text-center' and @title]"
    td_aff_domain = "//td[@class='text-center' and @title]"
    td_redirect_domain = "//td[@class='text-center' and @title]"
    td_creator = "//td[@class='text-center' and @title]"
    td_created_date = "//td[@class='text-center' and @title]"
    td_updated_by = "//td[@class='text-center' and @title]"
    td_updated_date = "//td[@class='text-center' and @title]"
    
    chk_status = "//td[@class='text-center']/input[@type='checkbox']"
    
    td_edit = "//td[@class='text-center' and @title='Edit Domain']"
    btn_edit = "//td[@title='Edit Domain']/button"
    icn_edit = "//td[@title='Edit Domain']/button/span[@class='oi oi-pencil text-secondary']"
    
    td_delete = "//td[@class='text-center' and @title='Delete Domain']"
    btn_delete = "//td[@title='Delete Domain']/button"
    icn_delete = "//td[@title='Delete Domain']/button/span[@class='oi oi-x text-danger']"
    
    # Pagination elements
    div_pagination = "//div[@class='page-container center-align']"
    btn_first_page = "//a[@class='icon page-first']"
    btn_prev_page = "//a[@class='icon page-prev']"
    div_page_input = "//div[@class='page-input']"
    txt_page_label = "//span[text()='Page ']"
    inp_page_number = "//input[@class='page-form']"
    txt_page_total = "//span[contains(text(), 'of')]"
    btn_next_page = "//a[@class='icon page-next']"
    btn_last_page = "//a[@class='icon page-last']"
    sel_page_size = "//select[@class='pagesize-select']"
    txt_page_info = "//span[@class='page-info']"
    
    # Add Modal elements
    mdl_add_domain = "//div[@class='modal-dialog']"
    mdl_content = "//div[@class='modal-content']"
    mdl_header = "//div[@class='modal-header']"
    mdl_title = "//h5[@class='modal-title']"
    icn_popup = "//span[@class='iconpopup']"
    txt_add_title = "//h5[contains(text(), 'Add New Specific Domain Control')]"
    btn_close = "//button[@class='close']"
    icn_close = "//button[@class='close']/span"
    
    mdl_body = "//div[@class='modal-body']"
    div_body_wrapper = "//div[@class='modal-body-wrapper']"
    div_form_container = "//div[@class='domain-form-container']"
    frm_domain = "//form[@autocomplete='off']"
    
    # Affiliate textarea
    div_aff_usernames = "//div[@class='align-items-center row form-group'][1]"
    lbl_aff_usernames = "//label[@for='affUsernames']"
    txt_aff_usernames = "//textarea[@id='affUsernames']"
    lbl_aff_instruction = "//div/label[contains(text(), 'Enter up to 500 affiliates')]"
    
    # Aff Domain field in modal
    div_modal_aff_domain = "//div[@class='align-items-center row form-group'][2]"
    lbl_modal_aff_domain = "//label[@for='affDomain']"
    inp_modal_aff_domain = "//input[@id='affDomain']"
    div_aff_domain_ssl = "//div[@class='col-sm-2']/div[@class='form-check']"
    lbl_aff_domain_ssl = "//input[@name='affDomainIsSSL']/parent::label"
    chk_aff_domain_ssl = "//input[@name='affDomainIsSSL']"
    
    # Redirect Domain field in modal
    div_modal_redirect_domain = "//div[@class='align-items-center row form-group'][3]"
    lbl_modal_redirect_domain = "//label[@for='redirectDomain']"
    inp_modal_redirect_domain = "//input[@id='redirectDomain']"
    div_redirect_domain_ssl = "//div[@class='col-sm-2']/div[@class='form-check']"
    lbl_redirect_domain_ssl = "//input[@name='redirectDomainIsSSL']/parent::label"
    chk_redirect_domain_ssl = "//input[@name='redirectDomainIsSSL']"
    
    # Status field
    div_status = "//div[@class='align-items-center row form-group'][4]"
    lbl_status = "//label[text()='Status']"
    chk_status_modal = "//input[@name='status']"
    
    # Action buttons
    btn_add = "//button[contains(@class, 'btn-success') and text()='Add']"
    btn_cancel = "//button[contains(@class, 'btn-info') and text()='Cancel']"
    
    # Delete confirmation dialog
    mdl_delete_confirm = "//div[@class='modal-dialog']"
    div_notification_content = "//div[@class='notification-popup-content p-3']"
    h5_domain_name = "//h5[contains(text(), 'aff-12bet.nexdev.net')]"
    div_confirm_message = "//div[@style='white-space: pre-line;']"
    div_button_container = "//div[@class='float-right mt-4']"
    btn_confirm_ok = "//button[contains(@class, 'btn-primary') and text()='OK']"
    btn_confirm_cancel = "//button[contains(@class, 'btn-light') and text()='Cancel']"
    
    # Helper methods for dynamic selectors
    def get_row_by_domain(self, domain_name):
        return f"//td[@class='text-center' and @title='{domain_name}']/parent::tr"
    
    def get_edit_button_by_domain(self, domain_name):
        return f"//td[@class='text-center' and @title='{domain_name}']/parent::tr//td[@title='Edit Domain']/button"
    
    def get_delete_button_by_domain(self, domain_name):
        return f"//td[@class='text-center' and @title='{domain_name}']/parent::tr//td[@title='Delete Domain']/button" 