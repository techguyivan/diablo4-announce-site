from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.common.keys import Keys
from base.selenium_driver import SeleniumDriver
from base.basepage import BasePage
import utilities.custom_logger as cl
import logging

class WorldCarouselPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #LOCATORS

    worldSideNav = "//*[@id='AppContainer']/div[2]/div[2]/div[3]/a[4]"
    beholdTheWorldIcon = "//*[@id='AppContainer']/div[5]/div/div[2]/a/div/div/div/button/div"
    ###################################

    slideImage1 = "//*[@id='world0']/div/div[1]"
    slideImage2 = "//*[@id='world1']/div/div[1]"
    slideImage3 = "//*[@id='world2']/div/div[1]"
    slideImage4 = "//*[@id='world3']/div/div[1]"
    slideImage5 = "//*[@id='world4']/div/div[1]"
    slideImage6 = "//*[@id='world5']/div/div[1]"
    slideImage7 = "//*[@id='world6']/div/div[1]"
    slideImage8 = "//*[@id='world7']/div/div[1]"
    slideImage9 = "//*[@id='world8']/div/div[1]"
    slideImage10 = "//*[@id='world9']/div/div[1]"
    slideImage11 = "//*[@id='world10']/div/div[1]"
    slideImage12 = "//*[@id='world11']/div/div[1]"


    ###################################3
    slideLeftArrow1 = "//*[@id='world0']/div/div[1]/button[1]"
    slideRightArrow1 = "//*[@id='world0']/div/div[1]/button[2]"
    slideLeftArrow2 = "//*[@id='world1']/div/div[1]/button[1]"
    slideRightArrow2 = "//*[@id='world1']/div/div[1]/button[2]"
    slideLeftArrow3 = "//*[@id='world2']/div/div[1]/button[1]"
    slideRightArrow3 = "//*[@id='world2']/div/div[1]/button[2]"
    slideLeftArrow4 = "//*[@id='world3']/div/div[1]/button[1]"
    slideRightArrow4 = "//*[@id='world3']/div/div[1]/button[2]"
    slideLeftArrow5 = "//*[@id='world4']/div/div[1]/button[1]"
    slideRightArrow5 = "//*[@id='world4']/div/div[1]/button[2]"
    slideLeftArrow6 = "//*[@id='world5']/div/div[1]/button[1]"
    slideRightArrow6 = "//*[@id='world5']/div/div[1]/button[2]"
    slideLeftArrow7 = "//*[@id='world6']/div/div[1]/button[1]"
    slideRightArrow7 = "//*[@id='world6']/div/div[1]/button[2]"
    slideLeftArrow8 = "//*[@id='world7']/div/div[1]/button[1]"
    slideRightArrow8 = "//*[@id='world7']/div/div[1]/button[2]"
    slideLeftArrow9 = "//*[@id='world8']/div/div[1]/button[1]"
    slideRightArrow9 = "//*[@id='world8']/div/div[1]/button[2]"
    slideLeftArrow10 = "//*[@id='world9']/div/div[1]/button[1]"
    slideRightArrow10 = "//*[@id='world9']/div/div[1]/button[2]"
    slideLeftArrow11 = "//*[@id='world10']/div/div[1]/button[1]"
    slideRightArrow11 = "//*[@id='world10']/div/div[1]/button[2]"
    slideLeftArrow12 = "//*[@id='world11']/div/div[1]/button[1]"
    slideRightArrow12 = "//*[@id='world11']/div/div[1]/button[2]"

    ##################################
    slideButton1 = "world0"
    slideButton2 = "world1"
    slideButton3 = "world2"
    slideButton4 = "world3"
    slideButton5 = "world4"
    slideButton6 = "world5"
    slideButton7 = "world6"
    slideButton8 = "world7"
    slideButton9 = "world8"
    slideButton10 = "world9"
    slideButton11 = "world10"
    slideButton12 = "world11"

    ##################################

    slide1Heading = "//*[@id='world0']/div/div[2]/div/h3"
    slide2Heading = "//*[@id='world1']/div/div[2]/div/h3"
    slide3Heading = "//*[@id='world2']/div/div[2]/div/h3"
    slide4Heading = "//*[@id='world3']/div/div[2]/div/h3"
    slide5Heading = "//*[@id='world4']/div/div[2]/div/h3"
    slide6Heading = "//*[@id='world5']/div/div[2]/div/h3"
    slide7Heading = "//*[@id='world6']/div/div[2]/div/h3"
    slide8Heading = "//*[@id='world7']/div/div[2]/div/h3"
    slide9Heading = "//*[@id='world8']/div/div[2]/div/h3"
    slide10Heading = "//*[@id='world9']/div/div[2]/div/h3"
    slide11Heading = "//*[@id='world10']/div/div[2]/div/h3"
    slide12Heading = "//*[@id='world11']/div/div[2]/div/h3"

    # METHODS

    def clickWorldSideNav(self):
        self.waitForElement(self.worldSideNav, locatorType="xpath")
        self.elementClick(self.worldSideNav, locatorType="xpath")

    def clickBeholdWorldIcon(self):
        self.waitForElement(self.beholdTheWorldIcon, locatorType="xpath")
        self.elementClick(self.beholdTheWorldIcon, locatorType="xpath")

    def clickSlideButton1(self):
        self.waitForElement(self.slideButton1, locatorType="id")
        self.elementClick(self.slideButton1, locatorType="id")

    def clickSlideButton2(self):
        self.waitForElement(self.slideButton2, locatorType="id")
        self.elementClick(self.slideButton2, locatorType="id")

    def clickSlideButton3(self):
        self.waitForElement(self.slideButton3, locatorType="id")
        self.elementClick(self.slideButton3, locatorType="id")

    def clickSlideButton4(self):
        self.waitForElement(self.slideButton4, locatorType="id")
        self.elementClick(self.slideButton4, locatorType="id")

    def clickSlideButton5(self):
        self.waitForElement(self.slideButton5, locatorType="id")
        self.elementClick(self.slideButton5, locatorType="id")

    def clickSlideButton6(self):
        self.waitForElement(self.slideButton6, locatorType="id")
        self.elementClick(self.slideButton6, locatorType="id")

    def clickSlideButton7(self):
        self.waitForElement(self.slideButton7, locatorType="id")
        self.elementClick(self.slideButton7, locatorType="id")

    def clickSlideButton8(self):
        self.waitForElement(self.slideButton8, locatorType="id")
        self.elementClick(self.slideButton8, locatorType="id")

    def clickSlideButton9(self):
        self.waitForElement(self.slideButton9, locatorType="id")
        self.elementClick(self.slideButton9, locatorType="id")

    def clickSlideButton10(self):
        self.waitForElement(self.slideButton10, locatorType="id")
        self.elementClick(self.slideButton10, locatorType="id")

    def clickSlideButton11(self):
        self.waitForElement(self.slideButton11, locatorType="id")
        self.elementClick(self.slideButton11, locatorType="id")

    def clickSlideButton12(self):
        self.waitForElement(self.slideButton12, locatorType="id")
        self.elementClick(self.slideButton12, locatorType="id")


    # VERIFICATION METHODS

    # WORK ON SLIDE IMAGES
    ########################################

    def verifyWCSlide1Displays(self):
        self.waitForElement(self.slideImage1, locatorType="xpath")
        result = self.isElementDisplayed(self.slideImage1, locatorType="xpath")

        return result

    def verifyWCSlide2Displays(self):
        self.waitForElement(self.slideImage2, locatorType="xpath")
        result = self.isElementDisplayed(self.slideImage2, locatorType="xpath")

        return result

    def verifyWCSlide3Displays(self):
        self.waitForElement(self.slideImage3, locatorType="xpath")
        result = self.isElementDisplayed(self.slideImage3, locatorType="xpath")

        return result

    def verifyWCSlide4Displays(self):
        self.waitForElement(self.slideImage4, locatorType="xpath")
        result = self.isElementDisplayed(self.slideImage4, locatorType="xpath")

        return result

    def verifyWCSlide5Displays(self):
        self.waitForElement(self.slideImage5, locatorType="xpath")
        result = self.isElementDisplayed(self.slideImage5, locatorType="xpath")

        return result

    def verifyWCSlide6Displays(self):
        self.waitForElement(self.slideImage6, locatorType="xpath")
        result = self.isElementDisplayed(self.slideImage6, locatorType="xpath")

        return result

    def verifyWCSlide7Displays(self):
        self.waitForElement(self.slideImage7, locatorType="xpath")
        result = self.isElementDisplayed(self.slideImage7, locatorType="xpath")

        return result

    def verifyWCSlide8Displays(self):
        self.waitForElement(self.slideImage8, locatorType="xpath")
        result = self.isElementDisplayed(self.slideImage8, locatorType="xpath")

        return result

    def verifyWCSlide9Displays(self):
        self.waitForElement(self.slideImage9, locatorType="xpath")
        result = self.isElementDisplayed(self.slideImage9, locatorType="xpath")

        return result

    def verifyWCSlide10Displays(self):
        self.waitForElement(self.slideImage10, locatorType="xpath")
        result = self.isElementDisplayed(self.slideImage10, locatorType="xpath")

        return result

    def verifyWCSlide11Displays(self):
        self.waitForElement(self.slideImage11, locatorType="xpath")
        result = self.isElementDisplayed(self.slideImage11, locatorType="xpath")

        return result

    def verifyWCSlide12Displays(self):
        self.waitForElement(self.slideImage12, locatorType="xpath")
        result = self.isElementDisplayed(self.slideImage12, locatorType="xpath")

        return result


    ##########################

    def verifySlideLeftArrow1Displays(self):
        self.waitForElement(self.slideLeftArrow1, locatorType="xpath")
        result =  self.isElementDisplayed(self.slideLeftArrow1, locatorType="xpath")

        return result

    def verifySlideRightArrow1Displays(self):
        self.waitForElement(self.slideRightArrow1, locatorType="xpath")
        result =  self.isElementDisplayed(self.slideRightArrow1, locatorType="xpath")

        return result

    def verifySlideLeftArrow2Displays(self):
        self.waitForElement(self.slideLeftArrow2, locatorType="xpath")
        result = self.isElementDisplayed(self.slideLeftArrow2, locatorType="xpath")

        return result

    def verifySlideRightArrow2Displays(self):
        self.waitForElement(self.slideRightArrow2, locatorType="xpath")
        result = self.isElementDisplayed(self.slideRightArrow2, locatorType="xpath")

        return result

    def verifySlideLeftArrow3Displays(self):
        self.waitForElement(self.slideLeftArrow3, locatorType="xpath")
        result = self.isElementDisplayed(self.slideLeftArrow3, locatorType="xpath")

        return result

    def verifySlideRightArrow3Displays(self):
        self.waitForElement(self.slideRightArrow3, locatorType="xpath")
        result = self.isElementDisplayed(self.slideRightArrow3, locatorType="xpath")

        return result

    def verifySlideLeftArrow4Displays(self):
        self.waitForElement(self.slideLeftArrow4, locatorType="xpath")
        result = self.isElementDisplayed(self.slideLeftArrow4, locatorType="xpath")

        return result

    def verifySlideRightArrow4Displays(self):
        self.waitForElement(self.slideRightArrow4, locatorType="xpath")
        result = self.isElementDisplayed(self.slideRightArrow4, locatorType="xpath")

        return result

    def verifySlideLeftArrow5Displays(self):
        self.waitForElement(self.slideLeftArrow5, locatorType="xpath")
        result = self.isElementDisplayed(self.slideLeftArrow5, locatorType="xpath")

        return result

    def verifySlideRightArrow5Displays(self):
        self.waitForElement(self.slideRightArrow5, locatorType="xpath")
        result = self.isElementDisplayed(self.slideRightArrow5, locatorType="xpath")

        return result

    def verifySlideLeftArrow6Displays(self):
        self.waitForElement(self.slideLeftArrow6, locatorType="xpath")
        result = self.isElementDisplayed(self.slideLeftArrow6, locatorType="xpath")

        return result

    def verifySlideRightArrow6Displays(self):
        self.waitForElement(self.slideRightArrow6, locatorType="xpath")
        result = self.isElementDisplayed(self.slideRightArrow6, locatorType="xpath")

        return result

    def verifySlideLeftArrow7Displays(self):
        self.waitForElement(self.slideLeftArrow7, locatorType="xpath")
        result = self.isElementDisplayed(self.slideLeftArrow7, locatorType="xpath")

        return result

    def verifySlideRightArrow7Displays(self):
        self.waitForElement(self.slideRightArrow7, locatorType="xpath")
        result = self.isElementDisplayed(self.slideRightArrow7, locatorType="xpath")

        return result

    def verifySlideLeftArrow8Displays(self):
        self.waitForElement(self.slideLeftArrow8, locatorType="xpath")
        result = self.isElementDisplayed(self.slideLeftArrow8, locatorType="xpath")

        return result

    def verifySlideRightArrow8Displays(self):
        self.waitForElement(self.slideRightArrow8, locatorType="xpath")
        result = self.isElementDisplayed(self.slideRightArrow8, locatorType="xpath")

        return result

    def verifySlideLeftArrow9Displays(self):
        self.waitForElement(self.slideLeftArrow9, locatorType="xpath")
        result = self.isElementDisplayed(self.slideLeftArrow9, locatorType="xpath")

        return result

    def verifySlideRightArrow9Displays(self):
        self.waitForElement(self.slideRightArrow9, locatorType="xpath")
        result = self.isElementDisplayed(self.slideRightArrow9, locatorType="xpath")

        return result

    def verifySlideLeftArrow10Displays(self):
        self.waitForElement(self.slideLeftArrow10, locatorType="xpath")
        result = self.isElementDisplayed(self.slideLeftArrow10, locatorType="xpath")

        return result

    def verifySlideRightArrow10Displays(self):
        self.waitForElement(self.slideRightArrow10, locatorType="xpath")
        result = self.isElementDisplayed(self.slideRightArrow10, locatorType="xpath")

        return result

    def verifySlideLeftArrow11Displays(self):
        self.waitForElement(self.slideLeftArrow11, locatorType="xpath")
        result = self.isElementDisplayed(self.slideLeftArrow11, locatorType="xpath")

        return result

    def verifySlideRightArrow11Displays(self):
        self.waitForElement(self.slideRightArrow11, locatorType="xpath")
        result = self.isElementDisplayed(self.slideRightArrow11, locatorType="xpath")

        return result

    def verifySlideLeftArrow12Displays(self):
        self.waitForElement(self.slideLeftArrow12, locatorType="xpath")
        result = self.isElementDisplayed(self.slideLeftArrow12, locatorType="xpath")

        return result

    def verifySlideRightArrow12Displays(self):
        self.waitForElement(self.slideRightArrow12, locatorType="xpath")
        result = self.isElementDisplayed(self.slideRightArrow12, locatorType="xpath")

        return result


    #########################################

    def verifySlideButton1Displays(self):
        self.waitForElement(self.slideButton1, locatorType="id")
        result = self.isElementDisplayed(self.slideButton1, locatorType="id")

        return result

    def verifySlideButton2Displays(self):
        self.waitForElement(self.slideButton2, locatorType="id")
        result = self.isElementDisplayed(self.slideButton2, locatorType="id")

        return result

    def verifySlideButton3Displays(self):
        self.waitForElement(self.slideButton3, locatorType="id")
        result = self.isElementDisplayed(self.slideButton3, locatorType="id")

        return result

    def verifySlideButton4Displays(self):
        self.waitForElement(self.slideButton4, locatorType="id")
        result = self.isElementDisplayed(self.slideButton4, locatorType="id")

        return result

    def verifySlideButton5Displays(self):
        self.waitForElement(self.slideButton5, locatorType="id")
        result = self.isElementDisplayed(self.slideButton5, locatorType="id")

        return result

    def verifySlideButton6Displays(self):
        self.waitForElement(self.slideButton6, locatorType="id")
        result = self.isElementDisplayed(self.slideButton6, locatorType="id")

        return result

    def verifySlideButton7Displays(self):
        self.waitForElement(self.slideButton7, locatorType="id")
        result = self.isElementDisplayed(self.slideButton7, locatorType="id")

        return result

    def verifySlideButton8Displays(self):
        self.waitForElement(self.slideButton8, locatorType="id")
        result = self.isElementDisplayed(self.slideButton8, locatorType="id")

        return result

    def verifySlideButton9Displays(self):
        self.waitForElement(self.slideButton9, locatorType="id")
        result = self.isElementDisplayed(self.slideButton9, locatorType="id")

        return result

    def verifySlideButton10Displays(self):
        self.waitForElement(self.slideButton10, locatorType="id")
        result = self.isElementDisplayed(self.slideButton10, locatorType="id")

        return result

    def verifySlideButton11Displays(self):
        self.waitForElement(self.slideButton11, locatorType="id")
        result = self.isElementDisplayed(self.slideButton11, locatorType="id")

        return result

    def verifySlideButton12Displays(self):
        self.waitForElement(self.slideButton12, locatorType="id")
        result = self.isElementDisplayed(self.slideButton12, locatorType="id")

        return result

    ###########################

    def verifySlideHeading1Displays(self):
        self.waitForElement(self.slide1Heading, locatorType="xpath")
        result = self.isElementDisplayed(self.slide1Heading, locatorType="xpath")

        return result

    def verifySlideHeading2Displays(self):
        self.waitForElement(self.slide2Heading, locatorType="xpath")
        result = self.isElementDisplayed(self.slide2Heading, locatorType="xpath")

        return result

    def verifySlideHeading3Displays(self):
        self.waitForElement(self.slide3Heading, locatorType="xpath")
        result = self.isElementDisplayed(self.slide3Heading, locatorType="xpath")

        return result

    def verifySlideHeading4Displays(self):
        self.waitForElement(self.slide4Heading, locatorType="xpath")
        result = self.isElementDisplayed(self.slide4Heading, locatorType="xpath")

        return result

    def verifySlideHeading5Displays(self):
        self.waitForElement(self.slide5Heading, locatorType="xpath")
        result = self.isElementDisplayed(self.slide5Heading, locatorType="xpath")

        return result

    def verifySlideHeading6Displays(self):
        self.waitForElement(self.slide6Heading, locatorType="xpath")
        result = self.isElementDisplayed(self.slide6Heading, locatorType="xpath")

        return result

    def verifySlideHeading7Displays(self):
        self.waitForElement(self.slide7Heading, locatorType="xpath")
        result = self.isElementDisplayed(self.slide7Heading, locatorType="xpath")

        return result

    def verifySlideHeading8Displays(self):
        self.waitForElement(self.slide8Heading, locatorType="xpath")
        result = self.isElementDisplayed(self.slide8Heading, locatorType="xpath")

        return result

    def verifySlideHeading9Displays(self):
        self.waitForElement(self.slide9Heading, locatorType="xpath")
        result = self.isElementDisplayed(self.slide9Heading, locatorType="xpath")

        return result

    def verifySlideHeading10Displays(self):
        self.waitForElement(self.slide10Heading, locatorType="xpath")
        result = self.isElementDisplayed(self.slide10Heading, locatorType="xpath")

        return result

    def verifySlideHeading11Displays(self):
        self.waitForElement(self.slide11Heading, locatorType="xpath")
        result = self.isElementDisplayed(self.slide11Heading, locatorType="xpath")

        return result

    def verifySlideHeading12Displays(self):
        self.waitForElement(self.slide12Heading, locatorType="xpath")
        result = self.isElementDisplayed(self.slide12Heading, locatorType="xpath")

        return result





