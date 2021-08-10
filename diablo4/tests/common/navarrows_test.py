from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.common.navarrows_page import NavArrowsPage
from utilities.teststatus import TestStatus
import time
import unittest
import pytest

#Run this page -  pytest -s -v tests/common/navarrows_test.py

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestNavArrows(unittest.TestCase):

    @pytest.fixture(autouse="True")
    def classSetup(self, oneTimeSetUp):
        self.na = NavArrowsPage(self.driver)
        self.ts = TestStatus(self.driver)

    # Verify Intro Down Nav Arrow Displays

    #@pytest.mark.run(order="#")
    def test_introDownArrowDisplays(self):
        #self.na.clickIntroSideNav()
        result = self.na.verifyIntroDownArrowDisplays()
        self.ts.markFinal("test_introDownArrowDisplays", result, "Intro Down Arrow Displays")

    #WORK ON NAV ARROWS, FINDING THE CLICK ELEMENT IS THE ISSUE
    # Verify Intro Down Nav Arrow Navigates To Classes Page

    # @pytest.mark.run(order="#")
    def test_introDownArrowNavsToClasses(self):
        #self.na.clickIntroSideNav()
        self.na.clickIntroDownArrow()
        result = self.na.verifyClassesHeadingDisplays()
        self.ts.markFinal("test_introDownArrowNavsToClasses", result, "Intro Down Arrow Navs to Classes Page")
