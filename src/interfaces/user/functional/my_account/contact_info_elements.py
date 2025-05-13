class ContactInfoElements:
    """
    Class containing XPath locators for the Contact Information section.
    These elements are for the contact details fields.
    """

    # Contact info group
    div_contact_info_group = "//div[@class='info-group'][.//span[text()='Contact Information']]"
    div_contact_title = "//div[@class='info-group'][.//span[text()='Contact Information']]/div[@class='title']"
    span_contact_title_text = "//div[@class='info-group'][.//span[text()='Contact Information']]//span[@class='text']"
    
    # Contact info fields
    div_form_horizontal_contact = "//div[@class='info-group'][.//span[text()='Contact Information']]/div[@class='form-horizontal']"
    
    # Gender field
    div_form_group_gender = "//div[@class='info-group'][.//span[text()='Contact Information']]//div[@class='form-group'][.//label[text()='Gender']]"
    label_gender = "//div[@class='info-group'][.//span[text()='Contact Information']]//label[text()='Gender']"
    label_radio_male = "//div[@class='info-group'][.//span[text()='Contact Information']]//label[contains(text(), 'Male')]"
    input_radio_male = "//div[@class='info-group'][.//span[text()='Contact Information']]//input[@id='male']"
    label_radio_female = "//div[@class='info-group'][.//span[text()='Contact Information']]//label[contains(text(), 'Female')]"
    input_radio_female = "//div[@class='info-group'][.//span[text()='Contact Information']]//input[@id='female']"
    
    # Address field
    div_form_group_address = "//div[@class='info-group'][.//span[text()='Contact Information']]//div[@class='form-group'][.//label[text()='Address']]"
    label_address = "//div[@class='info-group'][.//span[text()='Contact Information']]//label[text()='Address']"
    p_address_value = "//div[@class='info-group'][.//span[text()='Contact Information']]//label[text()='Address']/../../div[2]/p"
    
    # City field
    div_form_group_city = "//div[@class='info-group'][.//span[text()='Contact Information']]//div[@class='form-group'][.//label[text()='City']]"
    label_city = "//div[@class='info-group'][.//span[text()='Contact Information']]//label[text()='City']"
    p_city_value = "//div[@class='info-group'][.//span[text()='Contact Information']]//label[text()='City']/../../div[2]/p"
    
    # Postcode/Zip field
    div_form_group_postcode = "//div[@class='info-group'][.//span[text()='Contact Information']]//div[@class='form-group'][.//label[text()='Postcode/Zip']]"
    label_postcode = "//div[@class='info-group'][.//span[text()='Contact Information']]//label[text()='Postcode/Zip']"
    p_postcode_value = "//div[@class='info-group'][.//span[text()='Contact Information']]//label[text()='Postcode/Zip']/../../div[2]/p"
    
    # Country field
    div_form_group_country = "//div[@class='info-group'][.//span[text()='Contact Information']]//div[@class='form-group'][.//label[text()='Country']]"
    label_country = "//div[@class='info-group'][.//span[text()='Contact Information']]//label[text()='Country']"
    p_country_value = "//div[@class='info-group'][.//span[text()='Contact Information']]//label[text()='Country']/../../div[2]/p"
    
    # Email Address field
    div_form_group_email = "//div[@class='info-group'][.//span[text()='Contact Information']]//div[@class='form-group'][.//label[text()='Email Address']]"
    label_email = "//div[@class='info-group'][.//span[text()='Contact Information']]//label[text()='Email Address']"
    p_email_value = "//div[@class='info-group'][.//span[text()='Contact Information']]//label[text()='Email Address']/../../div[2]/p"
    
    # Contact Number field
    div_form_group_phone = "//div[@class='info-group'][.//span[text()='Contact Information']]//div[@class='form-group'][.//label[text()='Contact Number']]"
    label_phone = "//div[@class='info-group'][.//span[text()='Contact Information']]//label[text()='Contact Number']"
    input_phone = "//div[@class='info-group'][.//span[text()='Contact Information']]//input[@id='Phone']"
    span_validation_phone = "//span[@data-valmsg-for='Phone']"
    
    # MSN/YM/QQ field
    div_form_group_contact_app = "//div[@class='info-group'][.//span[text()='Contact Information']]//div[@class='form-group'][.//label[text()='MSN/YM/QQ']]"
    label_contact_app = "//div[@class='info-group'][.//span[text()='Contact Information']]//label[text()='MSN/YM/QQ']"
    input_contact_app_value = "//div[@class='info-group'][.//span[text()='Contact Information']]//input[@id='ContactAppList[0].Value']"
    span_validation_contact_app = "//span[@data-valmsg-for='ContactAppList[0].Value']"
    input_hidden_contact_app_name = "//input[@name='ContactAppList[0].Name']"
    input_hidden_contact_app_order = "//input[@name='ContactAppList[0].Order']"
    
    def get_contact_form_group_by_label(self, label_text):
        """Get contact form group by label text"""
        return f"//div[@class='info-group'][.//span[text()='Contact Information']]//div[@class='form-group'][.//label[text()='{label_text}']]"
    
    def get_contact_field_value_by_label(self, label_text):
        """Get contact field value by label text"""
        return f"//div[@class='info-group'][.//span[text()='Contact Information']]//div[@class='form-group'][.//label[text()='{label_text}']]/div[2]/p"
    
    def get_contact_input_by_label(self, label_text):
        """Get contact input field by label text"""
        return f"//div[@class='info-group'][.//span[text()='Contact Information']]//div[@class='form-group'][.//label[text()='{label_text}']]/div[2]/input" 