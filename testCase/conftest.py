from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser")
    else:
        driver = webdriver.Ie()
        print("Launching IE browser")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

########## PyTest HTML Reports############


def pytest_configure(config):
    config._metadata['ProjectName'] = 'nopcommerce'
    config._metadata['ModuleName'] = 'Customers'
    config._metadata['Tester'] = 'Asha'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


