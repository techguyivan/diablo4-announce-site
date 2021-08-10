from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.classes.barbarian_class_page import ClassesPage
from utilities.teststatus import TestStatus
import time
import unittest
import pytest

# Run this test - pytest -s -v tests/common/barbarian_class_test.py

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestBarbarianClasses(unittest.TestCase):

    @pytest.fixture(autouse="True")
    def classSetup(self, oneTimeSetUp):
        self.cp = ClassesPage(self.driver)
        self.ts = TestStatus(self.driver)

    #Verify Barbarian Class Page

    @pytest.mark.run(order=1)
    def test_barbarianPageDisplays(self):
        self.cp.clickClassesSideNav()
        self.cp.clickBarbarianCrossIcon()
        result = self.cp.verifyBarbarianPageDisplays()
        self.ts.markFinal("test_barbarianPageDisplays", result, "Barbarian Class Page Displays")