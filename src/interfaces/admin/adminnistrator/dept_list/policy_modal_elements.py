class PolicyModalElements:
    # Modal container elements
    mdl_policy = "//div[@class='modal-dialog']"
    mdl_content = "//div[@class='modal-content']"
    mdl_header = "//div[@class='modal-header']"
    mdl_title = "//h5[@class='modal-title']"
    div_title_text = "//div[@class='text-truncate']"
    txt_policy_title = "//div[@class='text-truncate']/text()"
    icn_popup = "//span[@class='iconpopup']"
    btn_close = "//button[@class='close']"
    icn_close = "//button[@class='close']/span[@aria-hidden='true']"
    
    # Container elements
    mdl_body = "//div[@class='modal-body']"
    div_body_wrapper = "//div[@class='modal-body-wrapper']"
    div_policy_container = "//div[@class='policy-form-container']"
    div_policy_list = "//div[@class='policy-list-content']"
    
    # Table element
    tbl_policy = "//table[@class='policy-data-table table']"
    
    # Table headers
    th_function = "//th[contains(text(), 'Function')]"
    th_group_permission = "//th[contains(text(), 'Group Permission')]"
    th_read = "//tr[2]/th[text()='Read']"
    th_host = "//tr[2]/th[text()='Host']"
    
    # Function rows, checkboxes (examples for common functions)
    def get_function_row(self, function_name):
        return f"//td[@title='{function_name}' and @colspan='2']/parent::tr"
    
    def get_function_read_checkbox(self, function_name):
        return f"//td[@title='{function_name}']/following-sibling::td[1]/input[@name='HasRead']"
    
    def get_function_host_checkbox(self, function_name):
        return f"//td[@title='{function_name}']/following-sibling::td[2]/input[@name='HasHost']"
    
    # Common functions rows
    td_user_control = "//td[@title='User Control']"
    chk_user_control_read = "//td[@title='User Control']/following-sibling::td[1]/input[@name='HasRead']"
    chk_user_control_host = "//td[@title='User Control']/following-sibling::td[2]/input[@name='HasHost']"
    
    td_affiliate = "//td[@title='Affiliate']"
    chk_affiliate_read = "//td[@title='Affiliate']/following-sibling::td[1]/input[@name='HasRead']"
    chk_affiliate_host = "//td[@title='Affiliate']/following-sibling::td[2]/input[@name='HasHost']"
    
    td_payment = "//td[@title='Payment']"
    chk_payment_read = "//td[@title='Payment']/following-sibling::td[1]/input[@name='HasRead']"
    chk_payment_host = "//td[@title='Payment']/following-sibling::td[2]/input[@name='HasHost']"
    
    td_media = "//td[@title='Media']"
    chk_media_read = "//td[@title='Media']/following-sibling::td[1]/input[@name='HasRead']"
    chk_media_host = "//td[@title='Media']/following-sibling::td[2]/input[@name='HasHost']"
    
    td_domain_control = "//td[@title='Domain Control']"
    chk_domain_control_read = "//td[@title='Domain Control']/following-sibling::td[1]/input[@name='HasRead']"
    chk_domain_control_host = "//td[@title='Domain Control']/following-sibling::td[2]/input[@name='HasHost']"
    
    td_player = "//td[@title='Player']"
    chk_player_read = "//td[@title='Player']/following-sibling::td[1]/input[@name='HasRead']"
    chk_player_host = "//td[@title='Player']/following-sibling::td[2]/input[@name='HasHost']"
    
    # Action buttons
    btn_update = "//button[contains(@class, 'btn-success') and text()='Update']"
    btn_cancel = "//button[contains(@class, 'btn-info') and text()='Cancel']" 