import unittest
from tests.agegate.age_test import TestAge
from tests.introduction.intro_test import TestIntro
from tests.classes.classes_test import TestClasses
from tests.classes.barbarian_class_test import TestBarbarianClasses
from tests.classes.sorceress_class_test import TestSorceressClasses
from tests.classes.druid_class_test import TestDruidClasses
from tests.gameplay.gameplay_test import TestGameplay
from tests.world.world_test import TestWorld
from tests.world.world_carousel_test import TestWorldCarousel
from tests.story.story_test import TestStory
from tests.story.story_carousel_test import TestStoryCarousel
from tests.updates.updates_test import TestUpdates
from tests.signup.signup_test import TestSignUp

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestAge)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestIntro)
tc3 = unittest.TestLoader().loadTestsFromTestCase(TestClasses)
tc4 = unittest.TestLoader().loadTestsFromTestCase(TestBarbarianClasses)
tc5 = unittest.TestLoader().loadTestsFromTestCase(TestSorceressClasses)
tc6 = unittest.TestLoader().loadTestsFromTestCase(TestDruidClasses)
tc7 = unittest.TestLoader().loadTestsFromTestCase(TestGameplay)
tc8 = unittest.TestLoader().loadTestsFromTestCase(TestWorld)
tc9 = unittest.TestLoader().loadTestsFromTestCase(TestWorldCarousel)
tc10 = unittest.TestLoader().loadTestsFromTestCase(TestStory)
tc11 = unittest.TestLoader().loadTestsFromTestCase(TestStoryCarousel)
tc12 = unittest.TestLoader().loadTestsFromTestCase(TestUpdates)
tc13 = unittest.TestLoader().loadTestsFromTestCase(TestSignUp)

# Create a test suite combining all test classes
regressionTest = unittest.TestSuite([tc1,tc2,tc3,tc4,tc5,tc6,tc7,tc8,tc9,tc10,tc11,tc12,tc13])

unittest.TextTestRunner(verbosity=2).run(regressionTest)


