from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.classes.druid_class_page import ClassesPage
from utilities.teststatus import TestStatus
import time
import unittest
import pytest

# Run this page - pytest -s -v tests/common/druid_class_test.py

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestDruidClasses(unittest.TestCase):

    @pytest.fixture(autouse="True")
    def classSetup(self, oneTimeSetUp):
        self.cp = ClassesPage(self.driver)
        self.ts = TestStatus(self.driver)

    #Verify Druid Class Page

    @pytest.mark.run(order=1)
    def test_druidPageDisplays(self):
        self.cp.clickClassesSideNav()
        self.cp.clickDruidCrossIcon()
        result = self.cp.verifyDruidPageDisplays()
        self.ts.markFinal("test_druidPageDisplays", result, "Druid Class Page Displays")