from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.classes.classes_page import ClassesPage
from utilities.teststatus import TestStatus
import time
import unittest
import pytest

# Run this page - pytest -s -v tests/common/classes_test.py

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestClasses(unittest.TestCase):

    @pytest.fixture(autouse="True")
    def classSetup(self, oneTimeSetUp):
        self.cp = ClassesPage(self.driver)
        self.ts = TestStatus(self.driver)

    # Verify Heroes of Sanctuary Heading Displays

    @pytest.mark.run(order=1)
    def test_HOSHeadingDisplays(self):
        self.cp.clickClassesSideNav()
        result = self.cp.verifyHOSHeadingDisplays()
        self.ts.markFinal("test_HOSHeadingDisplays", result, "Heroes of Sanctuary Title Label Displays")

    # Verify Heroes of Sanctuary Sub Heading Text Displays

    @pytest.mark.run(order=2)
    def test_HOSSubHeadingTextDisplays(self):
        self.cp.clickClassesSideNav()
        result = self.cp.verifySubHeadingTextDisplays()
        self.ts.markFinal("test_HOSSubHeadingTextDisplays", result, "Heroes of Sanctuary Sub Heading Text Displays")

    # Verify Barbarian Cross Icon Displays

    @pytest.mark.run(order=3)
    def test_barbarianCrossIconDisplays(self):
        self.cp.clickClassesSideNav()
        result = self.cp.verifyBarbarianCrossIconDisplays()
        self.ts.markFinal("test_barbarianCrossIconDisplays", result, "Barbarian Cross Icon Displays")

    # Verify Sorceress Cross Icon Displays

    @pytest.mark.run(order=4)
    def test_sorceressCrossIconDisplays(self):
        self.cp.clickClassesSideNav()
        result = self.cp.verifySorceressCrossIconDisplays()
        self.ts.markFinal("test_sorceressCrossIconDisplays", result, "Sorceress Cross Icon Displays")

    # Verify Druid Cross Icon Displays

    @pytest.mark.run(order=5)
    def test_druidCrossIconDisplays(self):
        self.cp.clickClassesSideNav()
        result = self.cp.verifyDruidCrossIconDisplays()
        self.ts.markFinal("test_druidCrossIconDisplays", result, "Druid Cross Icon Displays")
