from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.classes.sorceress_class_page import ClassesPage
from utilities.teststatus import TestStatus
import time
import unittest
import pytest

# Run this page - pytest -s -v tests/common/sorceress_class_test.py

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestSorceressClasses(unittest.TestCase):

    @pytest.fixture(autouse="True")
    def classSetup(self, oneTimeSetUp):
        self.cp = ClassesPage(self.driver)
        self.ts = TestStatus(self.driver)

    #Verify Sorceress Class Page

    @pytest.mark.run(order=1)
    def test_sorceressPageDisplays(self):
        self.cp.clickClassesSideNav()
        self.cp.clickSorceressCrossIcon()
        result = self.cp.verifySorceressPageDisplays()
        self.ts.markFinal("test_sorceressPageDisplays", result, "Sorceress Class Page Displays")