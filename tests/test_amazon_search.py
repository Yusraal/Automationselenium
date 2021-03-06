import pytest

@pytest.mark.regressiontest
def test_amazon_search(browser):
    browser.get("https://www.amazon.com/")
    browser.find_element_by_id("twotabsearchtextbox").send_keys("Hello World")
    browser.find_element_by_id("nav-search-submit-button").click()
    assert browser.title()
