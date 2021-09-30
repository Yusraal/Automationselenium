import pytest
@pytest.mark.regeressiontest
def test_basicnavigation_amazon(browser):
    browser.get("https://www.amazon.com")
