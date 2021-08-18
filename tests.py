import unittest
from unittest.mock import patch
from main import SummerTrip

class ChooseCityTestCase(unittest.TestCase):
    """Tests for choosing city function"""

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
#
class ChooseMonthTestCase(unittest.TestCase):
    """Tests for choosing month function"""

    user_choice = ['June']
    @patch('main.SummerTrip.get_month_choices', return_value=[['June']])
    @patch('builtins.input', side_effect=user_choice)
    def test_only_choose_month_in_options(self, mock_inputs, mock_call):
        """Test to check user can choose month in options"""
        summer_trip = SummerTrip()
        result = summer_trip.choose_month()
        self.assertEqual(result, 'June')
#
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
#
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
