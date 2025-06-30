"""
Edit Deal Modal Elements - Absolute Stable XPath mappings for 12BetAdmin2 Portal Deal Modal
Based on actual HTML structure analysis from live site - NO data-ref dependencies  
Production-ready element mappings with multiple fallback strategies for complex modal form
"""

class EditDealModalElements:
    """
    Edit Deal Modal Elements - Complete stable XPath mapping for deal editing operations
    Triggered by clicking on deal name buttons in the results table
    """
    
    # ========== MODAL CONTAINER & STRUCTURE ==========
    # Modal backdrop and container - STABLE by role and class
    div_modal_backdrop = "//div[@class='modal-backdrop fade show']"
    div_modal_container = "//div[@class='modal fade show'][@role='dialog']"
    div_modal_dialog = "//div[@class='modal-dialog deal-popup-container modal-lg']"
    div_modal_content = "//div[@class='modal-content']"
    
    # Modal header - STABLE by class and content
    div_modal_header = "//div[@class='modal-header']"
    h5_modal_title = "//h5[@class='modal-title']"
    h5_edit_deal = "//h5[contains(., 'Edit Deal')]"
    span_icon_popup = "//span[@class='iconpopup']"
    
    # Close button - STABLE by aria-label and class
    btn_close_modal = "//button[@type='button' and @aria-label='Close']"
    btn_close_modal_by_class = "//button[@class='close']"
    span_close_x = "//span[@aria-hidden='true' and text()='×']"
    
    # Modal body structure - STABLE by class
    div_modal_body = "//div[@class='modal-body']"
    div_modal_body_wrapper = "//div[@class='modal-body-wrapper']"
    
    # ========== BASIC DEAL INFORMATION ==========
    # Deal Name field - STABLE by ID, name and for attribute
    lbl_deal_name = "//label[@for='DealName' and contains(@class, 'col-form-label')]"
    lbl_deal_name_text = "//label[contains(., 'Deal Name')]"
    span_required_deal_name = "//label[@for='DealName']//span[@class='text-danger required']"
    inp_deal_name = "//input[@id='DealName' and @name='DealName']"
    inp_deal_name_by_class = "//input[@name='DealName' and @class='form-control']"
    
    # Deal Types field - STABLE by ID, name and for attribute  
    lbl_deal_types = "//label[@for='DealType' and contains(@class, 'col-form-label')]"
    lbl_deal_types_text = "//label[contains(., 'Deal Types')]"
    span_required_deal_types = "//label[@for='DealType']//span[@class='text-danger required']"
    sel_deal_types = "//select[@id='DealType' and @name='DealType']"
    sel_deal_types_disabled = "//select[@id='DealType' and @disabled]"
    
    # Deal Types options - STABLE by value and text
    opt_cpa = "//select[@name='DealType']/option[@value='3']"
    opt_cpa_text = "//select[@name='DealType']/option[text()='CPA']"
    opt_hybrid = "//select[@name='DealType']/option[@value='4']"  
    opt_hybrid_text = "//select[@name='DealType']/option[text()='Hybrid CPA/Revenue Share']"
    opt_revenue_share = "//select[@name='DealType']/option[@value='1']"
    opt_revenue_share_text = "//select[@name='DealType']/option[text()='Revenue Share']"
    
    # Description field - STABLE by ID, name and for attribute
    lbl_description = "//label[@for='Description' and contains(@class, 'col-form-label')]"
    lbl_description_text = "//label[text()='Description']"
    inp_description = "//input[@id='Description' and @name='Description']"
    inp_description_by_class = "//input[@name='Description' and @class='form-control']"
    
    # ========== SUB-AFFILIATE RATE SECTION ==========
    # Sub-Affiliate Rate fieldset - STABLE by legend and h6
    fieldset_sub_affiliate = "//fieldset"
    legend_sub_affiliate = "//legend"
    h6_sub_affiliate_rate = "//h6[contains(., 'Sub-Affiliate Rate')]"
    
    # Fixed Rate field - STABLE by ID, name and for attribute
    lbl_fixed_rate = "//label[@for='SubCommRate' and contains(@class, 'col-form-label')]"
    lbl_fixed_rate_text = "//label[text()='Fixed Rate']"
    sel_fixed_rate = "//select[@id='SubCommRate' and @name='SubCommRate']"
    sel_fixed_rate_by_class = "//select[@name='SubCommRate' and @class='form-control form-control']"
    
    # Fixed Rate options - STABLE by value and text
    opt_fixed_rate_5 = "//select[@name='SubCommRate']/option[@value='0.05']"
    opt_fixed_rate_5_text = "//select[@name='SubCommRate']/option[text()='5.0%']"
    opt_fixed_rate_10 = "//select[@name='SubCommRate']/option[@value='0.100']"
    opt_fixed_rate_10_text = "//select[@name='SubCommRate']/option[text()='10.0%']"
    opt_fixed_rate_20 = "//select[@name='SubCommRate']/option[@value='0.200']"
    opt_fixed_rate_20_text = "//select[@name='SubCommRate']/option[text()='20.0%']"
    
    # ========== TAB NAVIGATION ==========
    # Tab container - STABLE by class
    div_tabs = "//div[@class='tabs']"
    
    # Tab buttons - STABLE by class and content
    btn_cpa_tab = "//div[@class='tabs']//button[.//h7[text()='CPA']]"
    btn_cpa_tab_active = "//div[@class='tabs']//button[@class='active']"
    btn_revenue_share_tab = "//div[@class='tabs']//button[.//h7[text()='Revenue Share']]"
    h7_cpa = "//h7[text()='CPA']"
    h7_revenue_share = "//h7[text()='Revenue Share']"
    
    # Tab content - STABLE by class
    div_tab_content = "//div[@class='tab-content']"
    
    # ========== PLAYER TARGET COUNTRY ==========
    # Player Target Country section - STABLE by for attribute and content
    lbl_player_target_country = "//label[@for='CountryCodes' and contains(@class, 'col-form-label')]"
    lbl_player_target_text = "//label[contains(., 'Player Target Country')]"
    span_required_country = "//label[@for='CountryCodes']//span[@class='text-danger required']"
    
    # Multiple select container - STABLE by ID and class
    div_country_select = "//div[@id='multiple-select-1']"
    div_country_container = "//div[@class='multiple-select-container'][@id='multiple-select-1']"
    btn_country_dropdown = "//button[@class='multiple-select-default multiple-select-label']"
    btn_all_target_countries = "//button[.//span[@title='All Target Countries']]"
    span_country_text = "//span[@class='text-display'][@title='All Target Countries']"
    
    # Country options container - STABLE by class
    div_country_options = "//div[@class='multiple-select-default multiple-select-options-container']"
    ul_country_options_all = "//ul[@class='multiple-select-options multiple-select-option-all']"
    ul_country_options = "//ul[@class='multiple-select-options']"
    
    # Country checkboxes - STABLE by ID pattern and class
    chk_country_all = "//input[@id='multiple-select-1-optionItemAll']"
    chk_country_malaysia = "//input[@id='multiple-select-1-optionItem-0']"
    chk_country_bangladesh = "//input[@id='multiple-select-1-optionItem-1']"
    chk_country_india = "//input[@id='multiple-select-1-optionItem-2']"
    
    # ========== ACTIVITY PERIOD ==========
    # Activity Period field - STABLE by for attribute and content
    lbl_activity_period = "//label[@for='ActiveDays' and contains(@class, 'col-form-label')]"
    lbl_activity_text = "//label[contains(., 'Activity Period')]"
    span_required_activity = "//label[@for='ActiveDays']//span[@class='text-danger required']"
    span_info_activity = "//label[@for='ActiveDays']//span[@class='ml-1 oi icon-info']"
    inp_activity_period = "//input[@id='ActiveDays' and @name='ActiveDays']"
    inp_activity_by_class = "//input[@name='ActiveDays' and @class='form-control']"
    lbl_days = "//label[@class='text-content mb-0 ms-2' and text()='(days)']"
    
    # ========== MINIMUM PLAYER HOLDING PERIOD ==========
    # Holding Period section - STABLE by for attribute and content
    lbl_holding_period = "//label[@for='IsActivePlayerHoldingPeriod' and contains(@class, 'col-form-label')]"
    lbl_holding_text = "//label[contains(., 'Minimum Player Holding Period')]"
    span_info_holding = "//label[@for='IsActivePlayerHoldingPeriod']//span[@class='ml-1 oi icon-info']"
    chk_holding_period = "//input[@type='checkbox' and @name='IsActivePlayerHoldingPeriod']"
    
    # Holding Period inputs - STABLE by ID and name
    inp_holding_tickets = "//input[@id='HoldingTickets' and @name='HoldingTickets']"
    inp_holding_tickets_disabled = "//input[@name='HoldingTickets' and @disabled]"
    lbl_tickets_in = "//label[@class='text-content mb-0 ms-2' and text()='(tickets) in']"
    inp_holding_days = "//input[@id='HoldingDays' and @name='HoldingDays']"
    inp_holding_days_disabled = "//input[@name='HoldingDays' and @disabled]"
    lbl_holding_days = "//label[@class='text-content mb-0 ms-2' and text()='(days)']"
    
    # ========== QUOTA SECTION ==========
    # Quota section - STABLE by for attribute and content
    lbl_quota = "//label[@for='IsQuota' and contains(@class, 'col-form-label')]"
    lbl_quota_text = "//label[contains(., 'Quota')]"
    span_info_quota = "//label[@for='IsQuota']//span[@class='ml-1 oi icon-info']"
    chk_quota = "//input[@type='checkbox' and @name='IsQuota']"
    inp_quota_players = "//input[@id='Quota' and @name='Quota']"
    inp_quota_disabled = "//input[@name='Quota' and @disabled]"
    lbl_players = "//label[@class='text-content mb-0 ms-2' and text()='(players)']"
    
    # ========== INSTANT PAYMENT ==========
    # Instant Payment section - STABLE by for attribute and content
    lbl_instant_payment = "//label[@for='IsInstant' and contains(@class, 'col-form-label')]"
    lbl_instant_text = "//label[contains(., 'Instant Payment')]"
    span_info_instant = "//label[@for='IsInstant']//span[@class='ml-1 oi icon-info']"
    chk_instant_payment = "//input[@type='checkbox' and @name='IsInstant']"
    chk_instant_disabled = "//input[@name='IsInstant' and @disabled]"
    
    # ========== TIER SETTING SECTION ==========
    # Tier Setting fieldset - STABLE by class and content
    fieldset_tier_setting = "//fieldset[@class='tier-setting-group']"
    legend_tier_setting = "//fieldset[@class='tier-setting-group']//legend"
    h6_tier_setting = "//h6[contains(., 'Tier Setting')]"
    
    # Product Groups section - STABLE by content
    p_product_groups = "//p[contains(., 'Product Groups')]"
    span_group_index = "//span[@class='group-index']"
    div_select_product = "//div[@class='select-product ']"
    
    # Product Groups multiple select - STABLE by ID and class  
    div_product_select = "//div[@id='multiple-select-2']"
    div_product_container = "//div[@class='multiple-select-container'][@id='multiple-select-2']"
    btn_product_dropdown = "//div[@id='multiple-select-2']//button[@class='multiple-select-default multiple-select-label']"
    btn_all_products = "//button[.//span[@title='All Products']]"
    span_product_text = "//span[@class='text-display'][@title='All Products']"
    
    # Product options - STABLE by ID pattern
    inp_product_search = "//div[@id='multiple-select-2']//input[@name='inputOption']"
    chk_product_all = "//input[@id='multiple-select-2-optionItemAll']"
    chk_ow_sports = "//input[@id='multiple-select-2-optionItem-0']"
    chk_ow_number_game = "//input[@id='multiple-select-2-optionItem-1']"
    
    # ========== TIER TABLE ==========
    # Tier table - STABLE by class and structure
    tbl_tier = "//table[@class='table table-bordered table-striped']"
    thead_tier = "//table[@class='table table-bordered table-striped']/thead"
    tbody_tier = "//table[@class='table table-bordered table-striped']/tbody"
    
    # Tier table headers - STABLE by text content and style
    th_tier = "//th[text()='Tier']"
    th_min_fdm = "//th[.//form[contains(., 'Min FDM')]]"
    th_min_total_deposit = "//th[.//form[contains(., 'Min Total Deposit')]]"
    th_min_turnover = "//th[.//form[contains(., 'Min Turnover')]]"
    th_cpa_amount = "//th[text()='CPA Amount']"
    th_action = "//th[text()='Action']"
    
    # Tier checkboxes in headers - STABLE by name attribute
    chk_min_fdm = "//input[@name='CheckedMinFdm']"
    chk_min_total_deposit = "//input[@name='CheckedMinTotalDeposit']"
    chk_min_turnover = "//input[@name='CheckedMinTurnover']"
    
    # ========== TIER ROW INPUTS ==========
    # Tier 1 row inputs - STABLE by ID and name pattern
    inp_tier1_min_fdm = "//input[@id='MinFdm1' and @name='MinFdm']"
    inp_tier1_min_fdm_disabled = "//input[@name='MinFdm' and @disabled]"
    inp_tier1_total_deposit = "//input[@id='MinTotalDeposit1' and @name='MinTotalDeposit']"
    inp_tier1_total_deposit_disabled = "//input[@name='MinTotalDeposit' and @disabled]"
    inp_tier1_turnover = "//input[@id='MinTO1' and @name='MinTO']"
    inp_tier1_cpa_amount = "//input[@id='CpaAmount1' and @name='CpaAmount']"
    
    # Tier action buttons - STABLE by class and text
    btn_tier_add = "//button[@class='btn btn-tier' and text()='+']"
    btn_tier_add_plus = "//button[@class='btn btn-action' and text()='Add +']"
    
    # ========== MODAL ACTION BUTTONS ==========
    # Save and Cancel buttons - STABLE by class and text
    btn_save = "//button[@type='button' and contains(@class, 'btn-save') and text()='SAVE']"
    btn_save_by_class = "//button[@class='my-2 btn btn-success btn-save btn btn-secondary']"
    btn_cancel = "//button[@type='button' and contains(@class, 'btn-info') and text()='CANCEL']"
    btn_cancel_by_class = "//button[@class='my-2 btn btn-info btn btn-secondary']"
    
    # ========== NOTE SECTION ==========
    # Revenue Share note - STABLE by text content and class
    p_revenue_note = "//p[@class='text-danger my-2']"
    p_note_text = "//p[contains(., 'Revenue Share change will take effect')]"
    
    # ========== DYNAMIC HELPER METHODS ==========
    @staticmethod
    def get_deal_type_option_by_value(value):
        """Get deal type option by value in modal - STABLE"""
        return f"//div[@class='modal-content']//select[@name='DealType']/option[@value='{value}']"
    
    @staticmethod
    def get_deal_type_option_by_text(text):
        """Get deal type option by text in modal - STABLE"""
        return f"//div[@class='modal-content']//select[@name='DealType']/option[text()='{text}']"
    
    @staticmethod
    def get_fixed_rate_option_by_value(value):
        """Get fixed rate option by value - STABLE"""
        return f"//select[@name='SubCommRate']/option[@value='{value}']"
    
    @staticmethod
    def get_fixed_rate_option_by_percentage(percentage):
        """Get fixed rate option by percentage text - STABLE"""
        return f"//select[@name='SubCommRate']/option[text()='{percentage}']"
    
    @staticmethod
    def get_country_checkbox_by_index(index):
        """Get country checkbox by index - STABLE"""
        return f"//input[@id='multiple-select-1-optionItem-{index}']"
    
    @staticmethod
    def get_country_label_by_index(index):
        """Get country label by index - STABLE"""
        return f"//span[@for='multiple-select-1-optionItem-{index}']"
    
    @staticmethod
    def get_product_checkbox_by_index(index):
        """Get product checkbox by index - STABLE"""
        return f"//input[@id='multiple-select-2-optionItem-{index}']"
    
    @staticmethod
    def get_product_label_by_index(index):
        """Get product label by index - STABLE"""
        return f"//span[@for='multiple-select-2-optionItem-{index}']"
    
    @staticmethod
    def get_tier_input_by_tier_and_name(tier_number, input_name):
        """Get tier input by tier number and input name - STABLE"""
        return f"//input[@id='{input_name}{tier_number}' and @name='{input_name}']"
    
    @staticmethod
    def get_input_by_label_text(label_text):
        """Get input by associated label text - STABLE"""
        return f"//label[contains(., '{label_text}')]/..//input"
    
    @staticmethod
    def get_checkbox_by_label_text(label_text):
        """Get checkbox by associated label text - STABLE"""
        return f"//label[contains(., '{label_text}')]//input[@type='checkbox']"
    
    @staticmethod
    def get_select_by_label_text(label_text):
        """Get select by associated label text - STABLE"""
        return f"//label[contains(., '{label_text}')]/..//select"
    
    @staticmethod
    def get_button_by_text_in_modal(button_text):
        """Get button by text within modal - STABLE"""
        return f"//div[@class='modal-content']//button[text()='{button_text}']"
    
    @staticmethod
    def get_modal_input_by_name(input_name):
        """Get input by name within modal - STABLE"""
        return f"//div[@class='modal-content']//input[@name='{input_name}']"
    
    @staticmethod
    def get_modal_select_by_name(select_name):
        """Get select by name within modal - STABLE"""
        return f"//div[@class='modal-content']//select[@name='{select_name}']"
    
    # ========== MULTIPLE FALLBACK STRATEGIES ==========
    @staticmethod
    def get_modal_container_all_strategies():
        """Multiple strategies for modal container - HIGHEST RELIABILITY"""
        return [
            "//div[@class='modal fade show'][@role='dialog']",
            "//div[@class='modal-dialog deal-popup-container modal-lg']",
            "//div[@class='modal-content']",
            "//div[.//h5[contains(., 'Edit Deal')]]"
        ]
    
    @staticmethod
    def get_close_button_all_strategies():
        """Multiple strategies for close button - HIGHEST RELIABILITY"""
        return [
            "//button[@type='button' and @aria-label='Close']",
            "//button[@class='close']",
            "//span[@aria-hidden='true' and text()='×']",
            "//h5[contains(., 'Edit Deal')]/..//button[@aria-label='Close']"
        ]
    
    @staticmethod
    def get_save_button_all_strategies():
        """Multiple strategies for save button - HIGHEST RELIABILITY"""
        return [
            "//button[@type='button' and contains(@class, 'btn-save') and text()='SAVE']",
            "//button[@class='my-2 btn btn-success btn-save btn btn-secondary']",
            "//button[contains(., 'SAVE')]",
            "//div[@class='modal-content']//button[text()='SAVE']"
        ]
    
    @staticmethod
    def get_cancel_button_all_strategies():
        """Multiple strategies for cancel button - HIGHEST RELIABILITY"""
        return [
            "//button[@type='button' and contains(@class, 'btn-info') and text()='CANCEL']",
            "//button[@class='my-2 btn btn-info btn btn-secondary']",
            "//button[contains(., 'CANCEL')]",
            "//div[@class='modal-content']//button[text()='CANCEL']"
        ]
    
    @staticmethod
    def get_deal_name_input_all_strategies():
        """Multiple strategies for deal name input - HIGHEST RELIABILITY"""
        return [
            "//input[@id='DealName' and @name='DealName']",
            "//input[@name='DealName' and @class='form-control']",
            "//label[@for='DealName']/..//input[@type='text']",
            "//div[@class='modal-content']//input[@name='DealName']"
        ]
    
    @staticmethod
    def get_deal_types_select_all_strategies():
        """Multiple strategies for deal types select - HIGHEST RELIABILITY"""
        return [
            "//select[@id='DealType' and @name='DealType']",
            "//select[@name='DealType' and contains(@class, 'search-box')]",
            "//label[@for='DealType']/..//select",
            "//div[@class='modal-content']//select[@name='DealType']"
        ]
    
    @staticmethod
    def get_description_input_all_strategies():
        """Multiple strategies for description input - HIGHEST RELIABILITY"""
        return [
            "//input[@id='Description' and @name='Description']",
            "//input[@name='Description' and @class='form-control']",
            "//label[@for='Description']/..//input[@type='text']",
            "//div[@class='modal-content']//input[@name='Description']"
        ]
    
    @staticmethod
    def get_fixed_rate_select_all_strategies():
        """Multiple strategies for fixed rate select - HIGHEST RELIABILITY"""
        return [
            "//select[@id='SubCommRate' and @name='SubCommRate']",
            "//select[@name='SubCommRate' and @class='form-control form-control']",
            "//label[@for='SubCommRate']/..//select",
            "//div[@class='modal-content']//select[@name='SubCommRate']"
        ]
    
    @staticmethod
    def get_activity_period_input_all_strategies():
        """Multiple strategies for activity period input - HIGHEST RELIABILITY"""
        return [
            "//input[@id='ActiveDays' and @name='ActiveDays']",
            "//input[@name='ActiveDays' and @class='form-control']",
            "//label[@for='ActiveDays']/..//input[@type='text']",
            "//div[@class='modal-content']//input[@name='ActiveDays']"
        ]
    
    @staticmethod
    def verify_modal_loaded():
        """Verify modal is properly loaded - STABLE CHECK"""
        return [
            "//h5[contains(., 'Edit Deal')]",
            "//button[@type='button' and @aria-label='Close']",
            "//button[text()='SAVE']",
            "//button[text()='CANCEL']"
        ]
    
    @staticmethod
    def verify_modal_closed():
        """Verify modal is properly closed - STABLE CHECK"""
        return [
            "//div[@class='modal fade show'][@style='display: none;']",
            "//div[@class='modal-backdrop fade show'][@style='display: none;']"
        ] 