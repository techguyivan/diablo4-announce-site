from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.updates.updates_page import UpdatesPage
from utilities.teststatus import TestStatus
import time
import unittest
import pytest

#Run this page -  pytest -s -v tests/common/updates_test.py

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestUpdates(unittest.TestCase):

    @pytest.fixture(autouse="True")
    def classSetup(self, oneTimeSetUp):
        self.up = UpdatesPage(self.driver)
        self.ts = TestStatus(self.driver)

    # Verify Dev Updates Heading Displays
    #@pytest.mark.run(order=1)
    def test_DUHeadingDisplays(self):
        self.up.clickUpdatesSideNav()
        result = self.up.verifyDevUpdatesHeadingDisplays()
        self.ts.markFinal("test_DUHeadingDisplays", result, "Dev Updates Heading Displays")


    # Verify News Grid Displays
    #@pytest.mark.run(order=1)
    def test_NewsGridDisplays(self):
        self.up.clickUpdatesSideNav()
        result = self.up.verifyNewsGridDisplays()
        self.ts.markFinal("test_NewsGridDisplays", result, "News Grid Displays")


    # Verify More Updates Link Displays
    # @pytest.mark.run(order=1)
    def test_MoreUpdatesLinkDisplays(self):
        self.up.clickUpdatesSideNav()
        result = self.up.verifyMoreUpdatesLinkDisplays()
        self.ts.markFinal("test_MoreUpdatesLinkDisplays", result, "More Updates Link Displays")