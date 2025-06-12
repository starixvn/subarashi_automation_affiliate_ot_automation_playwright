class PolicyModalElements:
    
    # Modal container
    mdl_policy = "//div[@class='modal-dialog']"
    mdl_content = "//div[@class='modal-content']"
    mdl_header = "//div[@class='modal-header']"
    mdl_title = "//h5[@class='modal-title']"
    div_title_text = "//div[@class='text-truncate']"
    icn_popup = "//span[@class='iconpopup']"
    btn_close = "//button[@class='close']"
    icn_close = "//button[@class='close']/span[@aria-hidden='true']"
    
    # Policy form container
    div_policy_container = "//div[@class='policy-form-container']"
    tbl_policy = "//table[@class='policy-data-table table']"
    
    # Table headers
    th_function = "//th[contains(text(), 'Function')]"
    th_individual_permission = "//th[contains(text(), 'Individual Permission')]"
    th_individual_read = "//tr[1]/th[contains(text(), 'Individual Permission')]/following-sibling::th[1]"
    th_individual_host = "//tr[1]/th[contains(text(), 'Individual Permission')]/following-sibling::th[2]"
    th_group_permission = "//th[contains(text(), 'Group Permission')]"
    th_group_read = "//tr[1]/th[contains(text(), 'Group Permission')]/following-sibling::th[1]"
    th_group_host = "//tr[1]/th[contains(text(), 'Group Permission')]/following-sibling::th[2]"
    
    # Subheader row
    th_read = "//tr[2]/th[contains(text(), 'Read')]"
    th_host = "//tr[2]/th[contains(text(), 'Host')]"
    
    # Policy table rows (general selectors)
    def get_policy_row_by_name(self, function_name):
        return f"//td[@title='{function_name}' and @colspan='2']/.."
    
    def get_individual_read_checkbox(self, function_name):
        return f"//td[@title='{function_name}']/following-sibling::td[1]/input[@name='HasRead']"
    
    def get_individual_host_checkbox(self, function_name):
        return f"//td[@title='{function_name}']/following-sibling::td[2]/input[@name='HasHost']"
    
    def get_group_read_checkbox(self, function_name):
        return f"//td[@title='{function_name}']/following-sibling::td[3]/input[@name='HasRead']"
    
    def get_group_host_checkbox(self, function_name):
        return f"//td[@title='{function_name}']/following-sibling::td[4]/input[@name='HasHost']"
    
    # Specific examples for commonly used functions
    # User Control
    td_user_control = "//td[@title='User Control']"
    chk_user_control_ind_read = "//td[@title='User Control']/following-sibling::td[1]/input[@name='HasRead']"
    chk_user_control_ind_host = "//td[@title='User Control']/following-sibling::td[2]/input[@name='HasHost']"
    
    # Affiliate
    td_affiliate = "//td[@title='Affiliate']"
    chk_affiliate_ind_read = "//td[@title='Affiliate']/following-sibling::td[1]/input[@name='HasRead']"
    chk_affiliate_ind_host = "//td[@title='Affiliate']/following-sibling::td[2]/input[@name='HasHost']"
    
    # Payment
    td_payment = "//td[@title='Payment']"
    chk_payment_ind_read = "//td[@title='Payment']/following-sibling::td[1]/input[@name='HasRead']"
    chk_payment_ind_host = "//td[@title='Payment']/following-sibling::td[2]/input[@name='HasHost']"
    
    # Media
    td_media = "//td[@title='Media']"
    chk_media_ind_read = "//td[@title='Media']/following-sibling::td[1]/input[@name='HasRead']"
    chk_media_ind_host = "//td[@title='Media']/following-sibling::td[2]/input[@name='HasHost']"
    
    # Player
    td_player = "//td[@title='Player']"
    chk_player_ind_read = "//td[@title='Player']/following-sibling::td[1]/input[@name='HasRead']"
    chk_player_ind_host = "//td[@title='Player']/following-sibling::td[2]/input[@name='HasHost']"
    
    # Action buttons
    btn_update = "//button[contains(@class, 'btn-success') and contains(text(), 'Update')]"
    btn_cancel = "//button[contains(@class, 'btn-info') and contains(text(), 'Cancel')]" 