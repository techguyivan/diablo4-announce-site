from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.common.keys import Keys
from base.selenium_driver import SeleniumDriver
from base.basepage import BasePage
import utilities.custom_logger as cl
import logging

class StoryCarouselPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #LOCATORS

    storyXClose = "//*[@id='story0']/div/div[2]/button"
    #######################################################################
    storySideNav = "//*[@id='AppContainer']/div[2]/div[2]/div[3]/a[5]"
    storyCrossIcon = "//*[@id='main-content']/div/div/a/div[3]/div/div/button"
    #######################################################################
    storyLeftArrow1 = "//*[@id='story0']/div/div[1]/button[1]"
    storyRightArrow1 = "//*[@id='story0']/div/div[1]/button[2]"
    storyLeftArrow2 = "//*[@id='story1']/div/div[1]/button[1]"
    storyRightArrow2 = "//*[@id='story1']/div/div[1]/button[2]"
    storyLeftArrow3 = "//*[@id='story2']/div/div[1]/button[1]"
    storyRightArrow3 = "//*[@id='story2']/div/div[1]/button[2]"
    storyLeftArrow4 = "//*[@id='story3']/div/div[1]/button[1]"
    storyRightArrow4 = "//*[@id='story3']/div/div[1]/button[2]"
    storyLeftArrow5 = "//*[@id='story4']/div/div[1]/button[1]"
    storyRightArrow5 = "//*[@id='story4']/div/div[1]/button[2]"
    ######################################################################
    storySlideImage1 = "//*[@id='story0']/div/div[1]"
    storySlideImage2 = "//*[@id='story1']/div/div[1]"
    storySlideImage3 = "//*[@id='story2']/div/div[1]"
    storySlideImage4 = "//*[@id='story3']/div/div[1]"
    storySlideImage5 = "//*[@id='story4']/div/div[1]"
    ######################################################################
    storySlideButton1 = "story0"
    storySlideButton2 = "story1"
    storySlideButton3 = "story2"
    storySlideButton4 = "story3"
    storySlideButton5 = "story4"
    ######################################################################
    storyHeading1 = "//*[@id='story0']/div/div[2]/div/h3"
    storyHeading2 = "//*[@id='story1']/div/div[2]/div/h3"
    storyHeading3 = "//*[@id='story2']/div/div[2]/div/h3"
    storyHeading4 = "//*[@id='story3']/div/div[2]/div/h3"
    storyHeading5 = "//*[@id='story4']/div/div[2]/div/h3"
    ######################################################################
    storyParagraph1 = "//*[@id='story0']/div/div[2]/div/p"
    storyParagraph2 = "//*[@id='story1']/div/div[2]/div/p"
    storyParagraph3 = "//*[@id='story2']/div/div[2]/div/p"
    storyParagraph4 = "//*[@id='story3']/div/div[2]/div/p"
    storyParagraph5 = "//*[@id='story4']/div/div[2]/div/p"
    ######################################################################



    #METHODS

    def clickStorySideNav(self):
        self.waitForElement(self.storySideNav, locatorType="xpath")
        self.elementClick(self.storySideNav, locatorType="xpath")

    def clickStoryCrossIcon(self):
        self.waitForElement(self.storyCrossIcon, locatorType="xpath")
        self.elementClick(self.storyCrossIcon, locatorType="xpath")

    def clickStoryXClose(self):
        self.waitForElement(self.storyXClose, locatorType="xpath")
        self.elementClick(self.storyXClose, locatorType="xpath")

    def clickSlideButton1(self):
        self.waitForElement(self.storySlideButton1, locatorType="id")
        self.elementClick(self.storySlideButton1, locatorType="id")

    def clickSlideButton2(self):
        self.waitForElement(self.storySlideButton2, locatorType="id")
        self.elementClick(self.storySlideButton2, locatorType="id")

    def clickSlideButton3(self):
        self.waitForElement(self.storySlideButton3, locatorType="id")
        self.elementClick(self.storySlideButton3, locatorType="id")

    def clickSlideButton4(self):
        self.waitForElement(self.storySlideButton4, locatorType="id")
        self.elementClick(self.storySlideButton4, locatorType="id")

    def clickSlideButton5(self):
        self.waitForElement(self.storySlideButton5, locatorType="id")
        self.elementClick(self.storySlideButton5, locatorType="id")



    #VERIFICATION METHODS

    def verifySlideStoryXDisplays(self):
        self.waitForElement(self.storyXClose, locatorType="xpath")
        result = self.isElementDisplayed(self.storyXClose, locatorType="xpath")

        return result

    def verifyStorySideNavDisplays(self):
        self.waitForElement(self.storySideNav, locatorType="xpath")
        result = self.isElementDisplayed(self.storySideNav, locatorType="xpath")

        return result

    def verifySlideLeftArrow1Displays(self):
        self.waitForElement(self.storyLeftArrow1, locatorType="xpath")
        result = self.isElementDisplayed(self.storyLeftArrow1, locatorType="xpath")

        return result

    def verifySlideRightArrow1Displays(self):
        self.waitForElement(self.storyRightArrow1, locatorType="xpath")
        result = self.isElementDisplayed(self.storyRightArrow1, locatorType="xpath")

        return result

    def verifySlideLeftArrow2Displays(self):
        self.waitForElement(self.storyLeftArrow2, locatorType="xpath")
        result = self.isElementDisplayed(self.storyLeftArrow2, locatorType="xpath")

        return result

    def verifySlideRightArrow2Displays(self):
        self.waitForElement(self.storyRightArrow2, locatorType="xpath")
        result = self.isElementDisplayed(self.storyRightArrow2, locatorType="xpath")

        return result

    def verifySlideLeftArrow3Displays(self):
        self.waitForElement(self.storyLeftArrow3, locatorType="xpath")
        result = self.isElementDisplayed(self.storyLeftArrow3, locatorType="xpath")

        return result

    def verifySlideRightArrow3Displays(self):
        self.waitForElement(self.storyRightArrow3, locatorType="xpath")
        result = self.isElementDisplayed(self.storyRightArrow3, locatorType="xpath")

        return result

    def verifySlideLeftArrow4Displays(self):
        self.waitForElement(self.storyLeftArrow4, locatorType="xpath")
        result = self.isElementDisplayed(self.storyLeftArrow4, locatorType="xpath")

        return result

    def verifySlideRightArrow4Displays(self):
        self.waitForElement(self.storyRightArrow4, locatorType="xpath")
        result = self.isElementDisplayed(self.storyRightArrow4, locatorType="xpath")

        return result

    def verifySlideLeftArrow5Displays(self):
        self.waitForElement(self.storyLeftArrow5, locatorType="xpath")
        result = self.isElementDisplayed(self.storyLeftArrow5, locatorType="xpath")

        return result

    def verifySlideRightArrow5Displays(self):
        self.waitForElement(self.storyRightArrow5, locatorType="xpath")
        result = self.isElementDisplayed(self.storyRightArrow5, locatorType="xpath")

        return result

    def verifyStorySlideImage1Displays(self):
        self.waitForElement(self.storySlideImage1, locatorType="xpath")
        result = self.isElementDisplayed(self.storySlideImage1, locatorType="xpath")

        return result

    def verifyStorySlideImage2Displays(self):
        self.waitForElement(self.storySlideImage2, locatorType="xpath")
        result = self.isElementDisplayed(self.storySlideImage2, locatorType="xpath")

        return result

    def verifyStorySlideImage3Displays(self):
        self.waitForElement(self.storySlideImage3, locatorType="xpath")
        result = self.isElementDisplayed(self.storySlideImage3, locatorType="xpath")

        return result

    def verifyStorySlideImage4Displays(self):
        self.waitForElement(self.storySlideImage4, locatorType="xpath")
        result = self.isElementDisplayed(self.storySlideImage4, locatorType="xpath")

        return result

    def verifyStorySlideImage5Displays(self):
        self.waitForElement(self.storySlideImage5, locatorType="xpath")
        result = self.isElementDisplayed(self.storySlideImage5, locatorType="xpath")

        return result

    def verifyStorySlideButton1Displays(self):
        self.waitForElement(self.storySlideButton1, locatorType="id")
        result = self.isElementDisplayed(self.storySlideButton1, locatorType="id")

        return result

    def verifyStorySlideButton2Displays(self):
        self.waitForElement(self.storySlideButton2, locatorType="id")
        result = self.isElementDisplayed(self.storySlideButton2, locatorType="id")

        return result

    def verifyStorySlideButton3Displays(self):
        self.waitForElement(self.storySlideButton3, locatorType="id")
        result = self.isElementDisplayed(self.storySlideButton3, locatorType="id")

        return result

    def verifyStorySlideButton4Displays(self):
        self.waitForElement(self.storySlideButton4, locatorType="id")
        result = self.isElementDisplayed(self.storySlideButton4, locatorType="id")

        return result

    def verifyStorySlideButton5Displays(self):
        self.waitForElement(self.storySlideButton5, locatorType="id")
        result = self.isElementDisplayed(self.storySlideButton5, locatorType="id")

        return result

    def verifyStoryHeading1Displays(self):
        self.waitForElement(self.storyHeading1, locatorType="xpath")
        result = self.isElementDisplayed(self.storyHeading1, locatorType="xpath")

        return result

    def verifyStoryHeading2Displays(self):
        self.waitForElement(self.storyHeading2, locatorType="xpath")
        result = self.isElementDisplayed(self.storyHeading2, locatorType="xpath")

        return result

    def verifyStoryHeading3Displays(self):
        self.waitForElement(self.storyHeading3, locatorType="xpath")
        result = self.isElementDisplayed(self.storyHeading3, locatorType="xpath")

        return result

    def verifyStoryHeading4Displays(self):
        self.waitForElement(self.storyHeading4, locatorType="xpath")
        result = self.isElementDisplayed(self.storyHeading4, locatorType="xpath")

        return result

    def verifyStoryHeading5Displays(self):
        self.waitForElement(self.storyHeading5, locatorType="xpath")
        result = self.isElementDisplayed(self.storyHeading5, locatorType="xpath")

        return result

    def verifyStoryParagraph1Displays(self):
        self.waitForElement(self.storyParagraph1, locatorType="xpath")
        result = self.isElementDisplayed(self.storyParagraph1, locatorType="xpath")

        return result

    def verifyStoryParagraph2Displays(self):
        self.waitForElement(self.storyParagraph2, locatorType="xpath")
        result = self.isElementDisplayed(self.storyParagraph2, locatorType="xpath")

        return result

    def verifyStoryParagraph3Displays(self):
        self.waitForElement(self.storyParagraph3, locatorType="xpath")
        result = self.isElementDisplayed(self.storyParagraph3, locatorType="xpath")

        return result

    def verifyStoryParagraph4Displays(self):
        self.waitForElement(self.storyParagraph4, locatorType="xpath")
        result = self.isElementDisplayed(self.storyParagraph4, locatorType="xpath")

        return result

    def verifyStoryParagraph5Displays(self):
        self.waitForElement(self.storyParagraph5, locatorType="xpath")
        result = self.isElementDisplayed(self.storyParagraph5, locatorType="xpath")

        return result











