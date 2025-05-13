"""
Product Item Elements

This file contains XPath locators for the product item elements.
"""

class ProductItemElements:
    """
    Class containing XPath locators for product item elements.
    """
    
    @staticmethod
    def get_product_mask(product_id):
        """
        Returns XPath for the mask element within a specific product item
        
        Args:
            product_id: The ID of the product wrapper (e.g., 'Sports', 'LiveCasino')
        """
        return f"//div[@class='wrapper-items'][@id='{product_id}']/div[@class='page-container']/div[@class='items']/div[@class='mask']"
    
    @staticmethod
    def get_product_images(product_id):
        """
        Returns XPath for the images container within a specific product item
        
        Args:
            product_id: The ID of the product wrapper (e.g., 'Sports', 'LiveCasino')
        """
        return f"//div[@class='wrapper-items'][@id='{product_id}']/div[@class='page-container']/div[@class='items']/div[@class='mask']/div[@class='imgs']"
    
    @staticmethod
    def get_product_img_pc(product_id):
        """
        Returns XPath for the desktop image within a specific product item
        
        Args:
            product_id: The ID of the product wrapper (e.g., 'Sports', 'LiveCasino')
        """
        return f"//div[@class='wrapper-items'][@id='{product_id}']/div[@class='page-container']/div[@class='items']/div[@class='mask']/div[@class='imgs']/img[@class='show-pc']"
    
    @staticmethod
    def get_product_shape(product_id):
        """
        Returns XPath for the shape element within a specific product item
        
        Args:
            product_id: The ID of the product wrapper (e.g., 'Sports', 'LiveCasino')
        """
        shape_class = product_id.lower()
        if product_id == "LiveCasino":
            shape_class = "live-casino"
        elif product_id == "NumberGame":
            shape_class = "numbergame"
        
        return f"//div[@class='wrapper-items'][@id='{product_id}']/div[@class='page-container']/div[@class='items']/div[@class='mask']/div[@class='shape shape-{shape_class}']"
    
    @staticmethod
    def get_product_group_slider(product_id):
        """
        Returns XPath for the group slider element within a specific product item
        
        Args:
            product_id: The ID of the product wrapper (e.g., 'Sports', 'LiveCasino')
        """
        return f"//div[@class='wrapper-items'][@id='{product_id}']/div[@class='page-container']/div[@class='items']/div[@class='mask']/div[@class='group-slider']"
    
    @staticmethod
    def get_product_heading_slider_pc(product_id):
        """
        Returns XPath for the desktop heading slider element within a specific product item
        
        Args:
            product_id: The ID of the product wrapper (e.g., 'Sports', 'LiveCasino')
        """
        return f"//div[@class='wrapper-items'][@id='{product_id}']/div[@class='page-container']/div[@class='items']/div[@class='mask']/div[@class='group-slider']/div[@class='heading-slider show-pc']"
    
    @staticmethod
    def get_product_text_slider(product_id):
        """
        Returns XPath for the text slider element within a specific product item
        
        Args:
            product_id: The ID of the product wrapper (e.g., 'Sports', 'LiveCasino')
        """
        return f"//div[@class='wrapper-items'][@id='{product_id}']/div[@class='page-container']/div[@class='items']/div[@class='mask']/div[@class='group-slider']/div[@class='text-slider']"
    
    @staticmethod
    def get_product_img_mobile(product_id):
        """
        Returns XPath for the mobile image within a specific product item
        
        Args:
            product_id: The ID of the product wrapper (e.g., 'Sports', 'LiveCasino')
        """
        img_class = product_id.lower()
        if product_id == "LiveCasino":
            img_class = "live-casino"
        elif product_id == "NumberGame":
            img_class = "numbergame"
            
        return f"//div[@class='wrapper-items'][@id='{product_id}']/div[@class='page-container']/div[@class='items']/div[@class='mask']/div[@class='group-slider']/div[@class='text-slider']/img[@class='show-mobile img-{img_class}']"
    
    @staticmethod
    def get_product_text_heading(product_id):
        """
        Returns XPath for the text heading element within a specific product item
        
        Args:
            product_id: The ID of the product wrapper (e.g., 'Sports', 'LiveCasino')
        """
        return f"//div[@class='wrapper-items'][@id='{product_id}']/div[@class='page-container']/div[@class='items']/div[@class='mask']/div[@class='group-slider']/div[@class='text-slider']/div[@class='text-heading']"
    
    @staticmethod
    def get_product_heading_slider_mobile(product_id):
        """
        Returns XPath for the mobile heading slider element within a specific product item
        
        Args:
            product_id: The ID of the product wrapper (e.g., 'Sports', 'LiveCasino')
        """
        return f"//div[@class='wrapper-items'][@id='{product_id}']/div[@class='page-container']/div[@class='items']/div[@class='mask']/div[@class='group-slider']/div[@class='text-slider']/div[@class='text-heading']/div[@class='heading-slider show-mobile']"
    
    @staticmethod
    def get_product_swiper(product_id):
        """
        Returns XPath for the swiper element within a specific product item
        
        Args:
            product_id: The ID of the product wrapper (e.g., 'Sports', 'LiveCasino')
        """
        slider_type = "auto-slider"
        if product_id in ["Lottery", "Esports", "Keno", "P2P", "NumberGame"]:
            slider_type = "manual-slider"
            
        return f"//div[@class='wrapper-items'][@id='{product_id}']/div[@class='page-container']/div[@class='items']/div[@class='mask']/div[@class='group-slider']/div[@class='shape-slider']/div[@class='swiper products-slider {slider_type}']"
    
    @staticmethod
    def get_product_swiper_wrapper(product_id):
        """
        Returns XPath for the swiper wrapper element within a specific product item
        
        Args:
            product_id: The ID of the product wrapper (e.g., 'Sports', 'LiveCasino')
        """
        slider_type = "auto-slider"
        if product_id in ["Lottery", "Esports", "Keno", "P2P", "NumberGame"]:
            slider_type = "manual-slider"
            
        return f"//div[@class='wrapper-items'][@id='{product_id}']/div[@class='page-container']/div[@class='items']/div[@class='mask']/div[@class='group-slider']/div[@class='shape-slider']/div[@class='swiper products-slider {slider_type}']/div[@class='swiper-wrapper']"
    
    @staticmethod
    def get_product_swiper_slide(product_id, index=1):
        """
        Returns XPath for a specific swiper slide within a product item
        
        Args:
            product_id: The ID of the product wrapper (e.g., 'Sports', 'LiveCasino')
            index: The 1-based index of the slide
        """
        slider_type = "auto-slider"
        if product_id in ["Lottery", "Esports", "Keno", "P2P", "NumberGame"]:
            slider_type = "manual-slider"
            
        return f"//div[@class='wrapper-items'][@id='{product_id}']/div[@class='page-container']/div[@class='items']/div[@class='mask']/div[@class='group-slider']/div[@class='shape-slider']/div[@class='swiper products-slider {slider_type}']/div[@class='swiper-wrapper']/div[@class='swiper-slide'][{index}]"
    
    @staticmethod
    def get_product_arrow(product_id, arrow_num):
        """
        Returns XPath for a specific arrow within a product item
        
        Args:
            product_id: The ID of the product wrapper (e.g., 'Sports', 'LiveCasino')
            arrow_num: The arrow number (1-4)
        """
        return f"//div[@class='wrapper-items'][@id='{product_id}']/div[@class='page-container']/div[@class='items']/span[@class='products-arrow arrow-{arrow_num}']" 