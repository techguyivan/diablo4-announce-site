from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.common.keys import Keys
from base.selenium_driver import SeleniumDriver
from base.basepage import BasePage
import utilities.custom_logger as cl
import logging

class IntroPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #LOCATORS

    introPlayIcon = "//*[@id='AppContainer']/div[5]/div/div[3]/div/div/button/div"
    introVideoIframe = "/html/body/div[2]/div/div[5]/div/div[5]/div[2]/div/iframe"
    d4BigLogo = "//*[@id='AppContainer']/div[5]/div/div[2]/div/div/div"
    returnToDarknessTitle = "//*[@id='AppContainer']/div[5]/div/div[2]/div/div/h3"

    #METHODS

    def clickIntroPlayIcon(self):
        self.waitForElement(self.introPlayIcon,locatorType="xpath")
        self.elementClick(self.introPlayIcon, locatorType="xpath")

    #VERIFICATION METHODS

    def verifyPlayIconVideo(self):
        self.introPage = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            if handle != self.introPage:
                self.introVideoIframe = handle
        self.waitForElement(self.introVideoIframe, locatorType="xpath")
        result = self.isElementDisplayed(self.introVideoIframe, locatorType="xpath")

        return result

    def verifyD4LogoDisplays(self):
        self.waitForElement(self.d4BigLogo, locatorType="xpath")
        result = self.isElementDisplayed(self.d4BigLogo, locatorType="xpath")

        return result

    def verifyRTDTitleDisplays(self):
        self.waitForElement(self.returnToDarknessTitle, locatorType="xpath")
        result = self.isElementDisplayed(self.returnToDarknessTitle, locatorType="xpath")

        return result