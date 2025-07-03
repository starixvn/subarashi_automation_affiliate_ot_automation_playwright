from datetime import datetime

class DemoTestData:
    test_data = {
        "important": "Yes",
        "english": "test message English",
        "indonesian": "test message Indonesian",
        "korean": "test message Korean",
        "thai": "test message Thai",
        "vietnamese": "test message Vietnamese",
        "chinese": "test message Chinese",
    }
    # API request templates
    api_templates = {
        "create_message": {
            "method": "POST",
            "headers": {"content-type": "application/json"},
            "body": {
                "message": "test message",
                "priority": "high",
                "recipient": "all"
            }
        }
    }
    # Headers templates
    REQUIRED_HEADERS = {
        "content-type": "application/json;charset=UTF-8",
        "accept": "application/json, text/plain, */*"
    }

    @staticmethod
    def get_current_timestamp():
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    @classmethod
    def get_test_data(cls, scenario="default"):
        base_data = {
            "creator": "AAVictor",
            "created_date": cls.get_current_timestamp(),
            "message": "test message"
        }
        scenarios = {
            "urgent": {**base_data, "priority": "urgent", "important": "Yes"},
            "normal": {**base_data, "priority": "normal", "important": "No"}
        }
        return scenarios.get(scenario, base_data)