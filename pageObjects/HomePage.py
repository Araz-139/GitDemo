
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pageObjects.CheckoutPage import CheckoutPage


class HomePage:
    #let's make a constructor
    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[text() = 'Shop']")
    name = (By.CSS_SELECTOR, "input[name = 'name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    check = (By.ID, "exampleCheck1")
    radio = (By.CSS_SELECTOR, "#inlineRadio1")
    dropdown = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type = 'submit']")
    alert_message = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()#* is added to read it as tuple
        #self.driver.find_element(By.XPATH, "//a[text() = 'Shop']").click()
        checkout_page = CheckoutPage(self.driver)
        return checkout_page

    def nameInput(self):
        return self.driver.find_element(*HomePage.name)


    def emailInput(self):
        return self.driver.find_element(*HomePage.email)

    def passwordInput(self):
        return self.driver.find_element(*HomePage.password)

    def checkClick(self):
        return self.driver.find_element(*HomePage.check)


    def radioClick(self):
        return self.driver.find_element(*HomePage.radio)

#I need to check the accuracy of this one...
    def dropdownSelect(self):
        return Select(self.driver.find_element(*HomePage.dropdown))


    def submitClick(self):
        return self.driver.find_element(*HomePage.submit)


    def alert_messageText(self):
        return self.driver.find_element(*HomePage.alert_message)

