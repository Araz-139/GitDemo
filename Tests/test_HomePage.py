from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
import pytest
import time
from TestData.HomePageData import HomePageData



class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        # implicit wait is a global wait time applied to your script
        self.driver.implicitly_wait(5)  # will wait for a max of 5s for an element to show
        homePage = HomePage(self.driver)

        #input name
        homePage.nameInput().send_keys(getData["name"])
        #input email
        homePage.emailInput().send_keys(getData["email"])
        #input password
        homePage.passwordInput().send_keys("123456")
        #click check
        homePage.checkClick().click()
        #click radio
        homePage.radioClick().click()
        #select female from dropdown
        homePage.dropdownSelect().select_by_visible_text(getData["sex"])
        #click submit button
        homePage.submitClick().click()
        #get the alert message text in a var
        alert_text = homePage.alert_messageText().text #problem here!!
        assert "Success" in alert_text #there is a problem here!
        time.sleep(3) #just for debugging purposes

        self.driver.refresh()

    @pytest.fixture(params= HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param

        #these are replaced with the above ones...
        #driver.find_element(By.CSS_SELECTOR, "input[name = 'name']").send_keys("Araz")
        #driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
        #driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
        #driver.find_element(By.ID, "exampleCheck1").click()
        #driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
"""
        # Static dropdown
        dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
        dropdown.select_by_visible_text("Female")
"""
        #here selecting the 3rd instance of the given element
        #driver.find_element(By.XPATH, "//input[@type = 'submit']").click()
        #message = driver.find_element(By.CLASS_NAME, "alert-success").text
        #print(message)
        # let's use an assertion to check whether the test passes the assertion
