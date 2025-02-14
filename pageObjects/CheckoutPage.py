from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import ConfirmPage

class CheckoutPage:

    #create the constructor and pass the driver obj to it
    def __init__(self, driver):
        self.driver = driver

    card_title = (By.XPATH, "//div[@class= 'card h-100']")
    card_footer = (By.XPATH, "//h4[@class= 'card-title']")
    checkout_button = (By.XPATH, "//a[@class = 'nav-link btn btn-primary']")
    checkout_button2 = (By.XPATH, "//button[@class = 'btn btn-success']")

    def GetCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.card_title)

    def GetCardFooters(self):
        return self.driver.find_elements(*CheckoutPage.card_footer)

    def GetCheckoutButton(self):
        return self.driver.find_element(*CheckoutPage.checkout_button)

    def GetCheckoutButton2(self):
        self.driver.find_element(*CheckoutPage.checkout_button2).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page