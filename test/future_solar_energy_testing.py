from app.calculator import *
import unittest


class TestFutureSolar(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_1(self):
        """
            solar_testing
            condition: This path is when the start time and end time is not within daylight length, thus it will return directly as there will be no solar energy generated
        """
        start_time = datetime(2021, 2, 22, 1, 30)
        end_time = datetime(2021, 2, 22, 2, 15)
        postcode = "7250"
        solar_energy_generated = self.calculator.calculate_solar_energy_future(
            start_time, end_time, postcode)
        expected_result = 0
        self.assertAlmostEqual(solar_energy_generated, expected_result, msg=("Expected %s, got %s instead"
                                                                                         % (expected_result, solar_energy_generated)))
    def test_2(self):
        """
            solar_testing
            condition: This path is when the start time hour is the same as sunrise hour but the start time minute is smaller than the sunrise minute,
            it will update the value of start time. Then, path 8-9-10 will not be possible as path 8-9-10 indicates the start time to end time is a whole hour, 
            which won’t happen as if the start time minute is smaller than sunrise minute it won’t be a whole hour.
        """
        start_time = datetime(2021, 2, 22, 5, 00)
        end_time = datetime(2021, 2, 22, 6, 00)
        postcode = "7250"
        solar_energy_generated = self.calculator.calculate_solar_energy_future(
            start_time, end_time, postcode)
        expected_result = 0.99
        self.assertAlmostEqual(solar_energy_generated, expected_result, delta=0.01, msg=("Expected %s, got %s instead"
                                                                                         % (expected_result, solar_energy_generated)))
    def test_3(self):
        """
            solar_testing
            condition: This path is when the end time hour is the same as sunset hour but the end time minute is larger than the sunset minute, 
            it will update the value of end time. Then, path 8-9-10 will not be possible as path 8-9-10 indicates the start time to end time is a whole hour, 
            which won’t happen as if the end time minute is smaller than sunset minute it won’t be a whole hour.
        """
        start_time = datetime(2021, 2, 22, 19, 00)
        end_time = datetime(2021, 2, 22, 20, 00)
        postcode = "7250"
        solar_energy_generated = self.calculator.calculate_solar_energy_future(
            start_time, end_time, postcode)
        expected_result = 0.34
        self.assertAlmostEqual(solar_energy_generated, expected_result, delta=0.01, msg=("Expected %s, got %s instead"
                                                                                         % (expected_result, solar_energy_generated)))
    def test_4(self):
        """
            solar_testing
            condition: This path is when the start time and end time has a whole hour gap which is 60 minutes. The value of du will be updated to 1.
        """
        start_time = datetime(2021, 2, 22, 17, 00)
        end_time = datetime(2021, 2, 22, 18, 00)
        postcode = "7250"
        solar_energy_generated = self.calculator.calculate_solar_energy_future(
            start_time, end_time, postcode)
        expected_result = 3.25
        self.assertAlmostEqual(solar_energy_generated, expected_result, delta=0.01, msg=("Expected %s, got %s instead"
                                                                                         % (expected_result, solar_energy_generated)))
    def test_5(self):
        """
            cost_calculation for example given in the assignment spec
        """
        config = 3
        start_time = time(17,30)
        start_date = date(2022, 2, 22)
        battery_capacity = 50
        initial_charge = 20
        power = self.calculator.get_configuration(config)[0]
        base_cost = self.calculator.get_configuration(config)[1]
        end_time = datetime(2022,2,22,18,15)   
        final_cost = self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                                start_state=initial_charge, end_time=end_time,
                                                                base_price=base_cost, power=power,
                                                                capacity=battery_capacity, postcode="7250",solar_energy=True)
        expected_output = 0.22
        self.assertAlmostEqual(final_cost, expected_output, delta=0.01, msg=("Expected %s, got %s instead"
                                                                                         % (expected_output, final_cost)))

    def test_6(self):
        """
            cost_calculation for example given in the assignment spec, with the solar_energy = False
            which by defauly will not happen if the date extends to future, this testing main aim is to cover the branch
            The boolean for solar_energy is to give much more flexibility to the calculation for future extension
        """
        config = 3
        start_time = time(17,30)
        start_date = date(2022, 2, 22)
        battery_capacity = 50
        initial_charge = 20
        power = self.calculator.get_configuration(config)[0]
        base_cost = self.calculator.get_configuration(config)[1]
        end_time = datetime(2022,2,22,18,15)   
        final_cost = self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                                start_state=initial_charge, end_time=end_time,
                                                                base_price=base_cost, power=power,
                                                                capacity=battery_capacity, postcode="7250")
        expected_output = 0.48
        self.assertAlmostEqual(final_cost, expected_output, delta=0.01, msg=("Expected %s, got %s instead"
                                                                                         % (expected_output, final_cost)))
    
    def test_7(self):
        """
            cost_calculation for same year which is 12-12-2021 to get reference date for 2020 instead of 2021, value will be difference when the date of testing exceed 12-12-2021
            This is manual calculaiton for the expected output:
            2020: si = 8.7, dl = 15.15, 
            5-6: cc = 2, du = 0.5
            6-7: cc = 1, du = 0.25

            2019: si = 8.1, dl = 15.13, 
            5-6: cc = 34, du = 0.5
            6-7: cc = 49, du = 0.25

            2018: si = 8.7, dl = 15.13, 
            5-6: cc = 6, du = 0.5 
            6-7: cc = 3, du = 0.25

                    |       2020         |        2019        |        2018        |
                    |solar | net  | cost | solar| net  | cost | solar| net  | cost | 
            5-6 pm  |2.8139|0.7861|0.0786|1.7667|1.8333|0.2017|2.7026|0.8974|0.0987|
            6-7 pm  |1.4213|0.3787|0.0189|0.6826|1.1174|0.0615|1.3944|0.4056|0.0223|
            total cost = ( 0.0786+0.0189+0.2017+0.0615+0.0987+0.0223 )/3
            total cost = 0.16
        """
        config = 3
        start_time = time(17,30)
        start_date = date(2021, 12, 12)
        battery_capacity = 50
        initial_charge = 20
        power = self.calculator.get_configuration(config)[0]
        base_cost = self.calculator.get_configuration(config)[1]
        end_time = datetime(2021,12,12,18,15)  
        final_cost = self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                                start_state=initial_charge, end_time=end_time,
                                                                base_price=base_cost, power=power,
                                                                capacity=battery_capacity, postcode="7250",solar_energy=True)
        expected_output = 0.16
        self.assertAlmostEqual(final_cost, expected_output, delta=0.01, msg=("Expected %s, got %s instead"
                                                                                         % (expected_output, final_cost)))

    # you may create test suite if needed
    # Test case needed for form
if __name__ == "__main__":
    unittest.main()
