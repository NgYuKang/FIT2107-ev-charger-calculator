from app.calculator import *
import unittest
from datetime import datetime


class TestSolarEnergyPastCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()
        self.postcode = "4000"

    def test_solar_energy_past_testcase1(self):
        """
        Path coverage for test case 1 of calculate_solar_energy_past_to_currentday_minus_two
        """
        start = datetime(2008, 7, 1, 12, 30)
        end = datetime(2008, 7, 1, 13)
        expected = 1.82
        actual = self.calculator.calculate_solar_energy_past_to_currentday_minus_two(start, end, self.postcode)
        self.assertAlmostEqual(actual, expected, delta=0.1, msg=("Expected %s, Got %s instead") % (expected, actual))

    def test_solar_energy_past_testcase2(self):
        """
        Path coverage for test case 2 of calculate_solar_energy_past_to_currentday_minus_two
        """
        start = datetime(2008, 6, 30)
        end = datetime(2008, 6, 30, 1)
        expected = 0
        actual = self.calculator.calculate_solar_energy_past_to_currentday_minus_two(start, end, self.postcode)
        self.assertEqual(actual, expected, msg=("Expected %s, Got %s instead") % (expected, actual))

    def test_solar_energy_past_diff_date(self):
        """
        Path coverage for datetime validation test for calculate_solar_energy_past_to_currentday_minus_two
        """
        start = datetime(2008, 7, 2)
        end = datetime(2008, 7, 1)
        with self.assertRaises(ValueError):
            self.calculator.calculate_solar_energy_past_to_currentday_minus_two(start, end, self.postcode)

    def test_solar_energy_past_invalid_hours_interval(self):
        """
        Path coverage for datetime validation test for calculate_solar_energy_past_to_currentday_minus_two
        """
        start = datetime(2008, 7, 1, 12, 1)
        end = datetime(2008, 7, 1, 13, 5)
        with self.assertRaises(ValueError):
            self.calculator.calculate_solar_energy_past_to_currentday_minus_two(start, end, self.postcode)

    def test_solar_energy_part_asgn_example(self):
        """
        Additional test using given example from assignment specs (Example 1)
        """
        start = datetime(2020, 12, 25, 8)
        end = datetime(2020, 12, 25, 9)
        postcode = "6001"
        expected = 6.02
        actual = self.calculator.calculate_solar_energy_past_to_currentday_minus_two(start, end, postcode)
        self.assertAlmostEqual(actual, expected, delta=0.1, msg=("Expected %s, Got %s instead") % (expected, actual))


class TestSolarEnergyDuration(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()
        self.postcode = "4000"
        self.date = date(2021, 9, 10)

    def test_solar_energy_duration_error(self):
        """
        Checks if ValueError is raised in appropriate cases (test case 1)
        """
        start = time(13)
        end = time(12)
        with self.assertRaises(ValueError):
            self.calculator.get_solar_energy_duration(start, end, self.date, self.postcode)

    def test_solar_energy_duration_start_during_sunset(self):
        """
        Ensures that function returns 0 if start time is during sunset (test case 2)
        """
        start = time(22)
        end = time(23)
        expected = 0
        actual = self.calculator.get_solar_energy_duration(start, end, self.date, self.postcode)
        self.assertEqual(actual, expected, msg=("Expected %s, Got %s instead") % (expected, actual))

    def test_solar_energy_duration_end_before_sunrise(self):
        """
        Ensures that function returns 0 if end time is before or during sunrise (test case 3)
        """
        start = time(3)
        end = time(4)
        expected = 0
        actual = self.calculator.get_solar_energy_duration(start, end, self.date, self.postcode)
        self.assertEqual(actual, expected, msg=("Expected %s, Got %s instead") % (expected, actual))

    def test_solar_energy_duration_normal(self):
        """
        Test case for normal inputs (test case 4)
        """
        start = time(12, 30)
        end = time(13)
        expected = 0.5
        actual = self.calculator.get_solar_energy_duration(start, end, self.date, self.postcode)
        self.assertEqual(actual, expected, msg=("Expected %s, Got %s instead") % (expected, actual))


class TestTotalCostWithSolarPast(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()
        self.postcode = "6001"

    def test_whitebox_total_cost_with_solar_past(self):
        """
        Path coverage test for total_cost_calculation taking solar energy from past dates into account
        """
        config = 8
        start_time = time(8)
        start_date = date(2020, 12, 25)
        battery_capacity = 50
        initial_charge = 20
        final_charge = 80
        expected_cost = 16.22
        power = self.calculator.get_configuration(config)[0]
        base_cost = self.calculator.get_configuration(config)[1]
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        end_time = self.calculator.get_end_time(start_date, start_time, charge_time)
        final_cost = self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                            start_state=initial_charge, end_time=end_time,
                                                            base_price=base_cost, power=power,
                                                            capacity=battery_capacity, postcode=self.postcode, solar_energy=True)

        self.assertAlmostEqual(final_cost, expected_cost, delta=0.01, msg=("Expected %s, got %s instead"
                                                                           % (expected_cost, final_cost)))

    def test_whitebox_total_cost_no_solar_past(self):
        """
        Path coverage test for total_cost_calculation without taking solar energy from past dates into account
        """
        config = 8
        start_time = time(8)
        start_date = date(2020, 12, 25)
        battery_capacity = 50
        initial_charge = 20
        final_charge = 80
        expected_cost = 16.50
        power = self.calculator.get_configuration(config)[0]
        base_cost = self.calculator.get_configuration(config)[1]
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        end_time = self.calculator.get_end_time(start_date, start_time, charge_time)
        final_cost = self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                            start_state=initial_charge, end_time=end_time,
                                                            base_price=base_cost, power=power,
                                                            capacity=battery_capacity, postcode=self.postcode, solar_energy=False)

        self.assertAlmostEqual(final_cost, expected_cost, delta=0.01, msg=("Expected %s, got %s instead"
                                                                           % (expected_cost, final_cost)))

if __name__ == '__main__':
    # load these test suits
    solar_calc_suit = unittest.TestLoader().loadTestsFromTestCase(TestSolarEnergyPastCalculator)
    solar_dur_suit = unittest.TestLoader().loadTestsFromTestCase(TestSolarEnergyDuration)
    total_cost_suit = unittest.TestLoader().loadTestsFromTestCase(TestTotalCostWithSolarPast)

    # run the test suits
    unittest.TextTestRunner(verbosity=2).run(solar_calc_suit)
    unittest.TextTestRunner(verbosity=2).run(solar_dur_suit)
    unittest.TextTestRunner(verbosity=2).run(total_cost_suit)
