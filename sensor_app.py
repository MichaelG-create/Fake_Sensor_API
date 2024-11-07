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
        - malfunction_rate : probability  of malfunction of a sensor
        - break_rate  : probability  of breaking of a sensor
    Methods:
        - simulate_visit_count(average_visit, std_visit_count) -> int
    """
    def __init__(self,
                 average_visit_count:int, standard_deviation_visit_count:int,
                 malfunction_rate: float, break_rate: float
                 ):
        self.average_visit = average_visit_count
        self.std_visit = standard_deviation_visit_count

        self.malfunction_rate = malfunction_rate
        self.break_rate = break_rate

    def malfunction_or_break(self, visit_count:int)-> (int, str):
        """
        if malfunction : diminish visit_count by 80% !
        if break event : visit_count = 0
        :param visit_count:
        :return: modified visit_count, break_or_malfunction_flag string to log the event type
        """
        event = np.random.random()

        if event <= self.break_rate:
            break_or_malfunction_flag = "break"
            visit_count =  0
        elif event <= self.malfunction_rate:
            break_or_malfunction_flag = "malfunction"
            visit_count =  int(visit_count * 0.2)
        else:
            break_or_malfunction_flag = ''

        return visit_count, break_or_malfunction_flag

    @staticmethod
    def modulate_with_week_day(visit_count:int, visit_date:date)->int:
        """
        Modulate random visit_count to take into account weekday traffic increase
        Monday 0    -> keep it
        Tuesday 1   -> keep it
        Wednesday 2 -> + 10 %
        Thursday 3  -> keep it
        Friday 4    -> + 25 %
        Saturday 5  -> + 35 %
        Sunday 6    -> closed   -> -1
        :param visit_count:
        :param visit_date:
        :return:
        """
        week_day = visit_date.weekday()
        if week_day == 2: visit_count *= 1.1
        elif week_day == 4: visit_count *= 1.1
        elif week_day == 5: visit_count *= 1.1
        elif week_day == 6: visit_count = -1

        return int(visit_count)

    def simulate_visit_count(self,visit_date:date)->int:
        """
        Generate a number representing the visitor count at a particular visit_date
        Generation of the number :
        - random from
            - a normal distribution centered on:
                - mean: self.average_visit
                - standard deviation: self.std_visit

        :param visit_date:
        :return:
        """
        # ensure reproducibility for the same day
        np.random.seed(visit_date.toordinal())

        # generate random visit count with random.normalvariate
        visit_count = int(np.random.normal(
            self.average_visit,
            self.std_visit
        ))

        # add week_day impact on visit_count
        visit_count = self.modulate_with_week_day(visit_count, visit_date)

        # malfunction or break event
        visit_count, flag = self.malfunction_or_break(visit_count)


        print(f"Visits count was :{visit_count} this day : {visit_date} "+flag)
        return visit_count

if __name__ == "__main__":
    # meaning : do this only if the script is directly run (__name__ = __main__')
    # When it’s imported as a module in another file, __name__ is set to the name of the file/module
    # (without the .py extension).
    avg_visit_count = 2000
    std_visit_count = 100

    malfunction_chance = 0.035
    break_chance = 0.015

    if len(sys.argv) > 1:
        date_tok = sys.argv[1].split('-')
        date_of_visit = date(int(date_tok[0]), int(date_tok[1]), int(date_tok[2]))
    else :
        date_of_visit = date(2024,11,5)
    sensor = Sensor(avg_visit_count, std_visit_count, malfunction_chance, break_chance)
    result = sensor.simulate_visit_count(date_of_visit)

