"""
Module containing Sensor Class
"""

from datetime import date

# date : useful when full days are used
# datetime : useful when moment of the day are needed
import sys

import numpy as np


class Sensor(object):
    """
    Creates a sensor object which:
        simulates a real visitor counter v in a mall
        returns a simulated visit_counts (at a given date)
    Attributes:
        - average_visit
        - std_visit
        - malfunction_rate : probability  of malfunction_event of a sensor
        - break_rate  : probability  of break_event of a sensor
    Methods:
        - simulate_visit_count(average_visit, STD_VISIT_COUNT) -> int
    """

    def __init__(
        self,
        average_visit_count: int,
        standard_deviation_visit_count: int,
        malfunction_rate: float,
        break_rate: float,
    ):
        self.average_visit = average_visit_count
        self.std_visit = standard_deviation_visit_count

        self.malfunction_rate = malfunction_rate
        self.break_rate = break_rate

    def break_event(self, event: float, visit_count: int) -> int:
        """
        if break event : visit_count = 0
        :param event: random number in [0,1] to check if sensor breaks
        :param visit_count:
        :return: modified visit_count, break_or_malfunction_flag string to log the event type
        """
        if event <= self.break_rate:
            visit_count = 0

        return visit_count

    def malfunction_event(self, event: float, visit_count: int) -> int:
        """
        if malfunction_event : diminish visit_count by 80% !
        :param event: random number in [0,1] to check if sensor malfunction
        :param visit_count:
        :return: modified visit_count, break_or_malfunction_flag string to log the event type
        """
        if event <= self.malfunction_rate:
            visit_count = int(visit_count * 0.2)

        return visit_count

    def is_broken(self, visit_day: date) -> bool:
        """
        test if this day, the sensor brakes
        :param visit_day:
        :return: broken or not
        """
        # ensure reproducibility for the same day
        self.initiate_seed(visit_day)
        # run random to progress along the random sequence initiated by the seed
        # so that rand_event is the same as in simulate_visit_count
        np.random.normal()

        # malfunction_event or break_event
        rand_event = np.random.random()
        if rand_event <= self.break_rate:
            return True
        else:
            return False

    def has_malfunction(self, visit_day: date) -> bool:
        """
        test if this day, the sensor has malfunction
        :param visit_day:
        :return: malfunction or not
        """
        # ensure reproducibility for the same day
        self.initiate_seed(visit_day)
        # run random to progress along the random sequence initiated by the seed
        # so that rand_event is the same as in simulate_visit_count
        np.random.normal()

        # malfunction_event
        rand_event = np.random.random()
        if rand_event <= self.malfunction_rate:
            return True
        else:
            return False

    @staticmethod
    def modulate_with_week_day(
        visit_count: int, visit_date=date(1, 1, 1), week_day=-1
    ) -> int:
        """
        Modulate random visit_count to take into account weekday traffic increase
        Monday 0    -> keep it
        Tuesday 1   -> keep it
        Wednesday 2 -> + 10 %
        Thursday 3  -> keep it
        Friday 4    -> + 10 %
        Saturday 5  -> + 35 %
        Sunday 6    -> closed   -> -1
        :param visit_count:
        :param visit_date: date of visit
        :param week_day: or day of the week (int in [0:7])
        :return:
        """
        if visit_date != date(1, 1, 1):
            week_day = visit_date.weekday()
        elif week_day == -1:
            print("Error no date or week_day given !")
            return 0

        if week_day == 6:
            visit_count = -1  # closed on sunday
        else:
            day_moduler = [1, 1, 1.1, 1, 1.1, 1.35]
            visit_count *= day_moduler[week_day]

        return int(visit_count)

    @staticmethod
    def initiate_seed(visit_day: date):
        # ensure reproducibility of rands for the same day
        np.random.seed(visit_day.toordinal())

    def simulate_visit_count(self, visit_date: date) -> int:
        """
        Generate a number representing the visitor count at a particular visit_date
        Generation of the number :
        - random from
            - a normal distribution centered with:
                - mean: self.average_visit
                - standard deviation: self.std_visit
        - modulation with week_day traffic modulation
        - -1 if sunday
        - 0 if sensor breaks
        - 80% traffic reduction if sensor malfunction
        :param visit_date:
        :return: visit_count
        """
        # ensure reproducibility for the same day
        self.initiate_seed(visit_date)

        # generate random visit count with random.normalvariate
        visit_count = int(np.random.normal(self.average_visit, self.std_visit))

        # add week_day impact on visit_count
        visit_count = self.modulate_with_week_day(visit_count, visit_date)

        # malfunction_event or break_event
        rand_event = np.random.random()
        visit_count = self.malfunction_event(rand_event, visit_count)
        visit_count = self.break_event(rand_event, visit_count)

        # print(f"Visits count was :{visit_count} this day : {visit_date} " + flag)
        return visit_count


if __name__ == "__main__":
    # meaning : do this only if the script is directly run (__name__ = __main__')
    # When it’s imported as a module in another file, __name__ is set to the name of the file/module
    # (without the .py extension).
    AVG_VISIT_COUNT: int = 2000
    STD_VISIT_COUNT: int = 100

    MALFUNCTION_CHANCE: float = 0.035
    BREAK_CHANCE: float = 0.015

    if len(sys.argv) > 1:
        date_tok = sys.argv[1].split("-")
        date_of_visit = date(int(date_tok[0]), int(date_tok[1]), int(date_tok[2]))
    else:
        date_of_visit = date(2024, 11, 5)
    sensor = Sensor(AVG_VISIT_COUNT, STD_VISIT_COUNT, MALFUNCTION_CHANCE, BREAK_CHANCE)
    result = sensor.simulate_visit_count(date_of_visit)
