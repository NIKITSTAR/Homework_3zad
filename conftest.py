from selene import browser
import pytest

@pytest.fixture
def setup_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser

    browser.quit()