# Exercise 11-1 & 11-2; Page 215/216

import unittest
from city_functions import format_city

class CitiesTestCase(unittest.TestCase):
    """Tests for city_functions.py"""

    def test_city_country(self):
        """Do cities like 'Santiago, Chile' work?"""
        formatted_city = format_city('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')

    def test_city_country_population(self):
        """Do cities like 'Santiago, Chile - Population 5000000' work?"""
        formatted_city = format_city('santiago', 'chile', 5000000)
        self.assertEqual(formatted_city, 'Santiago, Chile - Population 5000000')

if __name__ == '__main__':
    unittest.main()