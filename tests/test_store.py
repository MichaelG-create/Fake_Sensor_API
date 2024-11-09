"""test class Store"""

import unittest
from datetime import date

from data_app import Store


class TestStore(unittest.TestCase):
    """
    tests to do:
    - tests on sensors in fact not directly store ?
    - can test methods (get_tot
    """

    def test_get_all_traffic(self):
        """test all traffic should be 752 in this store this date"""
        lille_store = Store("Lille", 1200, 300)
        visits = lille_store.get_all_traffic(date(2023, 9, 13))
        self.assertEqual(visits, 752)

    def test_get_sensor_traffic(self):
        """test traffic of sensor 2 should be 151 in this store this date"""
        lille_store = Store("Lille", 1200, 300)
        visits = lille_store.get_sensor_traffic(2, date(2023, 9, 13))
        self.assertEqual(
            visits, 151
        )  # something around 20% of (average +10%) (wednesday)

    def test_sunday_closed(self):
        """test traffic of sensor 2 should be -1 in this store this sunday"""
        lille_store = Store("Lille", 1200, 300)
        visits = lille_store.get_sensor_traffic(2, date(2023, 9, 17))
        self.assertEqual(visits, -1)


if __name__ == "__main__":
    # meaning : do this only if the script is directly run (__name__ = __main__')
    # When it’s imported as a module in another file, __name__ is set to the name of the file/module
    # (without the .py extension).

    # use this to run the tests with the above created class
    unittest.main()
