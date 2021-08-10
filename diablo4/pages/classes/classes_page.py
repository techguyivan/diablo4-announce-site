from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.common.keys import Keys
from base.selenium_driver import SeleniumDriver
from base.basepage import BasePage
import utilities.custom_logger as cl
import logging

class ClassesPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #LOCATORS

    classesSideNav = "//*[@id='AppContainer']/div[2]/div[2]/div[3]/a[2]"
    heroesOfSanctuaryHeading = "//*[@id='AppContainer']/div[5]/div/div[3]/div/div[1]/div/h2"
    classesSubHeadingText = "//*[@id='AppContainer']/div[5]/div/div[3]/div/div[2]/div"
    barbarianCrossIcon = "//*[@id='AppContainer']/div[5]/div/div[1]/div[4]/div/div[1]/button/div"
    sorceressCrossIcon = "//*[@id='AppContainer']/div[5]/div/div[1]/div[4]/div/div[2]/button/div"
    druidCrossIcon = "//*[@id='AppContainer']/div[5]/div/div[1]/div[4]/div/div[3]/button/div"

    #METHODS

    def clickClassesSideNav(self):
        self.waitForElement(self.classesSideNav,locatorType="xpath")
        self.elementClick(self.classesSideNav, locatorType="xpath")

    #VERIFICATION METHODS

    def verifyHOSHeadingDisplays(self):
        self.waitForElement(self.heroesOfSanctuaryHeading, locatorType = "xpath")
        result = self.isElementDisplayed(self.heroesOfSanctuaryHeading, locatorType="xpath")

        return result

    def verifySubHeadingTextDisplays(self):
        self.waitForElement(self.classesSubHeadingText, locatorType = "xpath")
        result = self.isElementDisplayed(self.classesSubHeadingText, locatorType = "xpath")

        return result

    def verifyBarbarianCrossIconDisplays(self):
        self.waitForElement(self.barbarianCrossIcon, locatorType ="xpath")
        result = self.isElementDisplayed(self.barbarianCrossIcon, locatorType="xpath")

        return result

    def verifySorceressCrossIconDisplays(self):
        self.waitForElement(self.sorceressCrossIcon, locatorType="xpath")
        result = self.isElementDisplayed(self.sorceressCrossIcon, locatorType="xpath")

        return result

    def verifyDruidCrossIconDisplays(self):
        self.waitForElement(self.druidCrossIcon, locatorType="xpath")
        result = self.isElementDisplayed(self.druidCrossIcon, locatorType="xpath")

        return result








