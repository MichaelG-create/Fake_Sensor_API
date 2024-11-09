from datetime import date

import pandas as pd
import unittest

from data_app.sensor import Sensor


class TestSensor(unittest.TestCase):
    """
    Test sensor objects:
    - method get_visit_count:
        - -1 on sundays (test one known sunday)
        - not -1 on opened_days (test 6 consecutive known opened_days)
        - small values on malfunction_event days (test one known malfunction_event day with its strange value)
        - 0 on break days (test one known break day with the 0 count)
    - remarks
        - does not test ALL sundays
        - does not test ALL weekdays
        - does not test bank holidays (not implemented)
        - does not check if the distribution of the sensor count
         respects the gaussian low around the mean_value
         with the given std_deviation
        - Could calculate sums to check if mean_count is respected on specific opened_days
        - Could calculate sums to check if mean_count is respected on specific malfunction_days
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
            -1 == self.sensor.get_visit_count(sunday_date),
            (
                f"error : opened this sunday : {sunday_date} "
                f"with {self.sensor.get_visit_count(sunday_date)} visitors",
            ),
        )

    # needs to be tested over a set of weekday date (monday, tuesday, wednesday, thursday, friday, saturday
    def test_opened_on_worked_days(self):
        weekday_list = pd.date_range(date(2024, 11, 4), date(2024, 11, 9))
        for weekday_date in weekday_list:
            # informs unittests that we are running subtests on the same kind of test (opened_days_count != 1)
            with self.subTest(i=weekday_date):
                self.assertTrue(
                    -1 != self.sensor.get_visit_count(weekday_date),
                    (
                        f"error : should be opened this weekday : {weekday_date} "
                        f"but got {self.sensor.get_visit_count(weekday_date)} visitors",
                    ),
                )

    def test_malfunction_day(self) -> None:
        malfunction_date = date(2022, 2, 17)
        self.assertTrue(
            401 == self.sensor.get_visit_count(malfunction_date),
            (
                f"error : should malfunction_event this days {malfunction_date} "
                f"but got {self.sensor.get_visit_count(malfunction_date)} visitors instead of 401"
            ),
        )

    def test_break_day(self) -> None:
        break_date = date(2022, 2, 4)
        self.assertTrue(
            0 == self.sensor.get_visit_count(break_date),
            (
                f"error : should be broken this day : {break_date}, "
                f"got {self.sensor.get_visit_count(break_date)} visitors instead of 0",
            ),
        )

    def test_mean_count_when_sensor_ok(self) -> None:
        """
        for days without sensor break or malfunction,
        test if mean count is in range:
            [sensor.average_visit - sensor.std_visit,
            sensor.average_visit + sensor.std_visit]
        :return:
        """

        def get_weekday_dates(
            list_date: list[date], day_of_the_week: int
        ) -> list[date]:
            return [
                visit_date
                for visit_date in list_date
                if visit_date.weekday() == day_of_the_week
            ]

        def get_working_sensor_dates(
            detector: Sensor, list_date: list[date]
        ) -> list[date]:
            return [
                visit_date
                for visit_date in list_date
                if not (
                    detector.is_broken(visit_date)
                    or detector.has_malfunction(visit_date)
                )
            ]

        def calculate_mean_count(detector: Sensor, list_date: list[date]) -> float:
            return (
                sum([detector.get_visit_count(date_f) for date_f in list_date])
            ) / len(list_date)

        # start of test_mean_count_on_week_days
        probe = self.sensor

        start_date = date(2022, 1, 1)
        end_date = date(2024, 1, 1)

        date_list = [
            date_visit.date() for date_visit in pd.date_range(start_date, end_date)
        ]
        date_list = get_working_sensor_dates(probe, date_list)

        for week_day in range(6):  # don't test sundays : they're tested already
            with self.subTest(i=week_day):
                dates_weekday = get_weekday_dates(date_list, week_day)

                mean_count = calculate_mean_count(probe, dates_weekday)

                # mean_count should be in [m - std, m + std] if enough weekdays (~ 2 years)
                avg_val = probe.modulate_visit_count_with_week_day(
                    probe.average_visit, week_day=week_day
                )
                std_val = probe.modulate_visit_count_with_week_day(
                    probe.std_visit, week_day=week_day
                )

                min_val = avg_val - std_val
                max_val = avg_val + std_val

                self.assertTrue(
                    min_val <= mean_count <= max_val,
                    f"error : on day {week_day} average_count should be between :"
                    f" {min_val} and {max_val}"
                    f" but got an average of {mean_count}",
                )


if __name__ == "__main__":
    # meaning : do this only if the script is directly run (__name__ = __main__')
    # When it’s imported as a module in another file, __name__ is set to the name of the file/module
    # (without the .py extension).

    # use this to run the tests with the above created class
    unittest.main()
