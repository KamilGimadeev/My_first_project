import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
site = 0
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='none',
                     help="Choose interface language")


@pytest.fixture(params = ["Chrome"])
def browser(request):
    language = request.config.getoption("language")
    brow = request.param
    if brow == "Chrome" :
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif brow == "Firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    yield browser
    browser.quit()
