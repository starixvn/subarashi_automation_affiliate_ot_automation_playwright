"""
Media Gallery Elements

This file contains XPath locators for the media gallery elements on the Account Overview page.
"""

class MediaGalleryElements:
    """
    Class containing XPath locators for media gallery elements.
    """
    
    # Media gallery section container
    div_media_gallery_section = "//div[@id='media-gallery-section']"
    
    # Media gallery filters
    div_gallery_filters = "//div[@id='media-gallery-section']/div[@class='gallery-filters']"
    
    # Type filter
    div_type_filter = "//div[@class='gallery-filters']/div[@class='filter type']"
    select_type = "//div[@class='gallery-filters']/div[@class='filter type']/select[@id='media-type']"
    
    # Size filter
    div_size_filter = "//div[@class='gallery-filters']/div[@class='filter size']"
    select_size = "//div[@class='gallery-filters']/div[@class='filter size']/select[@id='media-size']"
    
    # Search filter
    div_search_filter = "//div[@class='gallery-filters']/div[@class='filter search']"
    input_search = "//div[@class='gallery-filters']/div[@class='filter search']/input[@id='media-search']"
    
    # Apply filter button
    div_apply_filter = "//div[@class='gallery-filters']/div[@class='filter apply']"
    button_apply = "//div[@class='gallery-filters']/div[@class='filter apply']/button[@id='btn-apply-filter']"
    
    # Media gallery grid
    div_gallery_grid = "//div[@id='media-gallery-section']/div[@class='gallery-grid']"
    
    # Media gallery items
    div_gallery_item = "//div[@class='gallery-grid']/div[@class='gallery-item']"
    img_thumbnail = "//div[@class='gallery-grid']/div[@class='gallery-item']/img[@class='thumbnail']"
    div_item_info = "//div[@class='gallery-grid']/div[@class='gallery-item']/div[@class='item-info']"
    p_item_name = "//div[@class='gallery-grid']/div[@class='gallery-item']/div[@class='item-info']/p[@class='name']"
    p_item_dimension = "//div[@class='gallery-grid']/div[@class='gallery-item']/div[@class='item-info']/p[@class='dimension']"
    
    # Download and preview buttons
    div_item_actions = "//div[@class='gallery-grid']/div[@class='gallery-item']/div[@class='item-actions']"
    button_download = "//div[@class='gallery-grid']/div[@class='gallery-item']/div[@class='item-actions']/button[@class='btn-download']"
    button_preview = "//div[@class='gallery-grid']/div[@class='gallery-item']/div[@class='item-actions']/button[@class='btn-preview']"
    
    # Pagination controls
    div_pagination = "//div[@id='media-gallery-section']/div[@class='pagination']"
    ul_pagination = "//div[@id='media-gallery-section']/div[@class='pagination']/ul[@class='pagination-list']"
    li_pagination_item = "//div[@id='media-gallery-section']/div[@class='pagination']/ul[@class='pagination-list']/li"
    li_previous = "//div[@id='media-gallery-section']/div[@class='pagination']/ul[@class='pagination-list']/li[@class='previous']"
    li_next = "//div[@id='media-gallery-section']/div[@class='pagination']/ul[@class='pagination-list']/li[@class='next']"
    
    # Preview modal
    div_preview_modal = "//div[@class='modal fade preview-modal']"
    div_modal_dialog = "//div[@class='modal fade preview-modal']/div[@class='modal-dialog']"
    div_modal_content = "//div[@class='modal fade preview-modal']/div[@class='modal-dialog']/div[@class='modal-content']"
    button_close_modal = "//div[@class='modal fade preview-modal']//button[@class='close']"
    img_preview_image = "//div[@class='modal fade preview-modal']//img[@class='preview-image']"
    
    # Select options helpers
    @staticmethod
    def get_type_option_by_value(value):
        """
        Get the XPath for a specific media type option by its value.
        
        Args:
            value (str): The value of the media type option (e.g., 'banner', 'logo', etc.).
            
        Returns:
            str: XPath locator for the specified media type option.
        """
        return f"//div[@class='filter type']/select[@id='media-type']/option[@value='{value}']"
    
    @staticmethod
    def get_size_option_by_value(value):
        """
        Get the XPath for a specific media size option by its value.
        
        Args:
            value (str): The value of the media size option (e.g., 'small', 'medium', 'large', etc.).
            
        Returns:
            str: XPath locator for the specified media size option.
        """
        return f"//div[@class='filter size']/select[@id='media-size']/option[@value='{value}']"
    
    @staticmethod
    def get_type_option_by_text(text):
        """
        Get the XPath for a specific media type option by its display text.
        
        Args:
            text (str): The display text of the media type option (e.g., 'Banner', 'Logo', etc.).
            
        Returns:
            str: XPath locator for the specified media type option.
        """
        return f"//div[@class='filter type']/select[@id='media-type']/option[text()='{text}']"
    
    @staticmethod
    def get_size_option_by_text(text):
        """
        Get the XPath for a specific media size option by its display text.
        
        Args:
            text (str): The display text of the media size option (e.g., 'Small', 'Medium', 'Large', etc.).
            
        Returns:
            str: XPath locator for the specified media size option.
        """
        return f"//div[@class='filter size']/select[@id='media-size']/option[text()='{text}']"
    
    @staticmethod
    def get_gallery_item_by_index(index=1):
        """
        Get the XPath for a specific gallery item by its index.
        
        Args:
            index (int): The index of the gallery item (1-based).
            
        Returns:
            str: XPath locator for the specified gallery item.
        """
        return f"(//div[@class='gallery-grid']/div[@class='gallery-item'])[{index}]"
    
    @staticmethod
    def get_pagination_item_by_number(number):
        """
        Get the XPath for a specific pagination item by its page number.
        
        Args:
            number (int): The page number.
            
        Returns:
            str: XPath locator for the specified pagination item.
        """
        return f"//div[@id='media-gallery-section']/div[@class='pagination']/ul[@class='pagination-list']/li/a[text()='{number}']" 