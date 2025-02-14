from selenium.webdriver.common.by import By


class ConfirmPage:

    #define constructor and pass the driver obj
    def __init__(self, driver):
        self.driver = driver

    countries = (By.ID, "country")
    armenia = (By.LINK_TEXT, "Armenia")
    checkbox = (By.XPATH, "//div[@class = 'checkbox checkbox-primary']")
    purchase = (By.XPATH, "//input[@value= 'Purchase']")
    success_text = (By.CLASS_NAME, "alert-success")

    def GetCountries(self):
        return self.driver.find_element(*ConfirmPage.countries)

    def GetArmenia(self):
        return self.driver.find_element(*ConfirmPage.armenia)

    def GetCheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def GetPurchase(self):
        return self.driver.find_element(*ConfirmPage.purchase)

    def GetSuccessText(self):
        return self.driver.find_element(*ConfirmPage.success_text)

