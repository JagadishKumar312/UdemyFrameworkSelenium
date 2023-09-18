import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from Utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


class TestHomePage(BaseClass):

    def test_formSubmission(self, setup,getData):
        log=self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first name is"+getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        log.info("email is"+getData["email"])
        homepage.getEmail().send_keys(getData["email"])
        time.sleep(2)
        homepage.clickCheckbox().click()

        # Static dropdown
        log.info("selecting the gender")
        self.selectionbyOption(homepage.getGender(),getData["gender"])

        time.sleep(2)
        homepage.clickSubmitButton().click()

        alertmessage = homepage.getAlertmessage().text
        print(alertmessage)
        self.driver.refresh()

        time.sleep(3)

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param
