from selenium.webdriver.common.by import By


class ConfirmPage:
    txtbox_Country = (By.ID, "country")

    def __init__(self, driver):
        self.driver = driver

    def getCountryName(self):
        return self.driver.find_element(*ConfirmPage.txtbox_Country)

