from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options




@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        chr_option = Options()
        chr_option.add_experimental_option("detach", True)
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chr_option)
        print("Launching chrome browser.........")
    elif browser == 'edge':
        edge_option = Options()
        edge_option.add_experimental_option("detach", True)
        driver = webdriver.Edge(EdgeChromiumDriverManager().install(), options=edge_option)
        print("Launching Edge browser.........")
    else:
        chr_option = Options()
        chr_option.add_experimental_option("detach", True)
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chr_option)
        print("Launching chrome browser.........")
    return driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Smitha'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)





