import pytest

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