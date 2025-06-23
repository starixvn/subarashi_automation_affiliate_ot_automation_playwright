# AFF 12B Automation Framework

A comprehensive Python automation testing framework built with Playwright, designed for web UI testing, API testing, and database validation with integrated reporting capabilities.

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Framework Components](#framework-components)
- [Testing](#testing)
- [Reporting](#reporting)
- [Contributing](#contributing)

## 🎯 Overview

This automation framework provides a robust, scalable testing solution for the AFF 12BET platform. It supports multiple testing types including:

- **Web UI Automation** using Playwright
- **API Testing** with comprehensive request/response validation
- **Database Testing** with SQL Server integration
- **Multi-environment Support** (local, UAT, production)
- **Integrated Reporting** via Telegram, MS Teams, and Slack
- **Google Sheets Integration** for test result tracking

## ✨ Features

### Core Features
- **Multi-Browser Support**: Chrome, Firefox, Safari via Playwright
- **Headless/Headed Mode**: Configurable browser execution
- **Auto-retry Mechanisms**: Configurable retry logic with backoff
- **Performance Monitoring**: Execution time tracking and reporting
- **Comprehensive Logging**: Multi-level logging with file and console output
- **Error Handling**: Structured exception hierarchy with context
- **Test Tracing**: Playwright trace collection for debugging

### Testing Capabilities
- **UI Testing**: Element interactions, form filling, navigation
- **API Testing**: REST API validation with JSON/XML support
- **Database Testing**: SQL Server query execution and validation
- **Cross-Frame Testing**: iFrame and nested frame support
- **File Operations**: Upload/download testing, Excel processing
- **Screenshot Capture**: Automatic screenshot on failures

### Reporting & Integration
- **Multi-Channel Notifications**: Telegram, MS Teams, Slack
- **Google Sheets Integration**: Real-time test result updates
- **HTML Reports**: Detailed test execution reports
- **Duration Tracking**: Test execution time measurement
- **Failure Analytics**: Failed test case extraction and reporting

## 🚀 Installation

### Prerequisites
- Python 3.13+
- UV package manager

### Setup Instructions

1. **Clone the repository**
```bash
git clone <repository-url>
cd AFF_12B_Automation_Python_Playwright
```

2. **Install dependencies using UV**
```bash
# Install UV if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Sync project dependencies
uv sync
```

3. **Install Playwright browsers**
```bash
uv run playwright install
```

4. **Configure environment variables**
Create necessary configuration files in `config/secrets/` directory.

## ⚙️ Configuration

### Project Configuration (`pyproject.toml`)
```toml
[project]
name = "aff-12b-automation-python-playwright"
version = "0.1.0"
requires-python = ">=3.13"
dependencies = [
    "pytest",
    "playwright",
    "pandas",
    "pyodbc",
    # ... other dependencies
]
```

### Pytest Configuration (`pytest.ini`)
```ini
[pytest]
python_files = TestSuites_*.py
testpaths = test_suites
addopts = --cache-clear --html=reports/report.html --self-contained-html -v --capture=tee-sys
pythonpath = src .
```

### Application Settings (`config/constants/settings.py`)
Configure environments, credentials, and integration settings:

```python
ENVIRONMENT = 'local'  # local, uat, prod
SITE = 'admin'        # admin, user
BROWSER = 'chromium'   # chromium, firefox, webkit
HEADLESS_MODE = False
TIMEOUT = 30
```

### Command Line Options (`conftest.py`)
```bash
--env        # Environment (local/uat/prod)
--site       # Site type (admin/user)
--browser    # Browser choice
--headless   # Headless mode
--debug_mode # Debug mode
```

## 📖 Usage

### Running Tests

#### Basic Test Execution
```bash
# Run all tests
uv run pytest

# Run specific test suite
uv run pytest test_suites/functional_testing/

# Run with specific environment
uv run pytest --env=uat --site=admin --browser=chromium
```

#### Advanced Options
```bash
# Run in headless mode
uv run pytest --headless=true

# Run with debug mode
uv run pytest --debug_mode=true

# Run specific test file
uv run pytest test_suites/functional_testing/admin/TestSuites_01_Admin_Login.py
```

### Framework Usage Examples

#### UI Testing
```python
from src.utils.services.page_utils import ui
from src.utils.services.utils import utils

class TestExample:
    def setup_method(self):
        self.utils = utils(debug=False)
        self.utils.initialize_browser()
        self.page = self.utils.page
    
    def test_login(self):
        self.page.navigate("https://example.com")
        self.page.input("#username", "testuser")
        self.page.input("#password", "testpass")
        self.page.click("#login-button")
        self.page.verify_element_exist("#dashboard")
```

#### API Testing
```python
from src.utils.services.api_utils import api

class TestAPI:
    def setup_method(self):
        self.utils = utils(debug=False)
        self.utils.initialize_browser()
        self.api = self.utils.api
    
    def test_api_endpoint(self):
        response = self.api.get("https://api.example.com/users")
        self.api.assert_status_code(response, 200)
        data = self.api.extract_response_json(response)
        assert len(data) > 0
```

#### Database Testing
```python
from src.utils.services.db_utils import db

class TestDatabase:
    def setup_method(self):
        self.db = db()
        self.db.connect("server_name", "database_name")
    
    def test_data_validation(self):
        result = self.db.query("SELECT COUNT(*) FROM users")
        assert result[0][0] > 0
```

## 🧩 Framework Components

### Core Utilities (`src/utils/core/`)

#### Decorators (`decorators.py`)
- **`@retry`**: Automatic retry with exponential backoff
- **`@log_exceptions`**: Exception logging and handling
- **`@monitor_performance`**: Execution time monitoring
- **`@convert_exceptions`**: Exception type conversion

```python
@retry(max_attempts=3, delay_seconds=1.0)
@log_exceptions(log_level="ERROR")
@monitor_performance()
def example_function():
    # Your test logic here
    pass
```

#### Exception Handling (`exceptions.py`)
Comprehensive exception hierarchy:
- `AutomationException`: Base exception class
- `ValidationException`: Input validation errors
- `BrowserException`: Browser-related errors
- `ElementException`: Element interaction errors
- `APIException`: API testing errors
- `DatabaseException`: Database operation errors

#### Logging System (`logging.py`)
Multi-level logging with custom levels:
```python
from src.utils.core import get_logger

logger = get_logger(__name__)
logger.trace("Detailed trace information")
logger.debug("Debug information")
logger.info("General information")
logger.notice("Important notice")
logger.success("Success message")
logger.warning("Warning message")
logger.error("Error message")
```

#### Validation (`validation.py`)
Input validation utilities:
```python
from src.utils.core import validate_not_none, validate_type, validate_url

validate_not_none(value, "parameter_name")
validate_type(value, str, "parameter_name")
validate_url(url, "URL parameter")
```

### Service Components

#### API Utils (`src/utils/services/api_utils/`)
- **Request Methods**: GET, POST, PUT, DELETE operations
- **Assertion Methods**: Response validation and verification
- **Extraction Methods**: Data extraction from responses
- **JSONPath Support**: Complex data extraction

#### Database Utils (`src/utils/services/db_utils/`)
- **Connection Management**: SQL Server connections
- **Query Execution**: SELECT, INSERT, UPDATE, DELETE operations
- **Data Methods**: Bulk operations and data manipulation
- **Transaction Support**: Commit/rollback operations

#### Page Utils (`src/utils/services/page_utils/`)
- **Element Interactions**: Click, input, select operations
- **Navigation**: Page navigation and URL handling
- **Frame Support**: iFrame and nested frame operations
- **Verification**: Element existence and state validation
- **File Operations**: Upload/download functionality
- **Screenshot Capture**: Automated screenshot collection

#### General Utils (`src/utils/services/utils/`)
- **Browser Management**: Browser lifecycle management
- **File Operations**: Excel, JSON, and file processing
- **Google Sheets**: Integration for result tracking
- **Crypto Operations**: Encryption/decryption utilities
- **Reporting**: Multi-channel notification system

## 📊 Testing

### Test Structure
Tests follow the naming convention `TestSuites_*.py` and are organized by functionality:

```
test_suites/
├── functional_testing/
│   ├── admin/
│   └── common/
├── smoke_test/
└── jobs_execute/
```

### Test Execution Flow
1. **Setup**: Browser initialization, configuration loading
2. **Execution**: Test steps with automatic logging
3. **Validation**: Assertions and verifications
4. **Cleanup**: Resource cleanup and result reporting
5. **Reporting**: Multi-channel notifications

### Performance Monitoring
All test methods are automatically tracked for execution time:
```python
@measure_test_execution_time
def test_example(self):
    # Test implementation
    pass
```

## 📈 Reporting

### Supported Channels
- **Telegram**: Real-time notifications via bot
- **MS Teams**: Integration via webhook
- **Slack**: Channel-based reporting
- **Google Sheets**: Live test result updates
- **HTML Reports**: Detailed execution reports

### Report Content
- Test execution timestamp
- Environment and configuration details
- Pass/fail status with failure details
- Execution duration
- Failed test case listings
- Error details and stack traces

### Google Sheets Integration
Real-time test result tracking with:
- Test case status updates
- Execution duration recording
- Environment-specific results
- Historical tracking

## 🤝 Contributing

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Install development dependencies: `uv sync --group dev`
4. Make your changes
5. Run tests: `uv run pytest`
6. Submit a pull request

### Code Style
- Follow PEP 8 guidelines
- Use type hints where applicable
- Maintain comprehensive logging
- Include proper error handling
- Write descriptive docstrings

### Testing Guidelines
- All test files must follow `TestSuites_*.py` naming
- Use proper setup/teardown methods
- Include comprehensive assertions
- Add appropriate decorators for retry/logging
- Maintain test isolation

## 📝 License

This project is proprietary software for AFF 12BET automation testing.

## 🔧 Troubleshooting

### Common Issues

1. **Module Import Errors**
   - Ensure `pythonpath = src .` is in `pytest.ini`
   - Run `uv sync` to install dependencies

2. **Browser Launch Failures**
   - Install browsers: `uv run playwright install`
   - Check headless mode settings

3. **Database Connection Issues**
   - Verify SQL Server connectivity
   - Check credentials in settings

4. **Google Sheets Integration**
   - Ensure service account file exists
   - Verify sheet permissions

### Debug Mode
Enable debug mode for detailed logging:
```bash
uv run pytest --debug_mode=true
```

### Trace Collection
Enable trace collection for debugging:
```python
ENABLE_TRACE = True
TRACE_PATH = "Trace/trace.zip"
```

## 📞 Support

For support and questions, please contact the automation team or create an issue in the repository.

---

**Framework Version**: 0.1.0  
**Last Updated**: 2025-06-12  
**Python Version**: 3.13+  
**Playwright Version**: Latest