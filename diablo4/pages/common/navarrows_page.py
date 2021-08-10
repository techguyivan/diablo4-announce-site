from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.common.keys import Keys
from base.basepage import BasePage
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging

class NavArrowsPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #LOCATORS

    #introSideNav = "//*[@id='AppContainer']/div[2]/div[2]/div[3]/a[1]/div[3]"
    introDownArrow = "/html/body/div[2]/div/div[3]/div[2]/div/a"
    heroesOfSanctuaryHeading = "//*[@id='AppContainer']/div[5]/div/div[3]/div/div[1]/div/h2"

    #METHODS

    #def clickIntroSideNav(self):
        #self.waitForElement(self.introSideNav,locatorType="xpath")
        #self.elementClick(self.introSideNav, locatorType="xpath")

    def clickIntroDownArrow(self):
        self.waitForElement(self.introDownArrow,locatorType="xpath")
        self.elementClick(self.introDownArrow, locatorType="xpath")

    #VERIFICATION METHODS

    def verifyIntroDownArrowDisplays(self):
        self.waitForElement(self.introDownArrow, locatorType="xpath")
        result = self.isElementDisplayed(self.introDownArrow, locatorType="xpath")

        return result

    def verifyClassesHeadingDisplays(self):
        self.waitForElement(self.heroesOfSanctuaryHeading, locatorType="xpath")
        result = self.isElementDisplayed(self.heroesOfSanctuaryHeading, locatorType="xpath")

        return result