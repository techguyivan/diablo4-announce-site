from selenium import webdriver
from pages.agegate.age_page import AgePage
from base.selenium_driver import SeleniumDriver
from utilities.teststatus import TestStatus
import time
import unittest
import pytest

#Run this page -  pytest -s -v tests/common/age_test.py

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestAge(unittest.TestCase):

    @pytest.fixture(autouse="True")
    def classSetup(self, oneTimeSetUp):
        self.ap = AgePage(self.driver)
        self.ts = TestStatus(self.driver)


    #Verify An Invalid Age

    @pytest.mark.run(order=1)
    def test_invalidAge(self):
        self.driver.get("https://diablo4.blizzard.com")
        self.ap.inputAge(2, 0, 1, 5, 0, 4, 0, 3)
        result = self.ap.verifyAgeInvalid()
        self.ts.markFinal("test_invalidAge", result, "Invalid Age Verification")


    #Verify A Valid Age

    @pytest.mark.run(order=2)
    def test_validAge(self):
        self.ap.inputAge(1, 9, 8, 2, 0, 4, 0, 3)
        result = self.ap.verifyAgeValid()
        self.ts.markFinal("test_validAge", result, "Valid Age Verification")