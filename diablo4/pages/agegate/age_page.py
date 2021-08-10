from selenium import webdriver
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
import time


class AgePage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #LOCATORS

    #Date Inputs

    _y1 = "year1"
    _y2 = "year2"
    _y3 = "year3"
    _y4 = "year4"
    _m1 = "month1"
    _m2 = "month2"
    _d1 = "day1"
    _d2 = "day2"

    #Access

    noAccessHeading = "//*[@id='AppContainer']/div[1]/div[2]/div/h2"
    d4BigLogo = "//*[@id='AppContainer']/div[5]/div/div[2]/div/div/div"


    #Input Methods

    def inputYear1(self, year1):
        self.sendKeys(year1, self._y1, locatorType="id")

    def inputYear2(self, year2):
        self.sendKeys(year2, self._y2, locatorType="id")

    def inputYear3(self, year3):
        self.sendKeys(year3, self._y3, locatorType="id")

    def inputYear4(self, year4):
        self.sendKeys(year4, self._y4, locatorType="id")

    def inputMonth1(self, month1):
        self.sendKeys(month1, self._m1, locatorType="id")

    def inputMonth2(self,month2):
        self.sendKeys(month2, self._m2, locatorType="id")

    def inputDay1(self,day1):
        self.sendKeys(day1, self._d1, locatorType="id")

    def inputDay2(self,day2):
        self.sendKeys(day2, self._d2, locatorType="id")


    def inputAge(self, year1="", year2="", year3="", year4="", month1="", month2="", day1="", day2=""):

        self.inputYear1(year1)
        self.inputYear2(year2)
        self.inputYear3(year3)
        self.inputYear4(year4)
        self.inputMonth1(month1)
        self.inputMonth2(month2)
        self.inputDay1(day1)
        self.inputDay2(day2)


    #Verification methods

    def verifyAgeInvalid(self):
        self.waitForElement(self.noAccessHeading, locatorType = "xpath")
        result = self.isElementDisplayed(self.noAccessHeading, locatorType = "xpath")

        return result

    def verifyAgeValid(self):
        self.waitForElement(self.d4BigLogo, locatorType="xpath")
        result = self.isElementDisplayed(self.d4BigLogo, locatorType="xpath")

        return result



