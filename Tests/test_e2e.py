import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage



#@pytest.mark.usefixture("setup")
#let's instead inherit the BaseClass that is decorated with this usefixtures
class TestOne(BaseClass):
    def test_e2e(self):
        # implicit wait is a global wait time applied to your script
        self.driver.implicitly_wait(5)  # will wait for a max of 5s for an element to show
        #let's assign 'driver' to the HomePage class we will use
        #--> given we already created a constructor for it that can take the driver as arg
        homePage = HomePage(self.driver)
        #click the shop link to open the page
        #using the class obj from HomePage class
        checkout_page = homePage.shopItems()

        # get a list of the products then find Blackberry and add to the card
        # and add the Blackberry product
        cards = checkout_page.GetCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            card_text = card.text
            print(card_text)
            if card_text == "Blackberry":
                checkout_page.GetCardFooters()[i].click()

        # go to checkout
        checkout_page.GetCheckoutButton().click()
        #this will take us to the confirm page
        confirm_page = checkout_page.GetCheckoutButton2()

        # now we input in the dropdown input and check the box and purchase
        confirm_page.GetCountries().send_keys("ar")
        #self.driver.find_element(By.ID, "country").send_keys("ar")
        #wait = WebDriverWait(self.driver, 10)  # will wait max of 10 s until the element shows in this driver
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Armenia")))  # until Armenia appears
        self.VerifyLinkPresence("Armenia")
        confirm_page.GetArmenia().click()
        confirm_page.GetCheckbox().click()
        confirm_page.GetPurchase().click()
        success_text = confirm_page.GetSuccessText().text
        """
        self.driver.find_element(By.LINK_TEXT, "Armenia").click()
        self.driver.find_element(By.XPATH, "//div[@class = 'checkbox checkbox-primary']").click()
        self.driver.find_element(By.XPATH, "//input[@value= 'Purchase']").click()
        success_text = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        """
        # let's assert with partial text content
        assert "Fail" in success_text

print("the test is done - this line is for git tutorial")
print("another change made by the other guy to learn git - 2")
print("these are changes done to the branch")
