PLAYER_API = "/Admin/Player/GetData"

PLAYER_HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest"
}

PLAYER_REQUEST_TEMPLATE = {
    "AffName": "",
    "UserName": "",
    "IbcUserName": "",
    "IsIncludeRemovedPlayer": False,
    "PageIndex": 1,
    "PageSize": 100
} 