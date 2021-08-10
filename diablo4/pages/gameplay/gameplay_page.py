from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.common.keys import Keys
from base.selenium_driver import SeleniumDriver
from base.basepage import BasePage
import utilities.custom_logger as cl
import logging

class GameplayPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #LOCATORS

    gameplaySideNav = "//*[@id='AppContainer']/div[2]/div[2]/div[3]/a[3]"
    abandonAllHopeHeading = "//*[@id='AppContainer']/div[5]/div/div/div[2]/div/div[1]"
    gamePlayFlavorText = "//*[@id='AppContainer']/div[5]/div/div/div[2]/div/div[2]/div"
    gamePlayPlayIcon = "//*[@id='AppContainer']/div[5]/div/div/div[5]/div/div/button/div"
    gamePlayVideoIframe = "/html/body/div[2]/div/div[5]/div/div/div[6]/div[2]/div/iframe"


    # METHODS

    def clickGameplaySideNav(self):
        self.waitForElement(self.gameplaySideNav, locatorType="xpath")
        self.elementClick(self.gameplaySideNav, locatorType="xpath")

    def clickGameplayPlayIcon(self):
        self.waitForElement(self.gamePlayPlayIcon, locatorType="xpath")
        self.elementClick(self.gamePlayPlayIcon, locatorType="xpath")

    # VERIFICATION METHODS

    def verifyAAHHeadingDisplays(self):
        self.waitForElement(self.abandonAllHopeHeading, locatorType="xpath")
        result = self.isElementDisplayed(self.abandonAllHopeHeading, locatorType="xpath")

        return result

    def verifyGameplayFlavorTextDisplays(self):
        self.waitForElement(self.gamePlayFlavorText, locatorType="xpath")
        result = self.isElementDisplayed(self.gamePlayFlavorText, locatorType="xpath")

        return result

    def verifyGameplayIconVideo(self):
        self.gamePlayPage = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            if handle != self.gamePlayPage:
                self.gamePlayVideoIframe = handle
        self.waitForElement(self.gamePlayVideoIframe, locatorType="xpath")
        result = self.isElementDisplayed(self.gamePlayVideoIframe, locatorType="xpath")

        return result
