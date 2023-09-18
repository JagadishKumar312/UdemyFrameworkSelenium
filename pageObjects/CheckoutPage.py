from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkoutbtn = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkoutbuttonscss = (By.CSS_SELECTOR, ".btn.btn-success")

    def __init__(self, driver):
        self.driver = driver

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def clickCheckoutbutton(self):
        return self.driver.find_element(*CheckoutPage.checkoutbtn)

    def clickbtnsuccess(self):
        self.driver.find_element(*CheckoutPage.checkoutbuttonscss).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage
