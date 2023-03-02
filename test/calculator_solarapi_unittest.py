from app.calculator import *
import unittest
from datetime import time, date
from unittest.mock import Mock, patch, PropertyMock
from requests.exceptions import Timeout


class TestDaylightLength(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    @patch('app.calculator.Calculator.get_weather_data')
    def test_DaylightLength_1(self, mocked_get):
        """
        Tests getting daylight length, mocking the return value from get_weather_data
        to see if the appropriate daylight length is calculated.
        """
        mocked_response = Mock()
        data = {"sunrise": "07:20:00",
                "sunset": "17:32:00"}
        mocked_response.json.return_value = data
        mocked_get.return_value = mocked_response

        input_date = date(2021, 8, 1)
        postcode = "3800"
        res = self.calculator.get_day_light_length(input_date, postcode)
        expected_output = 10.2
        self.assertAlmostEqual(res, expected_output, delta=0.01, msg=("Expected %s, got %s" %
                                                                      (expected_output, res)))

    @patch('app.calculator.Calculator.get_weather_data')
    def test_DaylightLength_2(self, mocked_get):
        """
        Tests getting daylight length, mocking the return value from get_weather_data
        to see if the appropriate daylight length is calculated.
        """
        mocked_response = Mock()
        data = {"sunrise": "06:29:00",
                "sunset": "17:20:00"}
        mocked_response.json.return_value = data
        mocked_get.return_value = mocked_response

        input_date = date(2021, 8, 1)
        postcode = "4000"
        res = self.calculator.get_day_light_length(input_date, postcode)
        expected_output = 10.85
        self.assertAlmostEqual(res, expected_output, delta=0.01, msg=("Expected %s, got %s" %
                                                                      (expected_output, res)))

    @patch('app.calculator.Calculator.get_weather_data')
    def test_DaylightLength_3(self, mocked_get):
        """
        Tests getting daylight length, mocking the return value from get_weather_data
        to see if the appropriate daylight length is calculated.
        """
        mocked_response = Mock()
        data = {"sunrise": "06:58:00",
                "sunset": "17:48:00"}
        mocked_response.json.return_value = data
        mocked_get.return_value = mocked_response

        input_date = date(2021, 8, 20)
        postcode = "3200"
        res = self.calculator.get_day_light_length(input_date, postcode)
        expected_output = 10.8334
        self.assertAlmostEqual(res, expected_output, delta=0.01, msg=("Expected %s, got %s" %
                                                                      (expected_output, res)))

    @patch('app.calculator.requests.get')
    def test_DaylightLength_error_invalid_postcode_1(self, mocked_get):
        """
        Tests getting daylight length, mocking an error return value from requests.get
        to see if the appropriate error is raised.
        """
        data = []
        mocked_response = Mock()
        mocked_response.json.return_value = data
        mocked_response.status_code = 200
        mocked_get.return_value = mocked_response

        with self.assertRaises(ValueError):
            self.calculator.get_sun_hour(postcode="0000", input_date=date(year=2021, month=8, day=20))

    @patch('app.calculator.requests.get')
    def test_DaylightLength_error_invalid_postcode_2(self, mocked_get):
        """
        Tests getting daylight length, mocking an error return value from requests.get
        to see if the appropriate error is raised.
        """
        data = ["lol", "lol"]
        mocked_response = Mock()
        mocked_response.json.return_value = data
        mocked_response.status_code = 400
        mocked_get.return_value = mocked_response

        with self.assertRaises(ValueError):
            self.calculator.get_sun_hour(postcode="00", input_date=date(year=2021, month=8, day=20))

    @patch('app.calculator.requests.get')
    def test_DaylightLength_error_invalid_date(self, mocked_get):
        """
        Tests getting daylight length, mocking an error return value from requests.get
        to see if the appropriate error is raised.
        """
        data = ["lol", "lol"]
        mocked_response = Mock()
        mocked_response.json.return_value = data
        mocked_response.status_code = 400
        mocked_get.return_value = mocked_response

        with self.assertRaises(ValueError):
            self.calculator.get_sun_hour(postcode="00", input_date=date(year=2000, month=8, day=20))

    @patch('app.calculator.requests.get')
    def test_DaylightLength_error_invalid_date2(self, mocked_get):
        """
        Tests getting daylight length, mocking an error return value from requests.get
        to see if the appropriate error is raised.
        """
        data = [{"id": "81a5f4b3-df47-4c20-ba2a-ea025e6ac0f8"}]
        mocked_response = Mock()
        mocked_response.json.return_value = data
        mocked_response.status_code = 200
        mocked_get.return_value = mocked_response

        with self.assertRaises(AttributeError):
            self.calculator.get_sun_hour(postcode="4000", input_date="2020/1/1")


class TestSunHours(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    @patch('app.calculator.Calculator.get_weather_data')
    def test_SunHours_1(self, mocked_get):
        """
        Tests getting sunhours, where the return value from get_weather_data is mocked
        to see if get_sun_hour retrieves data correctly.
        """
        mocked_response = Mock()
        data = {"sunHours": 3.2}
        mocked_response.json.return_value = data
        mocked_get.return_value = mocked_response

        input_date = date(2021, 8, 1)
        postcode = "3800"
        res = self.calculator.get_sun_hour(input_date, postcode)
        expected_output = 3.2
        self.assertEqual(res, expected_output, msg=("Expected %s, got %s" % (expected_output, res)))

    @patch('app.calculator.Calculator.get_weather_data')
    def test_SunHours_2(self, mocked_get):
        """
        Tests getting sunhours, where the return value from get_weather_data is mocked
        to see if get_sun_hour retrieves data correctly.
        """
        mocked_response = Mock()
        data = {"sunHours": 3.5}
        mocked_response.json.return_value = data
        mocked_get.return_value = mocked_response

        input_date = date(2021, 8, 2)
        postcode = "4000"
        res = self.calculator.get_sun_hour(input_date, postcode)
        expected_output = 3.5
        self.assertEqual(res, expected_output, msg=("Expected %s, got %s" % (expected_output, res)))

    @patch('app.calculator.Calculator.get_weather_data')
    def test_SunHours_3(self, mocked_get):
        """
        Tests getting sunhours, where the return value from get_weather_data is mocked
        to see if get_sun_hour retrieves data correctly.
        """
        mocked_response = Mock()
        data = {"sunHours": 2.6}
        mocked_response.json.return_value = data
        mocked_get.return_value = mocked_response

        input_date = date(2021, 8, 20)
        postcode = "3200"
        res = self.calculator.get_sun_hour(input_date, postcode)
        expected_output = 2.6
        self.assertEqual(res, expected_output, msg=("Expected %s, got %s" % (expected_output, res)))

    @patch('app.calculator.requests.get')
    def test_SunHours_error_invalid_postcode_1(self, mocked_get):
        """
        Tests getting sunhours, where the return value from requests.get is mocked
        to see if get_sun_hour raises error correctly.
        """
        data = []
        mocked_response = Mock()
        mocked_response.json.return_value = data
        mocked_response.status_code = 200
        mocked_get.return_value = mocked_response

        with self.assertRaises(ValueError):
            self.calculator.get_sun_hour(postcode="0000", input_date=date(year=2021, month=8, day=20))

    @patch('app.calculator.requests.get')
    def test_SunHours_error_invalid_postcode_2(self, mocked_get):
        """
        Tests getting sunhours, where the return value from requests.get is mocked
        to see if get_sun_hour raises error correctly.
        """
        data = [1, 2, 3, 4, 5]
        mocked_response = Mock()
        mocked_response.json.return_value = data
        mocked_response.status_code = 400
        mocked_get.return_value = mocked_response

        with self.assertRaises(ValueError):
            self.calculator.get_sun_hour(postcode="00", input_date=date(year=2021, month=8, day=20))

    @patch('app.calculator.requests.get')
    def test_SunHours_error_invalid_date(self, mocked_get):
        """
        Tests getting sunhours, where the return value from requests.get is mocked
        to see if get_sun_hour raises error correctly.
        """
        data = {"statusCode": 400,
                "message": "Date must be specified, formatted in YYYY-MM-DD and be between 2008-07-01 and 2021-09-17.",
                "error": "Bad Request"}
        mocked_response = Mock()
        mocked_response.json.return_value = data
        mocked_response.status_code = 400
        mocked_get.return_value = mocked_response
        with self.assertRaises(ValueError):
            self.calculator.get_sun_hour(postcode="4000", input_date=date(year=2000, month=8, day=20))

    @patch('app.calculator.requests.get')
    def test_SunHours_error_invalid_date2(self, mocked_get):
        """
        Tests getting sunhours, where the return value from requests.get is mocked
        to see if get_sun_hour raises error correctly.
        """
        data = [{"id": "81a5f4b3-df47-4c20-ba2a-ea025e6ac0f8"}]
        mocked_response = Mock()
        mocked_response.json.return_value = data
        mocked_response.status_code = 400
        mocked_get.return_value = mocked_response

        with self.assertRaises(ValueError):
            self.calculator.get_sun_hour(postcode="4000", input_date="2020/1/1")


class TestGetSunriseSunSet(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    @patch('app.calculator.Calculator.get_weather_data')
    def test_SRSS_1(self, mocked_get):
        """
        Test getting sunrise and sunset, where the return value from
        get_Weather_data is mocked to see if get_sunrise_sunset function
        retrieves the sunrise and sunset value and returns them correctly in time type
        """
        mocked_response = Mock()
        data = {"sunrise": "07:20:00",
                "sunset": "17:32:00"}
        mocked_response.json.return_value = data
        mocked_get.return_value = mocked_response

        input_date = date(2021, 8, 1)
        postcode = "3800"
        res = self.calculator.get_sunrise_sunset(input_date, postcode)
        expected_sunrise = time(hour=7, minute=20, second=0)
        expected_sunset = time(hour=17, minute=32, second=0)
        expected_output = (expected_sunrise, expected_sunset)
        self.assertEqual(expected_sunrise, res[0], msg=("Expected %s, got %s" % (expected_sunrise, res[0])))
        self.assertEqual(expected_sunset, res[1], msg=("Expected %s, got %s" % (expected_sunset, res[1])))

    @patch('app.calculator.Calculator.get_weather_data')
    def test_SRSS_2(self, mocked_get):
        """
        Test getting sunrise and sunset, where the return value from
        get_Weather_data is mocked to see if get_sunrise_sunset function
        retrieves the sunrise and sunset value and returns them correctly in time type
        """
        mocked_response = Mock()
        data = {"sunrise": "06:28:00",
                "sunset": "17:20:00"}
        mocked_response.json.return_value = data
        mocked_get.return_value = mocked_response

        input_date = date(2021, 8, 2)
        postcode = "4000"
        res = self.calculator.get_sunrise_sunset(input_date, postcode)
        expected_sunrise = time(hour=6, minute=28, second=0)
        expected_sunset = time(hour=17, minute=20, second=0)
        expected_output = (expected_sunrise, expected_sunset)
        self.assertEqual(expected_sunrise, res[0], msg=("Expected %s, got %s" % (expected_sunrise, res[0])))
        self.assertEqual(expected_sunset, res[1], msg=("Expected %s, got %s" % (expected_sunset, res[1])))

    @patch('app.calculator.requests.get')
    def test_SRSS_3(self, mocked_get):
        """
        We test what happens if we give an invalid date type.
        Here we mock the response from the api, making it a success and giving it a return
        list of dictionary so that the code can retrieve the location id.
        """
        data = [{"id": "81a5f4b3-df47-4c20-ba2a-ea025e6ac0f8"}]
        mocked_response = Mock()
        mocked_response.json.return_value = data
        mocked_response.status_code = 200
        mocked_get.return_value = mocked_response

        input_date = "2020/1/1"
        postcode = "4000"
        with self.assertRaises(AttributeError):
            res = self.calculator.get_sunrise_sunset(input_date, postcode)

    @patch('app.calculator.requests.get')
    def test_SRSS_4(self, mocked_get):
        """
        Test getting sunrise and sunset, where the return value from
        requests.get is mocked to see if get_sunrise_sunset function
        raises error correctly
        """
        data = []
        mocked_response = Mock()
        mocked_response.json.return_value = data
        mocked_response.status_code = 400
        mocked_get.return_value = mocked_response
        input_date = date(2020, 1, 1)
        postcode = "0"
        with self.assertRaises(ValueError):
            res = self.calculator.get_sunrise_sunset(input_date, postcode)

    @patch('app.calculator.requests.get')
    def test_SRSS_5(self, mocked_get):
        """
        Test getting sunrise and sunset, where the return value from
        requests.get is mocked to see if get_sunrise_sunset function
        raises error correctly
        """
        data = []
        mocked_response = Mock()
        mocked_response.json.return_value = data
        mocked_response.status_code = 200
        mocked_get.return_value = mocked_response
        input_date = date(2020, 1, 1)
        postcode = "0000"
        with self.assertRaises(ValueError):
            res = self.calculator.get_sunrise_sunset(input_date, postcode)


class TestCloudCover(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    @patch('app.calculator.Calculator.get_weather_data')
    def test_cloud_cover_1(self, mocked_get):
        """
        We test get_cloud_cover by mocking the return value from get_weather_data
        where the return value contains the hourlyWeatherHistory, and we see if
        get_cloud_cover will correctly retrieve them into a list
        """
        mocked_response = Mock()
        data = {"hourlyWeatherHistory":
                    [{"hour": 0, "cloudCoverPct": 12}, {"hour": 1, "cloudCoverPct": 12},
                     {"hour": 2, "cloudCoverPct": 12}, {"hour": 3, "cloudCoverPct": 13},
                     {"hour": 4, "cloudCoverPct": 13}, {"hour": 5, "cloudCoverPct": 12},
                     {"hour": 6, "cloudCoverPct": 12}, {"hour": 7, "cloudCoverPct": 13},
                     {"hour": 8, "cloudCoverPct": 13}, {"hour": 9, "cloudCoverPct": 14},
                     {"hour": 10, "cloudCoverPct": 13}, {"hour": 11, "cloudCoverPct": 12},
                     {"hour": 12, "cloudCoverPct": 11}, {"hour": 13, "cloudCoverPct": 20},
                     {"hour": 14, "cloudCoverPct": 29}, {"hour": 15, "cloudCoverPct": 37},
                     {"hour": 16, "cloudCoverPct": 48}, {"hour": 17, "cloudCoverPct": 59},
                     {"hour": 18, "cloudCoverPct": 69}, {"hour": 19, "cloudCoverPct": 75},
                     {"hour": 20, "cloudCoverPct": 81}, {"hour": 21, "cloudCoverPct": 87},
                     {"hour": 22, "cloudCoverPct": 79}, {"hour": 23, "cloudCoverPct": 72}]}
        mocked_response.json.return_value = data
        mocked_get.return_value = mocked_response

        input_date = date(2021, 8, 2)
        postcode = "4000"
        excepted_list = [12, 12, 12, 13, 13, 12, 12, 13,
                         13, 14, 13, 12, 11, 20, 29, 37,
                         48, 59, 69, 75, 81, 87, 79, 72]
        res = self.calculator.get_cloud_cover(input_date, postcode)
        self.assertEqual(res, excepted_list, msg=("Excepted %s, got %s" % (excepted_list, res)))

    @patch('app.calculator.Calculator.get_weather_data')
    def test_cloud_cover_2(self, mocked_get):
        """
        We test get_cloud_cover by mocking the return value from get_weather_data
        where the return value contains the hourlyWeatherHistory, and we see if
        get_cloud_cover will correctly retrieve them into a list
        """
        mocked_response = Mock()
        data = {"hourlyWeatherHistory":
                    [{"hour": 0, "cloudCoverPct": 100}, {"hour": 1, "cloudCoverPct": 94},
                     {"hour": 2, "cloudCoverPct": 87}, {"hour": 3, "cloudCoverPct": 81},
                     {"hour": 4, "cloudCoverPct": 79}, {"hour": 5, "cloudCoverPct": 78},
                     {"hour": 6, "cloudCoverPct": 76}, {"hour": 7, "cloudCoverPct": 78},
                     {"hour": 8, "cloudCoverPct": 80}, {"hour": 9, "cloudCoverPct": 82},
                     {"hour": 10, "cloudCoverPct": 67}, {"hour": 11, "cloudCoverPct": 51},
                     {"hour": 12, "cloudCoverPct": 35}, {"hour": 13, "cloudCoverPct": 30},
                     {"hour": 14, "cloudCoverPct": 24}, {"hour": 15, "cloudCoverPct": 18},
                     {"hour": 16, "cloudCoverPct": 18}, {"hour": 17, "cloudCoverPct": 19},
                     {"hour": 18, "cloudCoverPct": 19}, {"hour": 19, "cloudCoverPct": 16},
                     {"hour": 20, "cloudCoverPct": 13}, {"hour": 21, "cloudCoverPct": 10},
                     {"hour": 22, "cloudCoverPct": 8}, {"hour": 23, "cloudCoverPct": 7}]}
        mocked_response.json.return_value = data
        mocked_get.return_value = mocked_response

        input_date = date(2021, 8, 1)
        postcode = "3800"
        excepted_list = [100, 94, 87, 81, 79, 78, 76, 78,
                         80, 82, 67, 51, 35, 30, 24, 18,
                         18, 19, 19, 16, 13, 10, 8, 7]
        res = self.calculator.get_cloud_cover(input_date, postcode)
        self.assertEqual(res, excepted_list, msg=("Excepted %s, got %s" % (excepted_list, res)))

    @patch('app.calculator.requests.get')
    def test_cloud_cover_3(self, mocked_get):
        """
        We test get_cloud_cover, mocking the request and seeing if error is raised
        """
        data = [{"id": "ab9f494f-f8a0-4c24-bd2e-2497b99f2258"}]
        mocked_response = Mock()
        mocked_response.json.return_value = data
        mocked_response.status_code = 200
        mocked_get.return_value = mocked_response

        input_date = "2020/1/1"
        postcode = "3800"
        with self.assertRaises(AttributeError):
            res = self.calculator.get_cloud_cover(input_date, postcode)

    @patch('app.calculator.requests.get')
    def test_cloud_cover_4(self, mocked_get):
        """
        We test get_cloud_cover,mocking the request and seeing if error is raised
        """
        data = [1, 2, 3, 4]
        mocked_response = Mock()
        mocked_response.json.return_value = data
        mocked_response.status_code = 400
        mocked_get.return_value = mocked_response

        input_date = date(2020, 1, 1)
        postcode = "00"
        with self.assertRaises(ValueError):
            res = self.calculator.get_cloud_cover(input_date, postcode)

    @patch('app.calculator.requests.get')
    def test_cloud_cover_5(self, mocked_get):
        """
        We test get_cloud_cover,mocking the request and seeing if error is raised
        """
        data = []
        mocked_response = Mock()
        mocked_response.json.return_value = data
        mocked_response.status_code = 200
        mocked_get.return_value = mocked_response

        input_date = date(2020, 1, 1)
        postcode = "0000"
        with self.assertRaises(ValueError):
            res = self.calculator.get_cloud_cover(input_date, postcode)


class TestGetWeatherData(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    @patch('app.calculator.requests.get')
    def test_invalid_postcode_get_weather_data_tc1(self, mocked_get):
        """
        We test get_weather_data,mocking the request and seeing if error is raised
        """
        data = [1, 2, 3]
        mocked_response = Mock()
        mocked_response.json.return_value = data
        mocked_response.status_code = 400
        mocked_get.return_value = mocked_response
        with self.assertRaises(ValueError):
            self.calculator.get_weather_data(date(2021, 8, 1), "000")

    @patch('app.calculator.requests.get')
    def test_invalid_postcode_get_weather_data_tc2(self, mocked_get):
        """
        We test get_weather_data,mocking the request and seeing if error is raised
        """
        data = []
        mocked_response = Mock()
        mocked_response.json.return_value = data
        mocked_response.status_code = 200
        mocked_get.return_value = mocked_response
        with self.assertRaises(ValueError):
            self.calculator.get_weather_data(date(2021, 8, 1), "0000")

    @patch('app.calculator.requests.get')
    def test_invalid_date_get_weather_data_tc3(self, mocked_get):
        """
        We test get_weather_data,mocking the request and seeing if error is raised
        """
        data = [{"id": "81a5f4b3-df47-4c20-ba2a-ea025e6ac0f8"}]
        mocked_response = Mock()
        mocked_response.json.return_value = data
        mocked_response.status_code = 400
        mocked_get.return_value = mocked_response

        with self.assertRaises(ValueError):
            self.calculator.get_weather_data(date(2000, 1, 1), "4000")

    @patch('app.calculator.requests.get')
    def test_get_weather_data_invalid_status_code(self, mocked_get):
        data_1 = [{"id": "81a5f4b3-df47-4c20-ba2a-ea025e6ac0f8"}]
        mocked_response_1 = Mock()
        mocked_response_1.json.return_value = data_1
        mocked_response_1.status_code = 200
        data_2 = {"date": "2019-12-01"}
        mocked_response_2 = Mock()
        mocked_response_2.json.return_value = data_2
        mocked_response_2.status_code = 400
        mocked_get.side_effect = [mocked_response_1, mocked_response_2]
        with self.assertRaises(ValueError):
            res = self.calculator.get_weather_data(date(2019, 12, 1), "4000")
            self.assertEqual(res, None)

    @patch('app.calculator.requests.get')
    def test_month_greater_10_get_weather_data(self, mocked_get):
        """
        Test branch of when the month is greater or equal to 10, for coverage.
        Mocks for ConnectionError, Timeout, then mocks appropriate response
        of the two requests to get weather data.
        """
        data_1 = [{"id": "81a5f4b3-df47-4c20-ba2a-ea025e6ac0f8"}]
        mocked_response_1 = Mock()
        mocked_response_1.json.return_value = data_1
        mocked_response_1.status_code = 200
        data_2 = {"date": "2019-12-01"}
        mocked_response_2 = Mock()
        mocked_response_2.json.return_value = data_2
        mocked_response_2.status_code = 200

        mocked_get.side_effect = [ConnectionError, Timeout, mocked_response_1, mocked_response_2]
        with self.assertRaises(ConnectionError):
            res = self.calculator.get_weather_data(date(2019, 12, 1), "4000")
            self.assertEqual(res, None)
        with self.assertRaises(Timeout):
            res = self.calculator.get_weather_data(date(2019, 12, 1), "4000")
            self.assertEqual(res, None)

        res = self.calculator.get_weather_data(date(2019, 12, 1), "4000")
        self.assertEqual(res.json().get("date"), "2019-12-01")

    @patch('app.calculator.requests.get')
    def test_month_lesser_10_get_weather_data(self, mocked_get):
        """
        Test branch of when the month is greater or equal to 10, for coverage.
        Mocks for ConnectionError, Timeout, then mocks appropriate response
        of the two requests to get weather data.
        """
        data_1 = [{"id": "81a5f4b3-df47-4c20-ba2a-ea025e6ac0f8"}]
        mocked_response_1 = Mock()
        mocked_response_1.json.return_value = data_1
        mocked_response_1.status_code = 200
        data_2 = {"date": "2019-09-01"}
        mocked_response_2 = Mock()
        mocked_response_2.json.return_value = data_2
        mocked_response_2.status_code = 200

        mocked_get.side_effect = [ConnectionError, Timeout, mocked_response_1, mocked_response_2]
        with self.assertRaises(ConnectionError):
            res = self.calculator.get_weather_data(date(2019, 9, 1), "4000")
            self.assertEqual(res, None)
        with self.assertRaises(Timeout):
            res = self.calculator.get_weather_data(date(2019, 9, 1), "4000")
            self.assertEqual(res, None)

        res = self.calculator.get_weather_data(date(2019, 9, 1), "4000")
        self.assertEqual(res.json().get("date"), "2019-09-01")

    @patch('app.calculator.requests.get')
    def test_day_lesser_10_get_weather_data(self, mocked_get):
        """
        Test branch of when the month is greater or equal to 10, for coverage.
        Mocks for ConnectionError, Timeout, then mocks appropriate response
        of the two requests to get weather data.
        """
        data_1 = [{"id": "81a5f4b3-df47-4c20-ba2a-ea025e6ac0f8"}]
        mocked_response_1 = Mock()
        mocked_response_1.json.return_value = data_1
        mocked_response_1.status_code = 200
        data_2 = {"date": "2019-09-01"}
        mocked_response_2 = Mock()
        mocked_response_2.json.return_value = data_2
        mocked_response_2.status_code = 200
        mocked_get.side_effect = [ConnectionError, Timeout, mocked_response_1, mocked_response_2]
        with self.assertRaises(ConnectionError):
            res = self.calculator.get_weather_data(date(2019, 9, 1), "4000")
            self.assertEqual(res, None)
        with self.assertRaises(Timeout):
            res = self.calculator.get_weather_data(date(2019, 9, 1), "4000")
            self.assertEqual(res, None)

        res = self.calculator.get_weather_data(date(2019, 9, 1), "4000")
        self.assertEqual(res.json().get("date"), "2019-09-01")

    @patch('app.calculator.requests.get')
    def test_day_greater_10_get_weather_data(self, mocked_get):
        """
        Test branch of when the month is greater or equal to 10, for coverage.
        Mocks for ConnectionError, Timeout, then mocks appropriate response
        of the two requests to get weather data.
        """
        data_1 = [{"id": "81a5f4b3-df47-4c20-ba2a-ea025e6ac0f8"}]
        mocked_response_1 = Mock()
        mocked_response_1.json.return_value = data_1
        mocked_response_1.status_code = 200
        data_2 = {"date": "2019-09-10"}
        mocked_response_2 = Mock()
        mocked_response_2.json.return_value = data_2
        mocked_response_2.status_code = 200
        mocked_get.side_effect = [ConnectionError, Timeout, mocked_response_1, mocked_response_2]
        with self.assertRaises(ConnectionError):
            res = self.calculator.get_weather_data(date(2019, 12, 1), "4000")
            self.assertEqual(res, None)
        with self.assertRaises(Timeout):
            res = self.calculator.get_weather_data(date(2019, 12, 1), "4000")
            self.assertEqual(res, None)


        res = self.calculator.get_weather_data(date(2019, 9, 10), "4000")
        self.assertEqual(res.json().get("date"), "2019-09-10")


if __name__ == "__main__":
    # create the test suit from the cases above.
    dayLightSuit = unittest.TestLoader().loadTestsFromTestCase(TestDaylightLength)
    sunHoursSuit = unittest.TestLoader().loadTestsFromTestCase(TestSunHours)
    weather_data_suit = unittest.TestLoader().loadTestsFromTestCase(TestGetWeatherData)
    # this will run the test suit
    unittest.TextTestRunner(verbosity=2).run(sunHoursSuit)
    unittest.TextTestRunner(verbosity=2).run(dayLightSuit)
    unittest.TextTestRunner(verbosity=2).run(weather_data_suit)
