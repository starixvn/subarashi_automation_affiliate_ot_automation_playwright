import pytest
import os

def pytest_addoption(parser):
    parser.addoption(
        '--env',
        action='store',
        default='local',
        help='Environment to run tests against (default: local)'
    )
    parser.addoption(
        '--site',
        action='store',
        default='admin',
        help='Site to run tests against (default: admin)'
    )
    parser.addoption(
        '--debug_mode',
        action='store',
        default='false',
        help='Enable debug mode (default: false)'
    )
    parser.addoption(
        '--headless',
        action='store',
        default='false',
        help='Run browser in headless mode (default: false)'
    )
    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        help='Browser to run tests with (default: chrome)'
    )

def pytest_configure(config):
    """Set environment variables based on command line options"""
    os.environ['PYTEST_ENV'] = config.getoption('--env')
    os.environ['PYTEST_SITE'] = config.getoption('--site')
    os.environ['PYTEST_DEBUG_MODE'] = config.getoption('--debug_mode')
    os.environ['PYTEST_HEADLESS'] = config.getoption('--headless')
    os.environ['PYTEST_BROWSER'] = config.getoption('--browser')
    
    # Debug output
    if config.getoption('--debug_mode').lower() == 'true':
        print(f"\n🚀 Test Configuration:")
        print(f"   Environment: {config.getoption('--env')}")
        print(f"   Site: {config.getoption('--site')}")
        print(f"   Headless: {config.getoption('--headless')}")
        print(f"   Browser: {config.getoption('--browser')}")
        print(f"   Debug Mode: {config.getoption('--debug_mode')}")

@pytest.fixture(scope="session")
def test_config(request):
    """Fixture to provide test configuration"""
    return {
        'env': request.config.getoption('--env'),
        'site': request.config.getoption('--site'),
        'debug_mode': request.config.getoption('--debug_mode'),
        'headless': request.config.getoption('--headless'),
        'browser': request.config.getoption('--browser')
    }