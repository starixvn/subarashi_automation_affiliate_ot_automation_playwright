class SubAffiliateDomainElements:
    # Data content
    div_data_content = "//div[@class='data-content']"
    
    # Add button
    div_actions = "//div[@class='my-2']"
    btn_add_domain = "//button[contains(text(), 'Add Sub-Affiliate Domain')]"
    icn_add_domain = "//span[@class='oi oi-plus ml-2']"
    
    # Table elements
    div_domain_list = "//div[@class='domain-list-content table-responsive table-striped my-2']"
    div_table_container = "//div[@class='table-container']"
    
    # Table headers
    tbl_domains = "//table[@class='table']"
    th_number = "//th[@title='#']"
    th_domain = "//th[@title='Domain']"
    th_ssl = "//th[@title='SSL']"
    th_creator = "//th[@title='Creator']"
    th_created_date = "//th[@title='Created Date']"
    th_edit = "//th[@title='Edit']"
    th_delete = "//th[@title='Delete']"
    
    # Table row elements
    td_row_number = "//td[@class='text-center' and @title]"
    td_domain = "//td[@class='text-center' and @title]"
    chk_ssl = "//td[@class='text-center']/input[@type='checkbox']"
    td_creator = "//td[@class='text-center' and @title]"
    td_created_date = "//td[@class='text-center']"
    
    td_edit = "//td[@class='text-center' and @title='Edit Domain']"
    btn_edit = "//td[@title='Edit Domain']/button"
    icn_edit = "//td[@title='Edit Domain']/button/span[@class='oi oi-pencil text-secondary']"
    
    td_delete = "//td[@class='text-center' and @title='Delete Domain']"
    btn_delete = "//td[@title='Delete Domain']/button"
    icn_delete = "//td[@title='Delete Domain']/button/span[@class='oi oi-x text-danger']"
    
    # Add Modal elements
    mdl_add_domain = "//div[@class='modal-dialog']"
    mdl_content = "//div[@class='modal-content']"
    mdl_header = "//div[@class='modal-header']"
    mdl_title = "//h5[@class='modal-title']"
    icn_popup = "//span[@class='iconpopup']"
    txt_add_title = "//h5[contains(text(), 'Add Sub-Affiliate Domain')]"
    btn_close = "//button[@class='close']"
    icn_close = "//button[@class='close']/span"
    
    mdl_body = "//div[@class='modal-body']"
    div_body_wrapper = "//div[@class='modal-body-wrapper']"
    div_form_container = "//div[@class='domain-form-container']"
    frm_domain = "//form[@autocomplete='off']"
    
    # Domain name field
    div_domain_name = "//div[@class='align-items-center mb-2 row form-group'][1]"
    lbl_domain_name = "//label[@for='domainName']"
    inp_domain_name = "//input[@name='domainName']"
    
    # SSL field
    div_ssl = "//div[@class='align-items-center mb-2 row form-group'][2]"
    lbl_ssl = "//label[text()='SSL']"
    chk_ssl_modal = "//input[@name='isSSL']"
    
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