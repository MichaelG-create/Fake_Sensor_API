from datetime import date

import pandas as pd
import unittest

from data_app import Store
from data_app.sensor import Sensor


class TestStore(unittest.TestCase):
    """
    tests to do:
    - tests on sensors in fact not directly store ?
    - can test methods (get_tot
    """

    def setUp(self):
        # This method is run before each test
        avg_visit_count = 2000
        std_visit_count = 100

        malfunction_chance = 0.035
        break_chance = 0.015

        self.sensor = Sensor(
            avg_visit_count, std_visit_count, malfunction_chance, break_chance
        )

    def test_get_all_traffic(self):
        lille_store = Store("Lille", 1200, 300)
        visits = lille_store.get_all_traffic(date(2023, 9, 13))
        self.assertEqual(visits, 752)

    def test_get_sensor_traffic(self):
        lille_store = Store("Lille", 1200, 300)
        visits = lille_store.get_sensor_traffic(2, date(2023, 9, 13))
        self.assertEqual(
            visits, 151
        )  # something around 20% of (average +10%) (wednesday)

    def test_sunday_closed(self):
        lille_store = Store("Lille", 1200, 300)
        visits = lille_store.get_sensor_traffic(2, date(2023, 9, 17))
        self.assertEqual(visits, -1)


if __name__ == "__main__":
    # meaning : do this only if the script is directly run (__name__ = __main__')
    # When it’s imported as a module in another file, __name__ is set to the name of the file/module
    # (without the .py extension).

    # use this to run the tests with the above created class
    unittest.main()
