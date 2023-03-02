from datetime import datetime, date, time, timedelta
import holidays
import requests
import dateutil.relativedelta

class Calculator():
    # you can choose to initialise variables here, if needed.
    def __init__(self):
        self.configuration = [[2, 5],
                              [3.6, 7.5],
                              [7.2, 10],
                              [11, 12.5],
                              [22, 15],
                              [36, 20],
                              [90, 30],
                              [350, 50]]
        # self.selection = None  this is for location ID selection
        self.previous_postcode = None
        self.previous_date = None
        self.api_data = None
        self.valid_states = ["ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"]
        self.location_data = {}
        self.weather_data = {}

        self.EARLIEST_DATE = date(2008, 7, 1)
        self.PANEL_SIZE = 50
        self.PANEL_EFFICIENCY = 0.2

    # you may add more parameters if needed, you may modify the formula also.
    def cost_calculation(self, initial_state: float, final_state: float, capacity: float,
                         is_peak: bool, is_holiday: bool, base_price: float) -> float:
        if initial_state < 0 or initial_state > 100:
            raise ValueError
        if final_state < initial_state or final_state > 100:
            raise ValueError
        if capacity < 0:
            raise ValueError
        if base_price < 0:
            raise ValueError

        if is_peak:
            peak_modifier = 1
        else:
            peak_modifier = 0.5

        if is_holiday:
            surcharge_factor = 1.1
        else:
            surcharge_factor = 1
        cost = ((final_state - initial_state) / 100) * capacity * \
            (base_price / 100) * surcharge_factor * peak_modifier
        return cost

    # you may add more parameters if needed, you may also modify the formula.
    def time_calculation(self, initial_state: float, final_state: float, capacity: float, power: float) -> float:
        if initial_state < 0 or initial_state > 100:
            raise ValueError
        if final_state < initial_state or final_state > 100:
            raise ValueError
        if capacity < 0:
            raise ValueError
        if power < 0:
            raise ValueError

        time = (final_state - initial_state) / 100 * capacity / power
        return time

    # you may create some new methods at your convenience, or modify these methods, or choose not to use them.
    def get_configuration(self, config: int):
        if config < 1 or config > 8:
            raise ValueError
        return self.configuration[config - 1]

    def is_holiday(self, start_date: date, state: str) -> bool:
        is_weekday = (start_date.weekday() < 5)
        state_holiday = holidays.Australia(prov=state)
        if state not in self.valid_states:
            raise ValueError
        return is_weekday or start_date in state_holiday  # or start_date in self.school_holidays[state]

    def is_peak(self, start_time: time) -> bool:
        left_peak = time(6)
        right_peak = time(18)
        return left_peak <= start_time < right_peak

    def get_end_time(self, start_date: date, start_time: time, charge_time: float):
        if charge_time < 0:
            raise ValueError
        starting_date_time = datetime.combine(start_date, start_time)
        time_to_add = timedelta(hours=charge_time)
        return starting_date_time + time_to_add

    def get_weather_data(self, input_date: date, postcode: str):
        """
        Returns all the weather data for the given date and postcode
        :param input_date: Date of the weather data
        :param postcode: Postcode/location of the weather data
        :return: Weather data, in requests data type
        """
        locationURL = "http://118.138.246.158/api/v1/location?postcode="
        if self.location_data.get(postcode) is None:
            requestLocationURL = locationURL + postcode
            resLocation = requests.get(url=requestLocationURL)
            if resLocation.status_code != 200:
                raise ValueError("Invalid postcode")
            if len(resLocation.json()) == 0:
                raise ValueError("Invalid postcode")
            self.location_data[postcode] = resLocation
        else:
            resLocation = self.location_data[postcode]

        locationID = resLocation.json()[0].get("id")
        if input_date.month < 10:
            month = "0" + str(input_date.month)
        else:
            month = str(input_date.month)
        if input_date.day < 10:
            day = "0" + str(input_date.day)
        else:
            day = str(input_date.day)
        dateRequest = "location=%s&date=%s-%s-%s" % (locationID, input_date.year, month, day)
        if self.weather_data.get(dateRequest) is None:
            weatherURL = "http://118.138.246.158/api/v1/weather?%s" % (dateRequest)
            resWeather = requests.get(url=weatherURL)
            if resWeather.status_code != 200:
                raise ValueError("Could not get weather data")
            self.weather_data[dateRequest] = resWeather
        else:
            resWeather = self.weather_data[dateRequest]
        return resWeather

    # to be acquired through API
    def get_sun_hour(self, input_date: date, postcode: str) -> float:
        """
        Returns the sun hour data for solar energy calculation of this date and postcode
        :param input_date: Date of the data
        :param postcode: Postcode/location of the data
        :return: Sun hour data for the given date and postcode
        """
        resWeather = self.get_weather_data(input_date, postcode)
        return resWeather.json().get("sunHours")

    def get_sunrise_sunset(self, input_date: date, postcode: str):
        """
        Returns the sunrise and sunset time data type in a tuple, given date and postcode
        :param input_date: Date to get the data
        :param postcode: Location/Postcode of the data
        :return: Sunrise and sunset, in time type, in a tuple.
        """
        resWeather = self.get_weather_data(input_date, postcode)
        sunrise_arr = resWeather.json().get("sunrise").split(":")
        sunrise = time(hour=int(sunrise_arr[0]), minute=int(
            sunrise_arr[1]), second=int(sunrise_arr[2]))
        sunset_arr = resWeather.json().get("sunset").split(":")
        sunset = time(hour=int(sunset_arr[0]), minute=int(
            sunset_arr[1]), second=int(sunset_arr[2]))
        return (sunrise, sunset)

    # to be acquired through API
    # Calculate it yourself for each day
    # get the sunrise and sunset, min max the start and the end, then just get the
    # difference and convert it to hours or something.
    def get_solar_energy_duration(self, start_time: time, end_time: time, input_date: date, postcode: str):
        # THIS FUNCTION SHOULD ONLY BE USED FOR REQ 2!
        # Tell me if u want me to change this to better suit need (NYK)

        if start_time > end_time:
            raise ValueError

        sunrise_sunset = self.get_sunrise_sunset(input_date, postcode)

        if start_time >= sunrise_sunset[1]:
            return 0
        if end_time <= sunrise_sunset[0]:
            return 0

        start_time_actual = max(start_time, sunrise_sunset[0])
        end_time_actual = min(end_time, sunrise_sunset[1])
        start_time_delta = timedelta(hours=int(start_time_actual.hour),
                                     minutes=int(start_time_actual.minute),
                                     seconds=int(start_time_actual.second))
        end_time_delta = timedelta(hours=int(end_time_actual.hour),
                                   minutes=int(end_time_actual.minute),
                                   seconds=int(end_time_actual.second))
        duration = (end_time_delta -
                    start_time_delta).total_seconds() / 60 / 60
        return duration

    # to be acquired through API
    def get_day_light_length(self, input_date: date, postcode: str) -> float:
        """
        Returns the daylight length hours of the given date and postcode
        :param input_date: Date to get the data
        :param postcode: Location/Postcode of the data
        :return: Daylight length hours of the given date and postcode
        """
        sunrise, sunset = self.get_sunrise_sunset(input_date, postcode)
        sunrise_delta = timedelta(
            hours=sunrise.hour, minutes=sunrise.minute, seconds=sunrise.second)
        sunset_delta = timedelta(
            hours=sunset.hour, minutes=sunset.minute, seconds=sunset.second)

        daylight_length = (sunset_delta - sunrise_delta).total_seconds() / 3600
        return daylight_length

    def get_cloud_cover(self, input_date: date, postcode: str) -> list:
        """
        Gets the list of cloud cover values for the given date and postcode.
        :param input_date: Date to find cloud cover values
        :param postcode: Postcode of the location
        :return: List of cloud cover values for hour 0 to hour 23
        """
        resWeather = self.get_weather_data(input_date, postcode)
        resWeatherCloudCoverList = resWeather.json().get("hourlyWeatherHistory")
        resWeatherCloudCoverList = sorted(resWeatherCloudCoverList, key = lambda i: i['hour'])
        res_cloud_clover = []
        for each in resWeatherCloudCoverList:
            hourly_cloud = each.get("cloudCoverPct")
            res_cloud_clover.append(hourly_cloud)
        return res_cloud_clover

    def calculate_solar_energy_past_to_currentday_minus_two(self, start_time_date: datetime,
                                                            end_time_date: datetime, postcode: str):
        """
        Takes in start and end datetimes to calculate solar energy generated based on provided postcode.
        This function can be used to calculate solar energy with duration up to an hour of a specific date.
        Only calculates solar energy between 1st July 2008 to 2 days before current date of input.

        Precondition: start_time_date must be during or after 1st July 2008
                      end_time_date must be 2 days before current date of input
                      start_time_date.date() and end_time_date.date() must be the same
                      start_time_date.time() and end_time_date.time() must have at most an hour interval, inclusive

        :param start_time_date: The starting date and time for solar energy calculation
        :param end_time_date: The ending date and time for solar energy calculation
        :param postcode: The postcode which specifies where the solar energy calculation takes place, since different states may have different solar energy generation
        :return: Total solar energy generated in KWh within the specified start and end datetime at the specified state based on postcode.
        """
        # We first check if start and end times are valid
        # If difference in hour is less 0, means starting time is later than end time
        # If difference in hour is more than 1, means interval between starting time and end time is more than 1 hour, which is not valid
        # Additionally, this also checks if the days are different, since difference in hours will show
        # This works since the app is programmed to call this function again if it reaches a new day.
        # So if range is 01/07/2008 23:30:00 to 02/07/2008 00:30:00, the function should be called twice like so:
        # 01/07/2008 23:30:00 to 01/07/2008 23:59:59, then 02/07/2008 00:00:00 to 02/07/2008 00:30:00
        diff_in_hours = (end_time_date - start_time_date).total_seconds() / 3600
        if diff_in_hours < 0 or diff_in_hours > 1:
            raise ValueError

        # date of this starting datetime
        start_date = start_time_date.date()

        # if the starting date is 1st July 2008 or later
        if start_date >= self.EARLIEST_DATE:
            sun_hour = self.get_sun_hour(start_date, postcode)  # retrieve solar insolation of this date (sun hour)

            daylight_length = self.get_day_light_length(start_date, postcode)  # retrieve daylight length of this date

            start = start_time_date.time()  # get the starting time

            end = end_time_date.time()      # get the end time

            # get the duration of solar energy within this time period (range 0 to 1)
            duration = self.get_solar_energy_duration(start, end, start_date, postcode)

            # finally calculate solar energy generated for the day and add into total sum
            energy = sun_hour * duration / daylight_length * self.PANEL_SIZE * self.PANEL_EFFICIENCY

            return energy

        # this function only calculates solar energy starting from 01/07/2008, so return 0 for anything earlier than this day
        else:
            return 0

    def calculate_solar_energy_future(self, start_time_date: datetime, end_time_date: datetime,
                                      postcode: str):
        """
            This function is to calculate the solar energy generated between start_time_date and end_time_date in the future

            solar insolation,   si
            duration,           du
            daylight length,    dl
            cloud cover,        cc

            CONCEPT
            1) start_time_date and end_time_date will be either whole hour or partial hour
            2) need to identify if both time is within daylight, if not, return 0 directly
            3) if start_time_date is same as sunrise hour, but minute is smaller than sunrise minute, update start_time_point to become sunrise
            4) if end_time_date is same as sunset hour, but minute is larger than sunset minute, update end_time_point to become sunset
            5) get si,du,dl,cc
            6) use it in the formula to get the solar energy generated
            7) return hourly_generated_solar_energy
        """
        sunrise, sunset = self.get_sunrise_sunset(start_time_date.date(), postcode)
        if start_time_date.time() > sunset or end_time_date.time() < sunrise:
            # if the start and end is not within daylight
            return 0

        start_time_point = start_time_date
        end_time_point = end_time_date
        if start_time_date.time() < sunrise:
            start_time_point = datetime.combine(start_time_date.date(),sunrise)
        elif end_time_date.time() > sunset:
            end_time_point = datetime.combine(start_time_date.date(),sunset)

        dl = self.get_day_light_length(start_time_date, postcode)
        si = self.get_sun_hour(start_time_date, postcode)
        cloud_cover_list = self.get_cloud_cover(start_time_date, postcode)
        cc = cloud_cover_list[start_time_point.hour]
        time_dif = (end_time_point - start_time_point)
        du = (time_dif.seconds // 60 % 60) / 60
        # if hour == 1: (means whole hour)
        if time_dif.seconds // 3600 == 1:
            du = 1
        hourly_generated_solar_energy = si * du / dl * (1-cc/100) * 50 * 0.2
        return hourly_generated_solar_energy

    def get_charging_time_str(self, charge_hours: float):

        hours = int(charge_hours)
        decimal_minutes = (charge_hours % 1) * 60
        minutes = int(decimal_minutes)
        seconds = int((decimal_minutes % 1) * 60)
        if charge_hours < 0:
            raise ValueError

        return_str = ""
        if hours > 0:
            if hours == 1:
                return_str += str(hours) + " hour "
            else:
                return_str += str(hours) + " hours "
        if minutes > 0:
            if minutes == 1:
                return_str += str(minutes) + " minute "
            else:
                return_str += str(minutes) + " minutes "
        if seconds > 0:
            if seconds == 1:
                return_str += str(seconds) + " second "
            else:
                return_str += str(seconds) + " seconds "
        return return_str.strip()

    def get_state(self, postcode: str) -> str:
        locationURL = "http://118.138.246.158/api/v1/location?postcode="
        requestLocationURL = locationURL + postcode
        resLocation = requests.get(url=requestLocationURL)
        if resLocation.status_code != 200:
            raise ValueError("Invalid postcode")
        if len(resLocation.json()) == 0:
            raise ValueError("Invalid postcode")
        state = resLocation.json()[0].get("state")
        return state

    # for the calculation of solar energy, should the solar energy generated time splited so that when it span across non-peak hour/holiday stuff the cost will be different
    def total_cost_calculation(self, start_date: date, start_time: time, end_time: datetime,
                               start_state: float, base_price: float, power: float, capacity: float,
                               postcode: str, solar_energy: bool = False) -> float:
        """
            To fulfill requirement 3, precondition will be as follow:
            1) if the date extends to the future, solar_energy by default will have a value of True
            2) the this_year_start and this_year_end time difference will either be whole hour or partial hour
        """
        if start_state < 0 or start_state > 100:
            raise ValueError
        if capacity < 0:
            raise ValueError
        if power < 0:
            raise ValueError
        if base_price < 0:
            raise ValueError
        if type(solar_energy) is not bool:
            raise ValueError

        state = self.get_state(postcode)
        cost = 0
        current_date_time = datetime.combine(start_date, start_time)

        reachedEnd = False
        while (not reachedEnd):
            holiday_surcharge = self.is_holiday(
                current_date_time.date(), state)
            peak = self.is_peak(current_date_time.time())
            added_time = timedelta(hours=1)
            new_datetime = min(end_time, (current_date_time +
                                          added_time).replace(minute=0, second=0, microsecond=0))
            difference_time_minutes = max(
                0, ((new_datetime - current_date_time).total_seconds() / 60))
            power_from_this_charge = (difference_time_minutes) / 60 * power
            # future date is define to be 2 days before today
            if current_date_time > datetime.today() - timedelta(days=2):
                cost_all_year_this_period = 0
                current_year = datetime.now().year
                gap = current_date_time.year - current_year
                # gap will add 1 if current_year is same as the start_year
                if current_date_time - dateutil.relativedelta.relativedelta(years=gap) > (datetime.today() - timedelta(days=2)):
                    gap = gap + 1
                for i in range(3):
                    this_year_start = current_date_time - dateutil.relativedelta.relativedelta(years=i + gap)
                    this_year_end = new_datetime - dateutil.relativedelta.relativedelta(years=i + gap)
                    is_holiday_this_year = self.is_holiday(this_year_start.date(), state)
                    solar_power_this_year = 0
                    if solar_energy:
                        solar_power_this_year = self.calculate_solar_energy_future(this_year_start, this_year_end, postcode)
                    remaining_charge = max(0, (power_from_this_charge - solar_power_this_year))
                    time_remaining_charge = remaining_charge / power
                    fsoc = ((time_remaining_charge * power / capacity) + (start_state / 100)) * 100
                    cost_all_year_this_period += self.cost_calculation(start_state, fsoc, capacity, peak,
                                                                       is_holiday_this_year, base_price)
                cost += cost_all_year_this_period / 3
            else:
                solar_power_this_period = 0
                if solar_energy:
                    solar_power_this_period = \
                        self.calculate_solar_energy_past_to_currentday_minus_two(current_date_time, new_datetime, postcode)
                remaining_charge = max(0, (power_from_this_charge - solar_power_this_period))
                time_remaining_charge = remaining_charge / power
                fsoc = ((time_remaining_charge * power / capacity) + (start_state / 100)) * 100
                cost += self.cost_calculation(start_state, fsoc, capacity, peak, holiday_surcharge, base_price)

            if new_datetime == end_time:
                reachedEnd = True
            current_date_time = new_datetime

        return round(cost, 2)
