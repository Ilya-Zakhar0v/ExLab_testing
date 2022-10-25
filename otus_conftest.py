import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
    parser.addoption("--url", "-U", action="store", default="http://test.exlab.team/", help="choose your browser")


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request, url):
    """ Фикстура инициализации браузера """
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        browser = webdriver.Chrome()
    elif browser == "firefox":
        browser = webdriver.Firefox()
    elif browser == "safari":
        browser = webdriver.Safari()
    else:
        raise Exception(f"{request.param} is not supported!")
    browser.implicitly_wait(5)
    request.addfinalizer(browser.close)

    def open(path=""):
        return browser.get(url + path)
    browser.open = open
    browser.open()
    return browser