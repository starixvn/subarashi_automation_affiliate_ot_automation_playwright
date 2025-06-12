class MediaGalleryElements:
    
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