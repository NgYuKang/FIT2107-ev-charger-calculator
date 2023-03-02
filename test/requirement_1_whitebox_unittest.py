from app.calculator import *
import unittest
from datetime import time, date
from dateutil.relativedelta import relativedelta
from unittest.mock import Mock, patch, PropertyMock
import os


# Uncomment for local test
# os.chdir("../")
class WhiteBoxCostCalculator(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()
        self.postcode = "4000"

    def test_whitebox_totalcost_tc1(self):
        """
        Path coverage test case 1 for total_cost_calculation.
        """
        config = 1
        start_time = time(8)
        start_date = date(2021, 8, 24)
        battery_capacity = 50
        initial_charge = 20
        final_charge = 40
        expected_cost = 0.55
        power = self.calculator.get_configuration(config)[0]
        base_cost = self.calculator.get_configuration(config)[1]
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        end_time = self.calculator.get_end_time(start_date, start_time, charge_time)
        final_cost = self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                            start_state=initial_charge, end_time=end_time,
                                                            base_price=base_cost, power=power,
                                                            capacity=battery_capacity, postcode=self.postcode)

        self.assertAlmostEqual(final_cost, expected_cost, delta=0.01, msg=("Expected %s, got %s instead"
                                                                           % (expected_cost, final_cost)))

    # def test_whitebox_totalcost_tc2(self):
    #     """
    #     Path coverage test case 2 for total_cost_calculation.
    #     """
    #     config = 1
    #     start_time = time(0)
    #     start_date = date(2021, 8, 21)
    #     battery_capacity = 50
    #     initial_charge = 20
    #     final_charge = 40
    #     expected_cost = 0.25
    #     power = self.calculator.get_configuration(config)[0]
    #     base_cost = self.calculator.get_configuration(config)[1]
    #     charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
    #                                                    capacity=battery_capacity, power=power)
    #     end_time = self.calculator.get_end_time(start_date, start_time, charge_time)
    #     final_cost = self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
    #                                                         start_state=initial_charge, end_time=end_time,
    #                                                         base_price=base_cost, power=power,
    #                                                         capacity=battery_capacity, postcode=self.postcode)
    #     self.assertAlmostEqual(final_cost, expected_cost, delta=0.01, msg=("Expected %s, got %s instead"
    #                                                                        % (expected_cost, final_cost)))

    @patch('app.calculator.Calculator.is_holiday')
    def test_whitebox_totalcost_tc3(self, mocked_holiday):
        """
        Path coverage test case 3 for total_cost_calculation.
        """
        mocked_holiday.return_value = False

        config = 3
        start_time = time(8)
        start_date = date.today()
        battery_capacity = 50
        initial_charge = 20
        final_charge = 40
        expected_cost = 1
        power = self.calculator.get_configuration(config)[0]
        base_cost = self.calculator.get_configuration(config)[1]
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        end_time = self.calculator.get_end_time(start_date, start_time, charge_time)
        final_cost = self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                            start_state=initial_charge, end_time=end_time,
                                                            base_price=base_cost, power=power,
                                                            capacity=battery_capacity, postcode=self.postcode)
        self.assertAlmostEqual(final_cost, expected_cost, delta=0.01, msg=("Expected %s, got %s instead"
                                                                           % (expected_cost, final_cost)))

    @patch('app.calculator.Calculator.is_holiday')
    def test_whitebox_totalcost_tc2(self, mocked_holiday):
        """
        Path coverage test case 2 for total_cost_calculation.
        """
        mocked_holiday.return_value = True

        config = 4
        start_time = time(0)
        start_date = date.today() + relativedelta(years=1)
        battery_capacity = 50
        initial_charge = 20
        final_charge = 40
        expected_cost = 0.69
        power = self.calculator.get_configuration(config)[0]
        base_cost = self.calculator.get_configuration(config)[1]
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        end_time = self.calculator.get_end_time(start_date, start_time, charge_time)
        final_cost = self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                            start_state=initial_charge, end_time=end_time,
                                                            base_price=base_cost, power=power,
                                                            capacity=battery_capacity, postcode=self.postcode)

        self.assertAlmostEqual(final_cost, expected_cost, delta=0.01, msg=("Expected %s, got %s instead"
                                                                           % (expected_cost, final_cost)))

    def test_whitebox_cost_calculation_tc1(self):
        """
        Path coverage test case 1 for cost_calculation
        """
        initial_state = 20
        final_state = 40
        capacity = 50
        base_price = 5
        is_holiday = True
        is_peak = True
        expected_cost = 0.55

        final_cost = self.calculator.cost_calculation(initial_state=initial_state, final_state=final_state,
                                                      capacity=capacity, is_holiday=is_holiday, is_peak=is_peak,
                                                      base_price=base_price)
        self.assertAlmostEqual(final_cost, expected_cost, delta=0.01, msg=("Expected %s, got %s instead"
                                                                           % (expected_cost, final_cost)))

    def test_whitebox_cost_calculation_tc2(self):
        """
        Path coverage test case 2 for cost_calculation
        """
        initial_state = 20
        final_state = 40
        capacity = 50
        base_price = 12.5
        is_holiday = True
        is_peak = False
        expected_cost = 0.69

        final_cost = self.calculator.cost_calculation(initial_state=initial_state, final_state=final_state,
                                                      capacity=capacity, is_holiday=is_holiday, is_peak=is_peak,
                                                      base_price=base_price)
        self.assertAlmostEqual(final_cost, expected_cost, delta=0.01, msg=("Expected %s, got %s instead"
                                                                           % (expected_cost, final_cost)))

    def test_whitebox_cost_calculation_tc3(self):
        """
        Path coverage test case 3 for cost_calculation
        """
        initial_state = 20
        final_state = 40
        capacity = 50
        base_price = 10
        is_holiday = False
        is_peak = True
        expected_cost = 1

        final_cost = self.calculator.cost_calculation(initial_state=initial_state, final_state=final_state,
                                                      capacity=capacity, is_holiday=is_holiday, is_peak=is_peak,
                                                      base_price=base_price)
        self.assertAlmostEqual(final_cost, expected_cost, delta=0.01, msg=("Expected %s, got %s instead"
                                                                           % (expected_cost, final_cost)))

    def test_whitebox_cost_calculation_tc4(self):
        """
        Path coverage test case 4 for cost_calculation
        """
        initial_state = 20
        final_state = 40
        capacity = 50
        base_price = 5
        is_holiday = False
        is_peak = False
        expected_cost = 0.25

        final_cost = self.calculator.cost_calculation(initial_state=initial_state, final_state=final_state,
                                                      capacity=capacity, is_holiday=is_holiday, is_peak=is_peak,
                                                      base_price=base_price)
        self.assertAlmostEqual(final_cost, expected_cost, delta=0.01, msg=("Expected %s, got %s instead"
                                                                           % (expected_cost, final_cost)))

    def test_whitebox_time_calculation_tc1(self):
        """
        Line coverage test case 1 for time_calculation
        """
        battery_capacity = 50
        initial_charge = 20
        final_charge = 40
        expected_time = 5
        power = 2
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        self.assertEqual(expected_time, charge_time, msg=("Expected %s, got %s instead" %
                                                          (expected_time, charge_time)))

    def test_whitebox_get_configuration_tc1(self):
        """
        Line coverage test case 1 for get_configuration
        """
        configuration = 1
        expected_out = [2, 5]
        actual_out = self.calculator.get_configuration(configuration)
        self.assertEqual(expected_out, actual_out, msg=("Expected %s, got %s instead" %
                                                        (expected_out, actual_out)))

    def test_whitebox_is_peak_tc1(self):
        """
        Path coverage test case 1 for is_peak
        """
        input_time = time(8)
        actual_out = self.calculator.is_peak(input_time)
        self.assertTrue(actual_out)

    def test_whitebox_is_peak_tc2(self):
        """
        Path coverage test case 2 for is_peak
        """
        input_time = time(19)
        actual_out = self.calculator.is_peak(input_time)
        self.assertFalse(actual_out)

    def test_whitebox_is_peak_tc3(self):
        """
        Path coverage test case 2 for is_peak
        """
        input_time = time(4)
        actual_out = self.calculator.is_peak(input_time)
        self.assertFalse(actual_out)

    def test_whitebox_get_charging_time_str_tc1(self):
        # Test get_charging_time_str, path coverage cfg test case, check branch of going through
        # else of ALL outer if statement
        input_time = 0
        expected_str = ""
        actual_str = self.calculator.get_charging_time_str(input_time)
        self.assertEqual(expected_str, actual_str, msg=("Expected %s, got %s instead" %
                                                        (expected_str, actual_str)))

    def test_whitebox_get_charging_time_str_tc2(self):
        # Test get_charging_time_str, path coverage cfg test case, check hour if statement branch
        input_time = 1
        expected_str = "1 hour"
        actual_str = self.calculator.get_charging_time_str(input_time)
        self.assertEqual(expected_str, actual_str, msg=("Expected %s, got %s instead" %
                                                        (expected_str, actual_str)))

    def test_whitebox_get_charging_time_str_tc3(self):
        # Test get_charging_time_str, path coverage cfg test case, check hour if statement branch
        input_time = 2
        expected_str = "2 hours"
        actual_str = self.calculator.get_charging_time_str(input_time)
        self.assertEqual(expected_str, actual_str, msg=("Expected %s, got %s instead" %
                                                        (expected_str, actual_str)))

    def test_whitebox_get_charging_time_str_tc4(self):
        # Test get_charging_time_str, path coverage cfg test case, check minute if statement branch
        input_time = (1 / 60)
        expected_str = "1 minute"
        actual_str = self.calculator.get_charging_time_str(input_time)
        self.assertEqual(expected_str, actual_str, msg=("Expected %s, got %s instead" %
                                                        (expected_str, actual_str)))

    def test_whitebox_get_charging_time_str_tc5(self):
        # Test get_charging_time_str, path coverage cfg test case, check minute if statement branch
        input_time = (2 / 60)
        expected_str = "2 minutes"
        actual_str = self.calculator.get_charging_time_str(input_time)
        self.assertEqual(expected_str, actual_str, msg=("Expected %s, got %s instead" %
                                                        (expected_str, actual_str)))

    def test_whitebox_get_charging_time_str_tc6(self):
        # Test get_charging_time_str, path coverage cfg test case, check seconds if statement branch
        input_time = (1 / 60) / 60
        expected_str = "1 second"
        actual_str = self.calculator.get_charging_time_str(input_time)
        self.assertEqual(expected_str, actual_str, msg=("Expected %s, got %s instead" %
                                                        (expected_str, actual_str)))

    def test_whitebox_get_charging_time_str_tc7(self):
        # Test get_charging_time_str, path coverage cfg test case, check seconds if statement branch
        input_time = (2 / 60 / 60)
        expected_str = "2 seconds"
        actual_str = self.calculator.get_charging_time_str(input_time)
        self.assertEqual(expected_str, actual_str, msg=("Expected %s, got %s instead" %
                                                        (expected_str, actual_str)))

    def test_whitebox_is_holiday_tc1(self):
        # MC/DC Test case for is_holiday
        in_date = date(2021, 9, 15)
        state = "ACT"
        actual_out = self.calculator.is_holiday(in_date, state)
        self.assertTrue(actual_out)

    def test_whitebox_is_holiday_tc2(self):
        # MC/DC Test case for is_holiday
        in_date = date(2021, 1, 1)
        state = "ACT"
        actual_out = self.calculator.is_holiday(in_date, state)
        self.assertTrue(actual_out)

    def test_whitebox_is_holiday_tc3(self):
        # MC/DC Test case for is_holiday
        in_date = date(2021, 8, 29)
        state = "ACT"
        actual_out = self.calculator.is_holiday(in_date, state)
        self.assertFalse(actual_out)

    def test_white_box_invalid_end_date(self):
        """
        We will test what happens when the end date is earlier than the start date.
        In this case, there should be 0 charge at all, at the backend.
        Frontend wise, this should be caught by calculator_form.py
        """
        config = 6
        start_time = time(5, 30)
        start_date = date(2021, 8, 21)
        battery_capacity = 50
        initial_charge = 20
        final_charge = 80
        expected_cost = 0
        power = self.calculator.get_configuration(config)[0]
        base_cost = self.calculator.get_configuration(config)[1]
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        # end_time = self.calculator.get_end_time(start_date, start_time, charge_time)
        end_time = datetime(2020, 8, 21, 5, 30)
        final_cost = self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                            start_state=initial_charge, end_time=end_time,
                                                            base_price=base_cost, power=power,
                                                            capacity=battery_capacity, postcode=self.postcode)

        self.assertEqual(final_cost, expected_cost, msg=("Expected %s, got %s instead" % (expected_cost, final_cost)))

    def test_whitebox_invalid_time(self):
        """
        We will test what happens if we supply invalid start date
        """
        config = 6
        start_time = time(5, 30)
        start_date = "2021-8-31"
        battery_capacity = 50
        initial_charge = 20
        final_charge = 80
        expected_cost = 0
        power = self.calculator.get_configuration(config)[0]
        base_cost = self.calculator.get_configuration(config)[1]
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        # end_time = self.calculator.get_end_time(start_date, start_time, charge_time)
        end_time = datetime(2020, 8, 21, 5, 30)
        with self.assertRaises(TypeError):
            final_cost = self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                                start_state=initial_charge, end_time=end_time,
                                                                base_price=base_cost, power=power,
                                                                capacity=battery_capacity, postcode=self.postcode)

    def test_whitebox_invalid_date(self):
        """
        We will test what happens if we supply invalid start_time type
        """
        config = 6
        start_time = "5:30"
        start_date = date(2021, 8, 21)
        battery_capacity = 50
        initial_charge = 20
        final_charge = 80
        expected_cost = 0
        power = self.calculator.get_configuration(config)[0]
        base_cost = self.calculator.get_configuration(config)[1]
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        # end_time = self.calculator.get_end_time(start_date, start_time, charge_time)
        end_time = datetime(2020, 8, 21, 5, 30)
        with self.assertRaises(TypeError):
            final_cost = self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                                start_state=initial_charge, end_time=end_time,
                                                                base_price=base_cost, power=power,
                                                                capacity=battery_capacity, postcode=self.postcode)

    def test_whitebox_invalid_type_isoc(self):
        """
        We will test what happens if we supply wrong isoc type
        """
        config = 6
        start_time = time(5, 30)
        start_date = date(2021, 8, 21)
        battery_capacity = 50
        initial_charge = "20"
        final_charge = 80
        power = self.calculator.get_configuration(config)[0]
        base_cost = self.calculator.get_configuration(config)[1]
        charge_time = 4
        end_time = self.calculator.get_end_time(start_date, start_time, charge_time)
        with self.assertRaises(TypeError):
            self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                   start_state=initial_charge, end_time=end_time,
                                                   base_price=base_cost, power=power, capacity=battery_capacity,
                                                   postcode=self.postcode)

    def test_whitebox_invalid_type_battery(self):
        """
        We will test what happens if we supply wrong battery capacity type
        """
        config = 6
        start_time = time(5, 30)
        start_date = date(2021, 8, 21)
        battery_capacity = "50"
        initial_charge = 20
        final_charge = 80
        power = self.calculator.get_configuration(config)[0]
        base_cost = self.calculator.get_configuration(config)[1]
        charge_time = 4
        end_time = self.calculator.get_end_time(start_date, start_time, charge_time)
        with self.assertRaises(TypeError):
            self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                   start_state=initial_charge, end_time=end_time,
                                                   base_price=base_cost, power=power, capacity=battery_capacity,
                                                   postcode=self.postcode)

    def test_whitebox_invalid_type_power(self):
        """
        We will test what happens if we supply wrong power type
        """
        config = 6
        start_time = time(5, 30)
        start_date = date(2021, 8, 21)
        battery_capacity = 50
        initial_charge = 20
        final_charge = 80
        power = str(self.calculator.get_configuration(config)[0])
        base_cost = self.calculator.get_configuration(config)[1]
        charge_time = 4
        end_time = self.calculator.get_end_time(start_date, start_time, charge_time)
        with self.assertRaises(TypeError):
            self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                   start_state=initial_charge, end_time=end_time,
                                                   base_price=base_cost, power=power, capacity=battery_capacity,
                                                   postcode=self.postcode)

    def test_whitebox_invalid_type_base_cost(self):
        """
        We will test what happens if we supply wrong base_cost type
        """
        config = 6
        start_time = time(5, 30)
        start_date = date(2021, 8, 21)
        battery_capacity = 50
        initial_charge = 20
        final_charge = 80
        power = self.calculator.get_configuration(config)[0]
        base_cost = str(self.calculator.get_configuration(config)[1])
        charge_time = 4
        end_time = self.calculator.get_end_time(start_date, start_time, charge_time)
        with self.assertRaises(TypeError):
            self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                   start_state=initial_charge, end_time=end_time,
                                                   base_price=base_cost, power=power, capacity=battery_capacity,
                                                   postcode=self.postcode)

    def test_whitebox_invalid_type_end_time(self):
        """
        We will test what happens if we supply wrong end_time type
        """
        config = 6
        start_time = time(5, 30)
        start_date = date(2021, 8, 21)
        battery_capacity = 50
        initial_charge = 20
        final_charge = 80
        power = self.calculator.get_configuration(config)[0]
        base_cost = self.calculator.get_configuration(config)[1]
        charge_time = 4
        end_time = "2021/8/21"
        with self.assertRaises(TypeError):
            self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                   start_state=initial_charge, end_time=end_time,
                                                   base_price=base_cost, power=power, capacity=battery_capacity,
                                                   postcode=self.postcode)

    def test_whitebox_invalid_type_postcode(self):
        """
        We will test what happens if we supply wrong base_cost type
        """
        config = 6
        start_time = time(5, 30)
        start_date = date(2021, 8, 21)
        battery_capacity = 50
        initial_charge = 20
        final_charge = 80
        power = self.calculator.get_configuration(config)[0]
        base_cost = self.calculator.get_configuration(config)[1]
        charge_time = 4
        end_time = "2021/8/21"
        with self.assertRaises(TypeError):
            self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                   start_state=initial_charge, end_time=end_time,
                                                   base_price=base_cost, power=power, capacity=battery_capacity,
                                                   postcode=4000)

    def test_whitebox_get_config_tc1(self):
        """
        Test boundary < 1
        """
        with self.assertRaises(ValueError):
            self.calculator.get_configuration(0)

    def test_whitebox_get_config_tc2(self):
        """
        Test boundary > 8
        """
        with self.assertRaises(ValueError):
            self.calculator.get_configuration(9)

    def test_invalid_cost_calc_tc1(self):
        """
        Test initial state < 0
        """
        with self.assertRaises(ValueError):
            self.calculator.cost_calculation(-1, 100, 100, True, True, 10)

    def test_invalid_cost_calc_tc2(self):
        # Test final state < initial state
        with self.assertRaises(ValueError):
            self.calculator.cost_calculation(20, 19, 100, True, True, 10)

    def test_invalid_cost_calc_tc3(self):
        # Test capacity < 0
        with self.assertRaises(ValueError):
            self.calculator.cost_calculation(20, 30, -100, True, True, 10)

    def test_invalid_cost_calc_tc4(self):
        # Test base price < 0
        with self.assertRaises(ValueError):
            self.calculator.cost_calculation(20, 30, 100, True, True, -5)

    def test_invalid_time_calc_tc1(self):
        # test initial state < 0
        with self.assertRaises(ValueError):
            self.calculator.time_calculation(-1, 100, 100, 100)

    def test_invalid_time_calc_tc2(self):
        # test final state < initial state
        with self.assertRaises(ValueError):
            self.calculator.time_calculation(20, 19, 100, 100)

    def test_invalid_time_calc_tc3(self):
        # test capacity < 0
        with self.assertRaises(ValueError):
            self.calculator.time_calculation(20, 40, -100, 100)

    def test_invalid_time_calc_tc4(self):
        # test power < 0
        with self.assertRaises(ValueError):
            self.calculator.time_calculation(20, 40, 100, -100)

    def test_invalid_state_is_holiday(self):
        # test invalid state input
        with self.assertRaises(ValueError):
            self.calculator.is_holiday(date(2020,12,1), "LOL")

    def test_invalid_date_is_holiday(self):
        # test invalid date input
        with self.assertRaises(AttributeError):
            self.calculator.is_holiday("1/12/2020", "ACT")

    def test_invalid_time_is_peak(self):
        # test invalid time input
        with self.assertRaises(TypeError):
            self.calculator.is_peak("00:00")

    def test_invalid_charge_time_get_end_time(self):
        # test invalid charge_hours, < 0
        with self.assertRaises(ValueError):
            self.calculator.get_end_time(date(2020,2,1), time(0), -1)

    def test_invalid_date_get_end_time(self):
        # test invalid date input
        with self.assertRaises(TypeError):
            self.calculator.get_end_time("1/2/2021", time(0), 10)

    def test_invalid_time_get_end_time(self):
        # test invalid time input
        with self.assertRaises(TypeError):
            self.calculator.get_end_time(date(2020,2,1), "00:00", 10)

    def test_invalid_get_charging_str(self):
        # test invalid input hours
        with self.assertRaises(ValueError):
            self.calculator.get_charging_time_str(-1)

    def test_invalid_initial_state_total_cost(self):
        # test invalid initial state
        config = 6
        start_time = time(0)
        start_date = date(2021, 8, 21)
        battery_capacity = 50
        initial_charge = -1
        final_charge = 80
        expected_cost = 0
        power = self.calculator.get_configuration(config)[0]
        base_cost = self.calculator.get_configuration(config)[1]
        end_time = datetime(2020, 8, 21, 5, 30)
        with self.assertRaises(ValueError):
            final_cost = self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                                start_state=initial_charge, end_time=end_time,
                                                                base_price=base_cost, power=power,
                                                                capacity=battery_capacity, postcode=self.postcode)
    def test_invalid_base_price_total_cost(self):
        # test invalid base price
        config = 6
        start_time = time(0)
        start_date = date(2021, 8, 21)
        battery_capacity = 50
        initial_charge = 0
        final_charge = 80
        expected_cost = 0
        power = self.calculator.get_configuration(config)[0]
        base_cost = -1
        end_time = datetime(2020, 8, 21, 5, 30)
        with self.assertRaises(ValueError):
            final_cost = self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                                start_state=initial_charge, end_time=end_time,
                                                                base_price=base_cost, power=power,
                                                                capacity=battery_capacity, postcode=self.postcode)
    def test_invalid_power_total_cost(self):
        # test invalid power
        config = 6
        start_time = time(0)
        start_date = date(2021, 8, 21)
        battery_capacity = 50
        initial_charge = 0
        final_charge = 80
        expected_cost = 0
        power = -1
        base_cost = 10
        end_time = datetime(2020, 8, 21, 5, 30)
        with self.assertRaises(ValueError):
            final_cost = self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                                start_state=initial_charge, end_time=end_time,
                                                                base_price=base_cost, power=power,
                                                                capacity=battery_capacity, postcode=self.postcode)
    def test_invalid_capacity_total_cost(self):
        # test invalid capacity
        config = 6
        start_time = time(0)
        start_date = date(2021, 8, 21)
        battery_capacity = -100
        initial_charge = 0
        final_charge = 80
        expected_cost = 0
        power = 0
        base_cost = 10
        end_time = datetime(2020, 8, 21, 5, 30)
        with self.assertRaises(ValueError):
            final_cost = self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                                start_state=initial_charge, end_time=end_time,
                                                                base_price=base_cost, power=power,
                                                                capacity=battery_capacity, postcode=self.postcode)
    def test_invalid_solar_energy_total_cost(self):
        # test invalid solar energy input
        config = 6
        start_time = time(0)
        start_date = date(2021, 8, 21)
        battery_capacity = 0
        initial_charge = 0
        final_charge = 80
        expected_cost = 0
        power = 10
        base_cost = 10
        end_time = datetime(2020, 8, 21, 5, 30)
        with self.assertRaises(ValueError):
            final_cost = self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                                start_state=initial_charge, end_time=end_time,
                                                                base_price=base_cost, power=power,
                                                                capacity=battery_capacity, postcode=self.postcode,
                                                                solar_energy=-1)
    def test_invalid_postcode_get_state_tc1(self):
        # Test invalid postcode
        with self.assertRaises(ValueError):
            self.calculator.get_state("000")

    def test_invalid_postcode_get_state_tc2(self):
        # Test invalid postcode
        with self.assertRaises(ValueError):
            self.calculator.get_state("0000")



if __name__ == "__main__":
    # create the test suit from the cases above.
    suit = unittest.TestLoader().loadTestsFromTestCase(WhiteBoxCostCalculator)
    # this will run the test suit
    unittest.TextTestRunner(verbosity=2).run(suit)
