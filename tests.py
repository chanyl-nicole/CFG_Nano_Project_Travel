#File for running unit tests on functions

import unittest
from unittest.mock import patch
from main import SummerTrip, TripPlan

class ChooseCityTestCase(unittest.TestCase):
    """Tests for choosing city function in SummerTrip class"""

    user_choice = ['Rome']
    @patch('main.SummerTrip.get_city_weather', return_value={'Rome': 'Rainy and Warm'})
    @patch('builtins.input', side_effect=user_choice)
    def test_can_choose_city_in_options(self, mock_inputs, mock_call):
        """Test to check user can choose city  in options"""
        summer_trip = SummerTrip()
        result = summer_trip.choose_city()
        self.assertEqual(result, 'Rome')

    user_choice = ['New York']

    @patch('main.SummerTrip.get_city_weather', return_value={'Rome': 'Rainy and Warm'})
    @patch('builtins.input', side_effect=user_choice)
    def test_cannot_choose_city_not_in_options(self, mock_inputs, mock_call):
        """Test to check user can't choose city not in options"""
        summer_trip = SummerTrip()
        result = summer_trip.choose_city()
        self.assertEqual(result, None)


    user_choice = ['rome']

    @patch('main.SummerTrip.get_city_weather', return_value={'Rome': 'Rainy and Warm'})
    @patch('builtins.input', side_effect=user_choice)
    def test_for_lower_case_letters_cities(self, mock_inputs, mock_call):
        """Test to check input works if user starts the city name with a lower case letter"""
        summer_trip = SummerTrip()
        result = summer_trip.choose_city()
        self.assertEqual(result, 'Rome')

    user_choice = ['roMe']

    @patch('main.SummerTrip.get_city_weather', return_value={'Rome': 'Rainy and Warm'})
    @patch('builtins.input', side_effect=user_choice)
    def test_for_upper_case_letters_cities(self, mock_inputs, mock_call):
        """Test to check that input works if user types a capital letter in the word"""
        summer_trip = SummerTrip()
        result = summer_trip.choose_city()
        self.assertEqual(result, 'Rome')

    user_choice = ['Rome3']

    @patch('main.SummerTrip.get_city_weather', return_value={'Rome': 'Rainy and Warm'})
    @patch('builtins.input', side_effect=user_choice)
    def test_for_numbers_in_city_input(self, mock_inputs, mock_call):
        """Test to check that input works if user types a number in the word"""
        summer_trip = SummerTrip()
        result = summer_trip.choose_city()
        self.assertEqual(result, 'Rome')

class ChooseMonthTestCase(unittest.TestCase):
    """Tests for choosing month function in SummerTrip class"""

    user_choice = ['June']
    @patch('main.SummerTrip.get_month_choices', return_value=[['June']])
    @patch('builtins.input', side_effect=user_choice)
    def test_only_choose_month_in_options(self, mock_inputs, mock_call):
        """Test to check user can choose month in options"""
        summer_trip = SummerTrip()
        result = summer_trip.choose_month()
        self.assertEqual(result, 'June')

    user_choice = ['May']
    @patch('main.SummerTrip.get_month_choices', return_value=[['June']])
    @patch('builtins.input', side_effect=user_choice)
    def test_only_choose_month_in_options(self, mock_inputs, mock_call):
        """Test to check user can't choose month not in options"""
        summer_trip = SummerTrip()
        result = summer_trip.choose_month()
        self.assertEqual(result, None)

    user_choice = ['june']
    @patch('main.SummerTrip.get_month_choices', return_value=[['June']])
    @patch('builtins.input', side_effect=user_choice)
    def test_for_lower_case_letters_months(self, mock_inputs, mock_call):
        """Test to check input works if user starts the month with a lower case letter"""
        summer_trip = SummerTrip()
        result = summer_trip.choose_month()
        self.assertEqual(result, 'June')

    user_choice = ['juNe']
    @patch('main.SummerTrip.get_month_choices', return_value=[['June']])
    @patch('builtins.input', side_effect=user_choice)
    def test_for_upper_case_letters_months(self, mock_inputs, mock_call):
        """Test to check input works if user users capital letters in month"""
        summer_trip = SummerTrip()
        result = summer_trip.choose_month()
        self.assertEqual(result, 'June')

    user_choice = ['Jun4e']
    @patch('main.SummerTrip.get_month_choices', return_value=[['June']])
    @patch('builtins.input', side_effect=user_choice)
    def test_for_numbers_in_months(self, mock_inputs, mock_call):
        """Test to check input works if user users types a number in month"""
        summer_trip = SummerTrip()
        result = summer_trip.choose_month()
        self.assertEqual(result, 'June')

class WorkingWithItemsTestCase(unittest.TestCase):
    """Tests for adding, removing and viewing items """

    user_item = ['Medication', 'done']
    @patch('db_utils._connect_to_db')
    @patch('builtins.input', side_effect=user_item)
    def test_done_ends_adding_items_to_list(self, mock_inputs, mock_database):
        """Test to check that 'done' will end ability to add items to the list"""
        trip_plan = TripPlan()
        result = trip_plan.add_personal_items()
        self.assertEqual(result, ['Medication'])

    user_item = ['Medication', 'Cards', 'Covid test', 'done']
    @patch('db_utils._connect_to_db')
    @patch('builtins.input', side_effect=user_item)
    def test_adding_multiple_items_to_list(self, mock_inputs, mock_database):
        """Test to check that a user can add more than one item to the list"""
        trip_plan = TripPlan()
        result = trip_plan.add_personal_items()
        self.assertEqual(result, ['Medication', 'Cards', 'Covid Test'])


class CovidAPITestCase(unittest.TestCase):
    city = ['Tokyo']
    @patch('db_utils._connect_to_db')
    @patch('builtins.input', side_effect=city)
    def test_adding_incorrect_city(self, mock_inputs, mock_city):
        """ Test to check if COVID API function will return results for a city that is not specified within db"""
        trip_plan = TripPlan()
        result = trip_plan.get_covid_restrictions()
        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()
#
# #to run first time in terminal: python3 -m unittest tests.py
#
#
#
#
#
#
#
#
#
#
