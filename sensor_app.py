from datetime import datetime


class Sensor(object):
    """
    Creates a sensor object which:
        simulates a real visitor counter v in a mall
        returns a simulated visit_counts (at a given date)
    Attributes:
        - average_visit_count
        - standard_deviation_visit_count
    Methods:
        - simulate_visit_count(average_visit_count, std_visit_count) -> int
    """
    def __init__(self, average_visit_count:int, standard_deviation_visit_count:int):
        self.average_visit_count = average_visit_count
        self.standard_deviation_visit_count = standard_deviation_visit_count

    def simulate_visit_count(self,date_visit)->int:
        """
        Generate a number representing the visitor count at a particular date_visit
        Generation of the number :
        - random from
            - a normal distribution centered on:
                - mean: self.average_visit_count
                - standard deviation: self.standard_deviation_visit_count

        :param date_visit:
        :return:
        """
        return 0
#

if __name__ == "__main__": # what's the point of this ?
    avg_visit_count = 2000
    std_visit_count = 100
    date_of_visit = datetime(2024,11,5)
    sensor = Sensor(avg_visit_count, std_visit_count)
    sensor.simulate_visit_count(date_of_visit)