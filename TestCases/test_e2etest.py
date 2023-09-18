import time
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.BaseClass import BaseClass
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage


class TestOne(BaseClass):

    def test_e2etesting(self, setup):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        checkOutPage = homepage.shopItems()
        log.info("getting all the card titles")
        # checkOutPage = CheckoutPage(self.driver)
        cards = checkOutPage.getCardTitles()

        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text

            # log.info(cardText)
            if cardText == "Blackberry":
                checkOutPage.getCardFooter()[i].click()
        time.sleep(2)

        checkOutPage.clickCheckoutbutton().click()
        time.sleep(2)

        confirmpage = checkOutPage.clickbtnsuccess()
        log.info("Entering country name as Ind")
        time.sleep(2)

        confirmpage.getCountryName().send_keys("Ind")
        time.sleep(2)
        self.verifyLinkPresence("India")

        # wait = WebDriverWait(self.driver, 10)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()

        # time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".checkbox.checkbox-primary").click()

        self.driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
        message = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
        print(message)
        # Success! The Form has been submitted successfully!.

        log.info("Text received from application is" + message)
        time.sleep(2)
