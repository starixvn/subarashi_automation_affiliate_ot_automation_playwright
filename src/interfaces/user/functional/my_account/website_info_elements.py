class WebsiteInfoElements:
    """
    Class containing XPath locators for the Website Information section.
    These elements are for the website details fields.
    """

    # Website info group
    div_website_info_group = "//div[@class='info-group website-info']"
    div_website_title = "//div[@class='info-group website-info']/div[@class='title']"
    span_website_title_text = "//div[@class='info-group website-info']//span[@class='text']"
    
    # Website info fields
    div_form_horizontal_website = "//div[@class='info-group website-info']/div[@class='form-horizontal']"
    
    # Has website radio options
    div_form_group_has_website = "//div[@class='info-group website-info']//div[@class='form-group'][.//input[@id='hasWebSite']]"
    label_has_website = "//div[@class='info-group website-info']//label[contains(text(), 'I have my own website')]"
    input_has_website = "//div[@class='info-group website-info']//input[@id='hasWebSite']"
    
    # Website info container
    div_website_info = "//div[@id='websiteInfo']"
    
    # Website URL field
    div_form_group_site_url = "//div[@class='info-group website-info']//div[@class='form-group'][.//label[text()='Website URL']]"
    label_site_url = "//div[@class='info-group website-info']//label[@for='SiteUrl']"
    input_site_url = "//div[@class='info-group website-info']//input[@id='SiteUrl']"
    button_add_url = "//div[@class='info-group website-info']//button[@id='btnAddUrl']"
    span_glyphicon_plus = "//div[@class='info-group website-info']//span[@class='glyphicon glyphicon-plus']"
    span_validation_site_url = "//span[@data-valmsg-for='AccountInformation.SiteUrl']"
    
    # Hidden more site URLs
    input_more_site_urls = "//input[@id='MoreSiteUrls']"
    
    # Additional website URL fields
    div_form_group_more_url2 = "//div[@class='info-group website-info']//div[@class='form-group websiteInput'][.//label[text()='Website URL 2']]"
    label_more_url2 = "//div[@class='info-group website-info']//label[@for='MoreUrlInput2']"
    input_more_url2 = "//div[@class='info-group website-info']//input[@id='MoreUrlInput2']"
    button_delete_url2 = "//div[@class='info-group website-info']//div[@class='form-group websiteInput'][.//label[text()='Website URL 2']]//button[@class='btn btn-submit btnDeleteUrl']"
    span_glyphicon_minus2 = "//div[@class='info-group website-info']//div[@class='form-group websiteInput'][.//label[text()='Website URL 2']]//span[@class='glyphicon glyphicon-minus']"
    span_validation_more_url2 = "//span[@data-valmsg-for='MoreUrlInput2']"
    
    div_form_group_more_url3 = "//div[@class='info-group website-info']//div[@class='form-group websiteInput'][.//label[text()='Website URL 3']]"
    label_more_url3 = "//div[@class='info-group website-info']//label[@for='MoreUrlInput3']"
    input_more_url3 = "//div[@class='info-group website-info']//input[@id='MoreUrlInput3']"
    button_delete_url3 = "//div[@class='info-group website-info']//div[@class='form-group websiteInput'][.//label[text()='Website URL 3']]//button[@class='btn btn-submit btnDeleteUrl']"
    span_glyphicon_minus3 = "//div[@class='info-group website-info']//div[@class='form-group websiteInput'][.//label[text()='Website URL 3']]//span[@class='glyphicon glyphicon-minus']"
    span_validation_more_url3 = "//span[@data-valmsg-for='MoreUrlInput3']"
    
    # No website radio option
    div_form_group_no_website = "//div[@class='info-group website-info']//div[@class='form-group'][.//input[@id='hasNoWebSite']]"
    label_no_website = "//div[@class='info-group website-info']//label[contains(text(), 'I don't have a website')]"
    input_no_website = "//div[@class='info-group website-info']//input[@id='hasNoWebSite']"
    
    # Description for no website
    div_form_group_no_site_desc = "//div[@class='info-group website-info']//div[@class='form-group'][.//textarea[@id='NoSiteDesc']]"
    label_no_site_desc = "//div[@class='info-group website-info']//label[contains(text(), 'Please describe how you would like to promote 12Bet')]"
    textarea_no_site_desc = "//div[@class='info-group website-info']//textarea[@id='NoSiteDesc']"
    span_validation_no_site_desc = "//span[@data-valmsg-for='AccountInformation.NoSiteDesc']"
    
    def get_more_url_field_by_index(self, index):
        """Get additional website URL field by index (2-based, since first is SiteUrl)"""
        return f"//div[@class='info-group website-info']//input[@id='MoreUrlInput{index}']"
    
    def get_more_url_label_by_index(self, index):
        """Get additional website URL label by index (2-based, since first is SiteUrl)"""
        return f"//div[@class='info-group website-info']//label[@for='MoreUrlInput{index}']"
    
    def get_delete_url_button_by_index(self, index):
        """Get delete URL button by index (2-based, since first is SiteUrl)"""
        return f"//div[@class='info-group website-info']//div[@class='form-group websiteInput'][.//label[text()='Website URL {index}']]//button[@class='btn btn-submit btnDeleteUrl']" 