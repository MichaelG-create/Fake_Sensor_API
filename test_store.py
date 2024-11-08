from datetime import date

import pandas as pd
import unittest

from sensor_app import Sensor
from store_app import Store


class TestStore(unittest.TestCase):
    """
    tests to do:
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

    # def tearDown(self):
    #     # This method is run after each test
    #     print("Cleaning up after test")

    def test_closed_on_sunday(self) -> None:
        sunday_date = date(2024, 11, 3)
        self.assertTrue(
            -1 == self.sensor.simulate_visit_count(sunday_date),
            f"error : opened this sunday : {sunday_date} with {self.sensor.simulate_visit_count(sunday_date)} visitors",
        )

    # needs to be tested over a set of weekday date (monday, tuesday, wednesday, thursday, friday, saturday
    def test_opened_on_worked_days(self):
        weekday_list = pd.date_range(date(2024, 11, 4), date(2024, 11, 9))
        for weekday_date in weekday_list:
            self.assertTrue(
                -1 != self.sensor.simulate_visit_count(weekday_date),
                f"error : should be opened this weekday : {weekday_date} but got {self.sensor.simulate_visit_count(weekday_date)} visitors",
            )

    def test_malfunction_day(self) -> None:
        malfunction_date = date(2022, 2, 17)
        self.assertTrue(
            401 == self.sensor.simulate_visit_count(malfunction_date),
            (
                f"error : should malfunction this days {malfunction_date} "
                f"but got {self.sensor.simulate_visit_count(malfunction_date)} visitors instead of 401"
            ),
        )

    def test_break_day(self) -> None:
        break_date = date(2022, 2, 4)
        self.assertTrue(
            0 == self.sensor.simulate_visit_count(break_date),
            f"error : should be broken this day : {break_date}, got {self.sensor.simulate_visit_count(break_date)} visitors instead of 0",
        )


if __name__ == "__main__":
    # meaning : do this only if the script is directly run (__name__ = __main__')
    # When it’s imported as a module in another file, __name__ is set to the name of the file/module
    # (without the .py extension).

    # use this to run the tests with the above created class
    unittest.main()
