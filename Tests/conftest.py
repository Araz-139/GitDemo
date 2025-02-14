import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

driver = None

#this  is called hook: in order to pass browser options from cmd
#documentation: https://docs.pytest.org/en/stable/example/simple.html
#note that the command line key name can be customized
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: Chrome"
    )

@pytest.fixture(scope= "class")
def setup(request): #request is an instance of the fixture
    global driver #to use the global driver obj
    #let's pass the browser name as defined in cmd browser_name (options_
    browser_name = request.config.getoption("--browser_name")
    # based on the browser_name passed in cmd select and use the driver:
    if browser_name == "chrome":
        service_obj = Service(r"C:\Users\Araz_Markosian\bin\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "firefox":
        service_obj = Service(r"C:\Users\Araz_Markosian\bin\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    elif browser_name == "IE":
        service_obj = Service(r"C:\Users\Araz_Markosian\bin\msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
    #then use the driver obj to launch the website and maximize
    driver.get(r"https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver #driver will be sent to the cls(class) object
    #aka we have assigned the driver obj to the class var "request"
    #so we need to input request as argument in the functions defined in the cls obj
    #that will use the driver obj
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)




