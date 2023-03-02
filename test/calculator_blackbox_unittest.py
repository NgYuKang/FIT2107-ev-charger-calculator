from app.calculator import *
import unittest
from datetime import time, date


class TestCalculator(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()
        self.postcode = "4000"

    def test_tc1_cost(self):
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
                                                                           % (expected_cost,final_cost)))

    def test_tc1_time(self):
        config = 1
        battery_capacity = 50
        initial_charge = 20
        final_charge = 40
        expected_time = "5 hours"
        power = self.calculator.get_configuration(config)[0]
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        time_str = self.calculator.get_charging_time_str(charge_time)
        self.assertEqual(expected_time, time_str, msg=("Expected %s, got %s instead" % (expected_time,time_str)))

    def test_tc2_cost(self):
        config = 1
        start_time = time(0)
        start_date = date(2021, 8, 21)
        battery_capacity = 50
        initial_charge = 20
        final_charge = 40
        expected_cost = 0.25
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
                                                                           % (expected_cost,final_cost)))

    def test_tc2_time(self):
        config = 1
        battery_capacity = 50
        initial_charge = 20
        final_charge = 40
        expected_time = "5 hours"
        power = self.calculator.get_configuration(config)[0]
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        time_str = self.calculator.get_charging_time_str(charge_time)
        self.assertEqual(expected_time, time_str, msg=("Expected %s, got %s instead" % (expected_time,time_str)))

    def test_tc3_cost(self):
        config = 2
        start_time = time(8)
        start_date = date(2021, 8, 24)
        battery_capacity = 50
        initial_charge = 20
        final_charge = 40
        expected_cost = 0.83
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
                                                                           % (expected_cost,final_cost)))

    def test_tc3_time(self):
        config = 2
        battery_capacity = 50
        initial_charge = 20
        final_charge = 40
        expected_time = "2 hours 46 minutes 39 seconds"
        power = self.calculator.get_configuration(config)[0]
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        time_str = self.calculator.get_charging_time_str(charge_time)
        self.assertEqual(expected_time, time_str, msg=("Expected %s, got %s instead" % (expected_time,time_str)))

    def test_tc4_cost(self):
        config = 2
        start_time = time(0)
        start_date = date(2021, 8, 21)
        battery_capacity = 50
        initial_charge = 20
        final_charge = 40
        expected_cost = 0.38
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
                                                                           % (expected_cost,final_cost)))

    def test_tc4_time(self):
        config = 2
        battery_capacity = 50
        initial_charge = 20
        final_charge = 40
        expected_time = "2 hours 46 minutes 39 seconds"
        power = self.calculator.get_configuration(config)[0]
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        time_str = self.calculator.get_charging_time_str(charge_time)
        self.assertEqual(expected_time, time_str, msg=("Expected %s, got %s instead" % (expected_time,time_str)))


    def test_tc5_cost(self):
        config = 3
        start_time = time(8)
        start_date = date(2021, 8, 21)
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
                                                                           % (expected_cost,final_cost)))

    def test_tc5_time(self):
        config = 3
        battery_capacity = 50
        initial_charge = 20
        final_charge = 40
        expected_time = "1 hour 23 minutes 19 seconds"
        power = self.calculator.get_configuration(config)[0]
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        time_str = self.calculator.get_charging_time_str(charge_time)
        self.assertEqual(expected_time, time_str, msg=("Expected %s, got %s instead" % (expected_time,time_str)))

    def test_tc6_cost(self):
        config = 3
        start_time = time(0)
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
                                                                           % (expected_cost,final_cost)))

    def test_tc6_time(self):
        config = 3
        battery_capacity = 50
        initial_charge = 20
        final_charge = 40
        expected_time = "1 hour 23 minutes 19 seconds"
        power = self.calculator.get_configuration(config)[0]
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        time_str = self.calculator.get_charging_time_str(charge_time)
        self.assertEqual(expected_time, time_str, msg=("Expected %s, got %s instead" % (expected_time,time_str)))

    def test_tc7_cost(self):
        config = 4
        start_time = time(8)
        start_date = date(2021, 8, 21)
        battery_capacity = 50
        initial_charge = 20
        final_charge = 40
        expected_cost = 1.25
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
                                                                           % (expected_cost,final_cost)))

    def test_tc7_time(self):
        config = 4
        battery_capacity = 50
        initial_charge = 20
        final_charge = 40
        expected_time = "54 minutes 32 seconds"
        power = self.calculator.get_configuration(config)[0]
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        time_str = self.calculator.get_charging_time_str(charge_time)
        self.assertEqual(expected_time, time_str, msg=("Expected %s, got %s instead" % (expected_time,time_str)))

    def test_tc8_cost(self):
        config = 4
        start_time = time(0)
        start_date = date(2021, 8, 24)
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
                                                                           % (expected_cost,final_cost)))

    def test_tc8_time(self):
        config = 4
        battery_capacity = 50
        initial_charge = 20
        final_charge = 40
        expected_time = "54 minutes 32 seconds"
        power = self.calculator.get_configuration(config)[0]
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        time_str = self.calculator.get_charging_time_str(charge_time)
        self.assertEqual(expected_time, time_str, msg=("Expected %s, got %s instead" % (expected_time,time_str)))

    def test_tc9_cost(self):
        config = 5
        start_time = time(8)
        start_date = date(2021, 8, 24)
        battery_capacity = 100
        initial_charge = 20
        final_charge = 60
        expected_cost = 6.6
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
                                                                           % (expected_cost,final_cost)))

    def test_tc9_time(self):
        config = 5
        battery_capacity = 100
        initial_charge = 20
        final_charge = 60
        expected_time = "1 hour 49 minutes 5 seconds"
        power = self.calculator.get_configuration(config)[0]
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        time_str = self.calculator.get_charging_time_str(charge_time)
        self.assertEqual(expected_time, time_str, msg=("Expected %s, got %s instead" % (expected_time,time_str)))

    def test_tc10_cost(self):
        config = 5
        start_time = time(0)
        start_date = date(2021, 8, 21)
        battery_capacity = 100
        initial_charge = 20
        final_charge = 60
        expected_cost = 3
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
                                                                           % (expected_cost,final_cost)))

    def test_tc10_time(self):
        config = 5
        battery_capacity = 100
        initial_charge = 20
        final_charge = 60
        expected_time = "1 hour 49 minutes 5 seconds"
        power = self.calculator.get_configuration(config)[0]
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        time_str = self.calculator.get_charging_time_str(charge_time)
        self.assertEqual(expected_time, time_str, msg=("Expected %s, got %s instead" % (expected_time,time_str)))

    def test_tc11_cost(self):
        config = 6
        start_time = time(8)
        start_date = date(2021, 8, 21)
        battery_capacity = 100
        initial_charge = 20
        final_charge = 60
        expected_cost = 8
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
                                                                           % (expected_cost,final_cost)))

    def test_tc11_time(self):
        config = 6
        battery_capacity = 100
        initial_charge = 20
        final_charge = 60
        expected_time = "1 hour 6 minutes 40 seconds"
        power = self.calculator.get_configuration(config)[0]
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        time_str = self.calculator.get_charging_time_str(charge_time)
        self.assertEqual(expected_time, time_str, msg=("Expected %s, got %s instead" % (expected_time,time_str)))

    def test_tc12_cost(self):
        config = 6
        start_time = time(0)
        start_date = date(2021, 8, 24)
        battery_capacity = 100
        initial_charge = 20
        final_charge = 60
        expected_cost = 4.4
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
                                                                           % (expected_cost,final_cost)))

    def test_tc12_time(self):
        config = 6
        battery_capacity = 100
        initial_charge = 20
        final_charge = 60
        expected_time = "1 hour 6 minutes 40 seconds"
        power = self.calculator.get_configuration(config)[0]
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        time_str = self.calculator.get_charging_time_str(charge_time)
        self.assertEqual(expected_time, time_str, msg=("Expected %s, got %s instead" % (expected_time,time_str)))


    def test_tc13_cost(self):
        config = 7
        start_time = time(8)
        start_date = date(2021, 8, 24)
        battery_capacity = 100
        initial_charge = 20
        final_charge = 60
        expected_cost = 13.2
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
                                                                           % (expected_cost,final_cost)))

    def test_tc13_time(self):
        config = 7
        battery_capacity = 100
        initial_charge = 20
        final_charge = 60
        expected_time = "26 minutes 39 seconds"
        power = self.calculator.get_configuration(config)[0]
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        time_str = self.calculator.get_charging_time_str(charge_time)
        self.assertEqual(expected_time, time_str, msg=("Expected %s, got %s instead" % (expected_time,time_str)))

    def test_tc14_cost(self):
        config = 7
        start_time = time(0)
        start_date = date(2021, 8, 21)
        battery_capacity = 100
        initial_charge = 20
        final_charge = 60
        expected_cost = 6
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
                                                                           % (expected_cost,final_cost)))

    def test_tc14_time(self):
        config = 7
        battery_capacity = 100
        initial_charge = 20
        final_charge = 60
        expected_time = "26 minutes 39 seconds"
        power = self.calculator.get_configuration(config)[0]
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        time_str = self.calculator.get_charging_time_str(charge_time)
        self.assertEqual(expected_time, time_str, msg=("Expected %s, got %s instead" % (expected_time,time_str)))

    def test_tc15_cost(self):
        config = 8
        start_time = time(8)
        start_date = date(2021, 8, 24)
        battery_capacity = 100
        initial_charge = 20
        final_charge = 60
        expected_cost = 22
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
                                                                           % (expected_cost,final_cost)))

    def test_tc15_time(self):
        config = 8
        battery_capacity = 100
        initial_charge = 20
        final_charge = 60
        expected_time = "6 minutes 51 seconds"
        power = self.calculator.get_configuration(config)[0]
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        time_str = self.calculator.get_charging_time_str(charge_time)
        self.assertEqual(expected_time, time_str, msg=("Expected %s, got %s instead" % (expected_time,time_str)))

    def test_tc16_cost(self):
        config = 8
        start_time = time(0)
        start_date = date(2021, 8, 21)
        battery_capacity = 100
        initial_charge = 20
        final_charge = 60
        expected_cost = 10
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
                                                                           % (expected_cost,final_cost)))

    def test_tc16_time(self):
        config = 8
        battery_capacity = 100
        initial_charge = 20
        final_charge = 60
        expected_time = "6 minutes 51 seconds"
        power = self.calculator.get_configuration(config)[0]
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        time_str = self.calculator.get_charging_time_str(charge_time)
        self.assertEqual(expected_time, time_str, msg=("Expected %s, got %s instead" % (expected_time,time_str)))

    def test_tc17_cost(self):
        config = 6
        start_time = time(5,30)
        start_date = date(2021, 8, 21)
        battery_capacity = 50
        initial_charge = 20
        final_charge = 80
        expected_cost = 4.2
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
                                                                           % (expected_cost,final_cost)))

    def test_tc17_time(self):
        config = 6
        battery_capacity = 50
        initial_charge = 20
        final_charge = 80
        expected_time = "50 minutes"
        power = self.calculator.get_configuration(config)[0]
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        time_str = self.calculator.get_charging_time_str(charge_time)
        self.assertEqual(expected_time, time_str, msg=("Expected %s, got %s instead" % (expected_time,time_str)))

    def test_tc18_cost(self):
        config = 3
        start_time = time(16,50)
        start_date = date(2021, 8, 20)
        battery_capacity = 50
        initial_charge = 20
        final_charge = 80
        expected_cost = 2.11
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
                                                                           % (expected_cost,final_cost)))

    def test_tc18_time(self):
        config = 3
        battery_capacity = 50
        initial_charge = 20
        final_charge = 80
        expected_time = "4 hours 10 minutes"
        power = self.calculator.get_configuration(config)[0]
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        time_str = self.calculator.get_charging_time_str(charge_time)
        self.assertEqual(expected_time, time_str, msg=("Expected %s, got %s instead" % (expected_time,time_str)))

    def test_tc19_cost(self):
        config = 2
        start_time = time(20,30)
        start_date = date(2021, 8, 22)
        battery_capacity = 50
        initial_charge = 20
        final_charge = 80
        expected_cost = 1.19
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
                                                                           % (expected_cost,final_cost)))

    def test_tc19_time(self):
        config = 2
        battery_capacity = 50
        initial_charge = 20
        final_charge = 80
        expected_time = "8 hours 20 minutes"
        power = self.calculator.get_configuration(config)[0]
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        time_str = self.calculator.get_charging_time_str(charge_time)
        self.assertEqual(expected_time, time_str, msg=("Expected %s, got %s instead" % (expected_time,time_str)))

    def test_tc20_cost(self):
        config = 1
        start_time = time(18,30)
        start_date = date(2021, 8, 20)
        battery_capacity = 50
        initial_charge = 20
        final_charge = 60
        expected_cost = 0.53
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
                                                                           % (expected_cost,final_cost)))

    def test_tc20_time(self):
        config = 1
        battery_capacity = 50
        initial_charge = 20
        final_charge = 60
        expected_time = "10 hours"
        power = self.calculator.get_configuration(config)[0]
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        time_str = self.calculator.get_charging_time_str(charge_time)
        self.assertEqual(expected_time, time_str, msg=("Expected %s, got %s instead" % (expected_time,time_str)))



# you may create test suite if needed
if __name__ == "__main__":
    # create the test suit from the cases above.
    suit = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
    # this will run the test suit
    unittest.TextTestRunner(verbosity=2).run(suit)
