from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.world.world_carousel_page import WorldCarouselPage
from utilities.teststatus import TestStatus
import time
import unittest
import pytest

#Run this page -  pytest -s -v tests/common/world_carousel_test.py

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestWorldCarousel(unittest.TestCase):

    @pytest.fixture(autouse="True")
    def classSetup(self, oneTimeSetUp):
        self.wcp = WorldCarouselPage(self.driver)
        self.ts = TestStatus(self.driver)

    # Verify Slide 1 Displays
    #@pytest.mark.run(order=#)
    def test_Slide1Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton1()
        result = self.wcp.verifyWCSlide1Displays()
        self.ts.markFinal("test_Slide1Displays", result, "Slide 1 Displays")

    # Verify Slide 2 Displays
    # @pytest.mark.run(order=#)
    def test_Slide2Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton2()
        result = self.wcp.verifyWCSlide2Displays()
        self.ts.markFinal("test_Slide2Displays", result, "Slide 2 Displays")

    # Verify Slide 3 Displays
    # @pytest.mark.run(order=#)
    def test_Slide3Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton3()
        result = self.wcp.verifyWCSlide3Displays()
        self.ts.markFinal("test_Slide3Displays", result, "Slide 3 Displays")

    # Verify Slide 4 Displays
    # @pytest.mark.run(order=#)
    def test_Slide4Displays(self):
            self.wcp.clickWorldSideNav()
            self.wcp.clickBeholdWorldIcon()
            self.wcp.clickSlideButton4()
            result = self.wcp.verifyWCSlide4Displays()
            self.ts.markFinal("test_Slide4Displays", result, "Slide 4 Displays")

    # Verify Slide 5 Displays
    # @pytest.mark.run(order=#)
    def test_Slide5Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton5()
        result = self.wcp.verifyWCSlide5Displays()
        self.ts.markFinal("test_Slide5Displays", result, "Slide 5 Displays")

    # Verify Slide 6 Displays
    # @pytest.mark.run(order=#)
    def test_Slide6Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton6()
        result = self.wcp.verifyWCSlide6Displays()
        self.ts.markFinal("test_Slide6Displays", result, "Slide 6 Displays")

    # Verify Slide 7 Displays
    # @pytest.mark.run(order=#)
    def test_Slide7Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton7()
        result = self.wcp.verifyWCSlide7Displays()
        self.ts.markFinal("test_Slide7Displays", result, "Slide 7 Displays")

    # Verify Slide 8 Displays
    # @pytest.mark.run(order=#)
    def test_Slide8Displays(self):
            self.wcp.clickWorldSideNav()
            self.wcp.clickBeholdWorldIcon()
            self.wcp.clickSlideButton8()
            result = self.wcp.verifyWCSlide8Displays()
            self.ts.markFinal("test_Slide8Displays", result, "Slide 8 Displays")

    # Verify Slide 9 Displays
    # @pytest.mark.run(order=#)
    def test_Slide9Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton9()
        result = self.wcp.verifyWCSlide9Displays()
        self.ts.markFinal("test_Slide9Displays", result, "Slide 9 Displays")

    # Verify Slide 10 Displays
    # @pytest.mark.run(order=#)
    def test_Slide10Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton10()
        result = self.wcp.verifyWCSlide10Displays()
        self.ts.markFinal("test_Slide10Displays", result, "Slide 10 Displays")

    # Verify Slide 11 Displays
    # @pytest.mark.run(order=#)
    def test_Slide11Displays(self):
            self.wcp.clickWorldSideNav()
            self.wcp.clickBeholdWorldIcon()
            self.wcp.clickSlideButton11()
            result = self.wcp.verifyWCSlide11Displays()
            self.ts.markFinal("test_Slide11Displays", result, "Slide 11 Displays")

    # Verify Slide 12 Displays
    # @pytest.mark.run(order=#)
    def test_Slide12Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton12()
        result = self.wcp.verifyWCSlide12Displays()
        self.ts.markFinal("test_Slide12Displays", result, "Slide 12 Displays")


    ###################################

    #Verify Slide Left Arrow 1 Displays

    #@pytest.mark.run(order=1)
    def test_SlideLeftArrow1Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton1()
        result = self.wcp.verifySlideLeftArrow1Displays()
        self.ts.markFinal("test_SlideLeftArrow1Displays", result, "Slide Left Arrow 1 Displays")

    #Verify Slide Right Arrow 1 Displays

    #@pytest.mark.run(order=2)
    def test_SlideRightArrow1Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton1()
        result = self.wcp.verifySlideRightArrow1Displays()
        self.ts.markFinal("test_SlideRightArrow1Displays", result, "Slide Right Arrow 1 Displays")

    # Verify Slide Left Arrow 2 Displays

    #@pytest.mark.run(order=3)
    def test_SlideLeftArrow2Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton2()
        result = self.wcp.verifySlideLeftArrow2Displays()
        self.ts.markFinal("test_SlideLeftArrow2Displays", result, "Slide Left Arrow 2 Displays")

    # Verify Slide Right Arrow 2 Displays

    # @pytest.mark.run(order=3)
    def test_SlideRightArrow2Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton2()
        result = self.wcp.verifySlideRightArrow2Displays()
        self.ts.markFinal("test_SlideRightArrow2Displays", result, "Slide Right Arrow 2 Displays")

    # Verify Slide Left Arrow 3 Displays

    # @pytest.mark.run(order=3)
    def test_SlideLeftArrow3Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton3()
        result = self.wcp.verifySlideLeftArrow3Displays()
        self.ts.markFinal("test_SlideLeftArrow3Displays", result, "Slide Left Arrow 3 Displays")

    # Verify Slide Right Arrow 3 Displays

    # @pytest.mark.run(order=3)
    def test_SlideRightArrow3Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton3()
        result = self.wcp.verifySlideRightArrow3Displays()
        self.ts.markFinal("test_SlideRightArrow3Displays", result, "Slide Right Arrow 3 Displays")

    # Verify Slide Left Arrow 4 Displays

    # @pytest.mark.run(order=3)
    def test_SlideLeftArrow4Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton4()
        result = self.wcp.verifySlideLeftArrow4Displays()
        self.ts.markFinal("test_SlideLeftArrow4Displays", result, "Slide Left Arrow 4 Displays")

    # Verify Slide Right Arrow 4 Displays

    # @pytest.mark.run(order=3)
    def test_SlideRightArrow4Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton4()
        result = self.wcp.verifySlideRightArrow4Displays()
        self.ts.markFinal("test_SlideRightArrow4Displays", result, "Slide Right Arrow 4 Displays")

    # Verify Slide Left Arrow 5 Displays

    # @pytest.mark.run(order=3)
    def test_SlideLeftArrow5Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton5()
        result = self.wcp.verifySlideLeftArrow5Displays()
        self.ts.markFinal("test_SlideLeftArrow5Displays", result, "Slide Left Arrow 5 Displays")

    # Verify Slide Right Arrow 5 Displays

    # @pytest.mark.run(order=3)
    def test_SlideRightArrow5Displays(self):
            self.wcp.clickWorldSideNav()
            self.wcp.clickBeholdWorldIcon()
            self.wcp.clickSlideButton5()
            result = self.wcp.verifySlideRightArrow5Displays()
            self.ts.markFinal("test_SlideRightArrow5Displays", result, "Slide Right Arrow 5 Displays")

    # Verify Slide Left Arrow 6 Displays

    # @pytest.mark.run(order=3)
    def test_SlideLeftArrow6Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton6()
        result = self.wcp.verifySlideLeftArrow6Displays()
        self.ts.markFinal("test_SlideLeftArrow6Displays", result, "Slide Left Arrow 6 Displays")

    # Verify Slide Right Arrow 6 Displays

    # @pytest.mark.run(order=3)
    def test_SlideRightArrow6Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton6()
        result = self.wcp.verifySlideRightArrow6Displays()
        self.ts.markFinal("test_SlideRightArrow6Displays", result, "Slide Right Arrow 6 Displays")

    # Verify Slide Left Arrow 7 Displays

    # @pytest.mark.run(order=3)
    def test_SlideLeftArrow7Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton7()
        result = self.wcp.verifySlideLeftArrow7Displays()
        self.ts.markFinal("test_SlideLeftArrow7Displays", result, "Slide Left Arrow 7 Displays")

    # Verify Slide Right Arrow 7 Displays

    # @pytest.mark.run(order=3)
    def test_SlideRightArrow7Displays(self):
            self.wcp.clickWorldSideNav()
            self.wcp.clickBeholdWorldIcon()
            self.wcp.clickSlideButton7()
            result = self.wcp.verifySlideRightArrow7Displays()
            self.ts.markFinal("test_SlideRightArrow7Displays", result, "Slide Right Arrow 7 Displays")

    # Verify Slide Left Arrow 8 Displays

    # @pytest.mark.run(order=3)

    def test_SlideLeftArrow8Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton8()
        result = self.wcp.verifySlideLeftArrow8Displays()
        self.ts.markFinal("test_SlideLeftArrow8Displays", result, "Slide Left Arrow 8 Displays")

    # Verify Slide Right Arrow 8 Displays

    # @pytest.mark.run(order=3)
    def test_SlideRightArrow8Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton8()
        result = self.wcp.verifySlideRightArrow8Displays()
        self.ts.markFinal("test_SlideRightArrow8Displays", result, "Slide Right Arrow 8 Displays")

    # Verify Slide Left Arrow 9 Displays

    # @pytest.mark.run(order=3)
    def test_SlideLeftArrow9Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton9()
        result = self.wcp.verifySlideLeftArrow9Displays()
        self.ts.markFinal("test_SlideLeftArrow9Displays", result, "Slide Left Arrow 9 Displays")

    # Verify Slide Right Arrow 9 Displays

    # @pytest.mark.run(order=3)
    def test_SlideRightArrow9Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton9()
        result = self.wcp.verifySlideRightArrow9Displays()
        self.ts.markFinal("test_SlideRightArrow9Displays", result, "Slide Right Arrow 9 Displays")

    # Verify Slide Left Arrow 10 Displays

    # @pytest.mark.run(order=3)
    def test_SlideLeftArrow10Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton10()
        result = self.wcp.verifySlideLeftArrow10Displays()
        self.ts.markFinal("test_SlideLeftArrow10Displays", result, "Slide Left Arrow 10 Displays")

    # Verify Slide Right Arrow 10 Displays

    # @pytest.mark.run(order=3)
    def test_SlideRightArrow10Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton10()
        result = self.wcp.verifySlideRightArrow10Displays()
        self.ts.markFinal("test_SlideRightArrow10Displays", result, "Slide Right Arrow 10 Displays")

    # Verify Slide Left Arrow 11 Displays

    # @pytest.mark.run(order=3)
    def test_SlideLeftArrow11Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton11()
        result = self.wcp.verifySlideLeftArrow11Displays()
        self.ts.markFinal("test_SlideLeftArrow11Displays", result, "Slide Left Arrow 11 Displays")

    # Verify Slide Right Arrow 11 Displays

    # @pytest.mark.run(order=3)
    def test_SlideRightArrow11Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton11()
        result = self.wcp.verifySlideRightArrow11Displays()
        self.ts.markFinal("test_SlideRightArrow11Displays", result, "Slide Right Arrow 11 Displays")

    # Verify Slide Left Arrow 12 Displays

    # @pytest.mark.run(order=3)
    def test_SlideLeftArrow12Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton12()
        result = self.wcp.verifySlideLeftArrow12Displays()
        self.ts.markFinal("test_SlideLeftArrow12Displays", result, "Slide Left Arrow 12 Displays")

    # Verify Slide Right Arrow 12 Displays

    # @pytest.mark.run(order=3)
    def test_SlideRightArrow12Displays(self):
            self.wcp.clickWorldSideNav()
            self.wcp.clickBeholdWorldIcon()
            self.wcp.clickSlideButton12()
            result = self.wcp.verifySlideRightArrow12Displays()
            self.ts.markFinal("test_SlideRightArrow12Displays", result, "Slide Right Arrow 12 Displays")

    #############################################

    # Verify Slide Button 1 displays
    #@pytest.mark.run(order=4)
    def test_SlideButton1Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        result = self.wcp.verifySlideButton1Displays()
        self.ts.markFinal("test_SlideButton1Displays", result, "Slide Button 1 Displays")

    # Verify Slide Button 2 displays
    #@pytest.mark.run(order=5)
    def test_SlideButton2Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        result = self.wcp.verifySlideButton2Displays()
        self.ts.markFinal("test_SlideButton2Displays", result, "Slide Button 2 Displays")

    # Verify Slide Button 3 displays
    #@pytest.mark.run(order=5)
    def test_SlideButton3Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        result = self.wcp.verifySlideButton3Displays()
        self.ts.markFinal("test_SlideButton3Displays", result, "Slide Button 3 Displays")

    # Verify Slide Button 4 displays
    #@pytest.mark.run(order=6)
    def test_SlideButton4Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        result = self.wcp.verifySlideButton4Displays()
        self.ts.markFinal("test_SlideButton4Displays", result, "Slide Button 4 Displays")

    # Verify Slide Button 5 displays
    #@pytest.mark.run(order=7)
    def test_SlideButton5Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        result = self.wcp.verifySlideButton5Displays()
        self.ts.markFinal("test_SlideButton5Displays", result, "Slide Button 5 Displays")

    # Verify Slide Button 6 displays
    #@pytest.mark.run(order=8)
    def test_SlideButton6Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        result = self.wcp.verifySlideButton6Displays()
        self.ts.markFinal("test_SlideButton6Displays", result, "Slide Button 6 Displays")

    # Verify Slide Button 7 displays
    #@pytest.mark.run(order=8)
    def test_SlideButton7Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        result = self.wcp.verifySlideButton7Displays()
        self.ts.markFinal("test_SlideButton7Displays", result, "Slide Button 7 Displays")

    # Verify Slide Button 8 displays
    #@pytest.mark.run(order=9)
    def test_SlideButton8Displays(self):
            self.wcp.clickWorldSideNav()
            self.wcp.clickBeholdWorldIcon()
            result = self.wcp.verifySlideButton8Displays()
            self.ts.markFinal("test_SlideButton8Displays", result, "Slide Button 8 Displays")

    # Verify Slide Button 9 displays
    #@pytest.mark.run(order=10)
    def test_SlideButton9Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        result = self.wcp.verifySlideButton9Displays()
        self.ts.markFinal("test_SlideButton9Displays", result, "Slide Button 9 Displays")

    # Verify Slide Button 10 displays
    #@pytest.mark.run(order=11)
    def test_SlideButton10Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        result = self.wcp.verifySlideButton10Displays()
        self.ts.markFinal("test_SlideButton10Displays", result, "Slide Button 10 Displays")

    # Verify Slide Button 11 displays
    #@pytest.mark.run(order=12)
    def test_SlideButton11Displays(self):
            self.wcp.clickWorldSideNav()
            self.wcp.clickBeholdWorldIcon()
            result = self.wcp.verifySlideButton11Displays()
            self.ts.markFinal("test_SlideButton11Displays", result, "Slide Button 11 Displays")

    # Verify Slide Button 12 displays
    #@pytest.mark.run(order=13)
    def test_SlideButton12Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        result = self.wcp.verifySlideButton12Displays()
        self.ts.markFinal("test_SlideButton12Displays", result, "Slide Button 12 Displays")

    #########################################

    #Verify Slide Heading 1 Displays
    #@pytest.mark.run(order=#)
    def test_SlideHeading1Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton1()
        result = self.wcp.verifySlideHeading1Displays()
        self.ts.markFinal("test_SlideHeading1Displays", result, "Slide Heading 1 Displays")

    #Verify Slide Heading 2 Displays
    #@pytest.mark.run(order=#)
    def test_SlideHeading2Displays(self):
            self.wcp.clickWorldSideNav()
            self.wcp.clickBeholdWorldIcon()
            self.wcp.clickSlideButton2()
            result = self.wcp.verifySlideHeading2Displays()
            self.ts.markFinal("test_SlideHeading2Displays", result, "Slide Heading 2 Displays")

    #Verify Slide Heading 3 Displays
    #@pytest.mark.run(order=#)

    def test_SlideHeading3Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton3()
        result = self.wcp.verifySlideHeading3Displays()
        self.ts.markFinal("test_SlideHeading3Displays", result, "Slide Heading 3 Displays")

    #Verify Slide Heading 4 Displays
    #@pytest.mark.run(order=#)

    def test_SlideHeading4Displays(self):
            self.wcp.clickWorldSideNav()
            self.wcp.clickBeholdWorldIcon()
            self.wcp.clickSlideButton4()
            result = self.wcp.verifySlideHeading4Displays()
            self.ts.markFinal("test_SlideHeading4Displays", result, "Slide Heading 4 Displays")

    #Verify Slide Heading 5 Displays
    #@pytest.mark.run(order=#)

    def test_SlideHeading5Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton5()
        result = self.wcp.verifySlideHeading5Displays()
        self.ts.markFinal("test_SlideHeading5Displays", result, "Slide Heading 5 Displays")

    #Verify Slide Heading 6 Displays
    #@pytest.mark.run(order=#)

    def test_SlideHeading6Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton6()
        result = self.wcp.verifySlideHeading6Displays()
        self.ts.markFinal("test_SlideHeading6Displays", result, "Slide Heading 6 Displays")

    #Verify Slide Heading 7 Displays
    #@pytest.mark.run(order=#)

    def test_SlideHeading7Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton7()
        result = self.wcp.verifySlideHeading7Displays()
        self.ts.markFinal("test_SlideHeading7Displays", result, "Slide Heading 7 Displays")

    #Verify Slide Heading 8 Displays
    #@pytest.mark.run(order=#)

    def test_SlideHeading8Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton8()
        result = self.wcp.verifySlideHeading8Displays()
        self.ts.markFinal("test_SlideHeading8Displays", result, "Slide Heading 8 Displays")

    # Verify Slide Heading 9 Displays
    # @pytest.mark.run(order=#)

    def test_SlideHeading9Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton9()
        result = self.wcp.verifySlideHeading9Displays()
        self.ts.markFinal("test_SlideHeading9Displays", result, "Slide Heading 9 Displays")

    #Verify Slide Heading 10 Displays
    #@pytest.mark.run(order=#)

    def test_SlideHeading10Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton10()
        result = self.wcp.verifySlideHeading10Displays()
        self.ts.markFinal("test_SlideHeading10Displays", result, "Slide Heading 10 Displays")

    #Verify Slide Heading 11 Displays
    #@pytest.mark.run(order=#)

    def test_SlideHeading11Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton11()
        result = self.wcp.verifySlideHeading11Displays()
        self.ts.markFinal("test_SlideHeading11Displays", result, "Slide Heading 11 Displays")

    #Verify Slide Heading 12 Displays
    #@pytest.mark.run(order=#)

    def test_SlideHeading12Displays(self):
        self.wcp.clickWorldSideNav()
        self.wcp.clickBeholdWorldIcon()
        self.wcp.clickSlideButton12()
        result = self.wcp.verifySlideHeading12Displays()
        self.ts.markFinal("test_SlideHeading12Displays", result, "Slide Heading 12 Displays")
