class SearchFormElements:
    
    # Main container elements
    div_search_form = "//div[@id='searchForm']"
    div_info_group = "//div[@id='searchForm' and @class='info-group']"
    div_title = "//div[@id='searchForm']//div[@class='title']"
    span_title_text = "//div[@id='searchForm']//div[@class='title']/span[@class='text']"

    # Search container
    div_search_container = "//div[@id='searchForm']//div[@class='search-container']"
    form_search = "//div[@id='searchForm']//form"

    # Form columns
    div_column_form_first = "//div[@id='searchForm']//form/div[@class='column-form'][1]"
    div_column_form_second = "//div[@id='searchForm']//form/div[@class='column-form'][2]"

    # Form groups in first column
    div_form_group_link_type = "//div[@id='searchForm']//div[contains(@class, 'form-group')][.//select[@id='AffLinkType']]"
    label_link_type = "//label[@for='AffLinkType']"
    select_link_type = "//select[@id='AffLinkType']"
    option_affiliate_link = "//select[@id='AffLinkType']/option[@value='AffiliateLink']"

    div_form_group_target_country = "//div[@id='searchForm']//div[contains(@class, 'form-group')][.//select[@id='TargetCountry']]"
    label_target_country = "//label[@for='TargetCountry']"
    select_target_country = "//select[@id='TargetCountry']"

    div_form_group_language = "//div[@id='searchForm']//div[contains(@class, 'form-group')][.//select[@id='Language']]"
    label_language = "//label[@for='Language']"
    select_language = "//select[@id='Language']"

    div_form_group_domain = "//div[@id='searchForm']//div[contains(@class, 'form-group')][.//select[@id='Domain']]"
    label_domain = "//label[@for='Domain']"
    select_domain = "//select[@id='Domain']"

    div_form_group_category = "//div[@id='searchForm']//div[contains(@class, 'form-group')][.//select[@id='Category']]"
    label_category = "//label[@for='Category']"
    select_category = "//select[@id='Category']"

    div_form_group_subcategory = "//div[@id='searchForm']//div[contains(@class, 'form-group')][.//select[@id='SubCategory']]"
    label_subcategory = "//label[@for='SubCategory']"
    select_subcategory = "//select[@id='SubCategory']"

    # Form groups in second column
    div_form_group_currency = "//div[@id='searchForm']//div[contains(@class, 'form-group')][.//select[@id='Currency']]"
    label_currency = "//label[@for='Currency']"
    select_currency = "//select[@id='Currency']"

    div_form_group_device = "//div[@id='searchForm']//div[contains(@class, 'form-group')][.//select[@id='DeviceType']]"
    label_device = "//div[@id='searchForm']//div[contains(@class, 'form-group')][.//select[@id='DeviceType']]//label"
    select_device = "//select[@id='DeviceType']"
    option_pc = "//select[@id='DeviceType']/option[@value='0']"
    option_mobile = "//select[@id='DeviceType']/option[@value='1']"

    div_form_group_media_size = "//div[@id='searchForm']//div[contains(@class, 'form-group')][.//select[@id='Size']]"
    label_media_size = "//label[@for='Size']"
    select_media_size = "//select[@id='Size']"

    div_form_group_page = "//div[@id='searchForm']//div[contains(@class, 'form-group')][.//select[@id='Page']]"
    label_page = "//label[@for='Page']"
    select_page = "//select[@id='Page']"

    div_form_group_channel = "//div[@id='searchForm']//div[contains(@class, 'form-group')][.//select[@id='Channel']]"
    label_channel = "//label[@for='Channel']"
    select_channel = "//select[@id='Channel']"

    # Generate button
    div_form_group_button = "//div[@id='searchForm']//div[contains(@class, 'form-group-button')]"
    button_generate = "//button[@id='btnMarketingSearch']"
