# Constants for Referrers API endpoints
REFERRERS_API = "/Admin/Portal/UserPanel/Referrers/GetReferrersList"
REFERRERS_DETAILS_API = "/Admin/Portal/UserPanel/Referrers/GetWebsiteUrlList"

# Device type mapping
DEVICE_TYPE_MAPPING = {
    "All": -1,
    "PC / Laptop": 1,
    "Mobile": 2
}

# Required headers for API requests
REFERRERS_REQUIRED_HEADERS = {
    "Content-Type": "application/json;charset=UTF-8",
    "Accept": "application/json, text/plain, */*",
    "X-Requested-With": "XMLHttpRequest"
}

# Request body template for referrers list
REFERRERS_REQUEST_BODY_TEMPLATE = {
    "deviceType": -1,
    "fromDate": None,
    "toDate": None,
    "affId": None
}

# Request body template for website URL details
REFERRERS_DETAILS_REQUEST_BODY_TEMPLATE = {
    "deviceType": -1,
    "fromDate": None,
    "toDate": None,
    "referrerUrl": None,
    "affId": None,
    "pageIndex": 1,
    "pageSize": 20
} 