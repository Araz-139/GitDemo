import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By



@pytest.mark.usefixtures("setup")
class BaseClass:
    def VerifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 10)  # will wait max of 10 s until the element shows in this driver
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

