from app.calculator import *
import unittest
from datetime import date
import os

# Uncomment for local test
# os.chdir("../")
class TestStateHolidays(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_state_holidays_1(self):
        state_str = "NT"
        anzac_day = date(2021, 4, 26)
        self.assertTrue(self.calculator.is_holiday(anzac_day, state_str))

    def test_state_holidays2(self):
        state_str = "ACT"
        easter_sat = date(2021, 4, 3)
        self.assertTrue(self.calculator.is_holiday(easter_sat, state_str))



if __name__ == "__main__":
    # create the test suit from the cases above.
    suit = unittest.TestLoader().loadTestsFromTestCase(TestStateHolidays)
    # this will run the test suit
    unittest.TextTestRunner(verbosity=2).run(suit)