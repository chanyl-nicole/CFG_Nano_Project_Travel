import unittest
from unittest.mock import patch
from main import choose_city, choose_month

class ChooseCityTestCase(unittest.TestCase):
    """Tests for choosing city function"""

    user_choice = ['Rome']
    @patch('main.get_city_weather', return_value={'Rome': 'Rainy and Warm'})
    @patch('builtins.input', side_effect=user_choice)
    def test_can_choose_city_in_options(self, mock_inputs, a):
        """Test to check user can choose city  in options"""
        result = choose_city('June')
        self.assertEqual(result, 'Rome')

    user_choice = ['New York', 'Rome']

    @patch('main.get_city_weather', return_value={'Rome': 'Rainy and Warm'})
    @patch('builtins.input', side_effect=user_choice)
    def test_cannot_choose_city_not_in_options(self, mock_inputs, a):
        """Test to check user can't choose city not in options"""
        result = choose_city('June')
        self.assertEqual(result, 'Rome')

    user_choice = ['rome']

    @patch('main.get_city_weather', return_value={'Rome': 'Rainy and Warm'})
    @patch('builtins.input', side_effect=user_choice)
    def test_for_lower_case_letters_cities(self, mock_inputs, a):
        """Test to check input works if user starts the city name with a lower case letter"""
        result = choose_city('June')
        self.assertEqual(result, 'Rome')

    user_choice = ['roMe']

    @patch('main.get_city_weather', return_value={'Rome': 'Rainy and Warm'})
    @patch('builtins.input', side_effect=user_choice)
    def test_for_upper_case_letters_cities(self, mock_inputs, a):
        """Test to check that input works if user types a capital letter in the word"""
        result = choose_city('June')
        self.assertEqual(result, 'Rome')

class ChooseMonthTestCase(unittest.TestCase):
    """Tests for choosing month function"""

    user_choice = ['June']
    @patch('main.get_month_choices', return_value=[['June']])
    @patch('builtins.input', side_effect=user_choice)
    def test_only_choose_month_in_options(self, mock_inputs, a):
        """Test to check user can choose month in options"""
        result = choose_month()
        self.assertEqual(result, 'June')

    user_choice = ['May', 'June']
    @patch('main.get_month_choices', return_value=[['June']])
    @patch('builtins.input', side_effect=user_choice)
    def test_only_choose_month_in_options(self, mock_inputs, a):
        """Test to check user can't choose month not in options"""
        result = choose_month()
        self.assertEqual(result, 'June')

    user_choice = ['june']
    @patch('main.get_month_choices', return_value=[['June']])
    @patch('builtins.input', side_effect=user_choice)
    def test_for_lower_case_letters_months(self, mock_inputs, a):
        """Test to check input works if user starts the month with a lower case letter"""
        result = choose_month()
        self.assertEqual(result, 'June')

    user_choice = ['juNe']
    @patch('main.get_month_choices', return_value=[['June']])
    @patch('builtins.input', side_effect=user_choice)
    def test_for_upper_case_letters_months(self, mock_inputs, a):
        """Test to check input works if user users capital letters in month"""
        result = choose_month()
        self.assertEqual(result, 'June')

if __name__ == '__main__':
    unittest.main()

#to run first time in terminal: python3 -m unittest tests.py










