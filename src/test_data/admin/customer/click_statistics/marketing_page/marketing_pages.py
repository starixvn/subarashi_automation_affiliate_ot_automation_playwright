# Constants for Marketing Pages API endpoints
MARKETING_PAGES_API = "/Admin/Portal/UserPanel/MarketingStatistics/GetMarketingStatisticsList"

# Required headers for API requests
MARKETING_PAGES_REQUIRED_HEADERS = {
    "Content-Type": "application/json;charset=UTF-8",
    "Accept": "application/json, text/plain, */*",
    "X-Requested-With": "XMLHttpRequest"
}

# Request body template for marketing pages list
MARKETING_PAGES_REQUEST_BODY_TEMPLATE = {
    "affId": None,
    "fromDate": None,
    "toDate": None,
    "languageCodes": "",
    "includedInActive": False
} 