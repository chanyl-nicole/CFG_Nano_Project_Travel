import unittest
from unittest.mock import patch
from main import choose_city

class ChooseCityTestCase(unittest.TestCase):
    """Tests for choosing city function"""

    list_of_cities = ['Rome', 'London', 'Santorini', 'Swiss Alps']
    user_choice = 'Rome'

    @patch('builtins.input', side_effect=[user_choice, list_of_cities])
    def test_only_choose_city_in_options(self, mock_inputs):
        result = choose_city('June')
        self.assertIn(result, 'Rome')

# class ChooseCityTestCase(unittest.TestCase):
#     """Tests for choosing city function"""
#
#     list_of_cities = ['Rome', 'London', 'Santorini', 'Swiss Alps']
#     user_choice = 'New York'
#
#     @patch('builtins.input', side_effect=[user_choice, list_of_cities])
#     def test_cannot_choose_city_not_in_options(self, mock_inputs):
#         result = choose_city('June')
#         self.assertNotIn(result, 'New York')








