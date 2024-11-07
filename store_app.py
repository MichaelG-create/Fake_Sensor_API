import sys
from datetime import date

from sensor_app import Sensor


class Store(object):
    """
    Store attributes:
    - sensors_number sensors (Sensor object) (2)
    - average_total_visits = sum (visits) for all sensors
    - std_total_visit = std dev of visits for all the sensors (?)
    Store_methods:
    - simulate_store_visit_count on a given date
    """

    def __init__(
        self,
        store_name: str,
        sensors_number: int,
        average_total_visits: int,
        std_total_visit: int,
        malfunction_rate: float,
        break_rate: float,
    ):
        self.store_name = store_name
        self.sensors_number = sensors_number  # 2 for instance

        self.average_total_visits = average_total_visits
        self.std_total_visit = std_total_visit

        self.malfunction_rate = malfunction_rate
        self.break_rate = break_rate

        self.sensors_list = self.create_sensors()

    def create_sensors(self) -> list[Sensor]:
        """
        Creates a list of self.sensors_number with attributes :
        - average_total_visits shared between all sensors (2 for instance) using :
            - average_visit_ratios list (each sensor has a fraction of the total traffic
        :return: list_of_sensors created
        """
        list_of_sensors = []
        average_visit_ratios = [
            0.8,
            0.2,
        ]  # 2 sensors get respectively 80% and 20% of the traffic
        print(f"self.sensors_number : {self.sensors_number}")
        for i in range(self.sensors_number):
            average_visit_sensor = int(
                average_visit_ratios[i] * self.average_total_visits
            )
            std_visit_sensor = int(average_visit_ratios[i] * self.std_total_visit)
            list_of_sensors.append(
                Sensor(
                    average_visit_sensor,
                    std_visit_sensor,
                    self.malfunction_rate,
                    self.break_rate,
                )
            )
        return list_of_sensors

    def simulate_store_visit_count(self, visit_date: date) -> int:
        """
        generate the traffic count :
         - at date
         - on each sensor
         and sum it
        :param visit_date:
        :return: sum of all sensor's traffic at date for the store (store_count
        """
        # remark : when a sensor breaks or malfunction it variates the store_count
        return int(
            sum(
                [
                    sensor.simulate_visit_count(visit_date)
                    for sensor in self.sensors_list
                ]
            )
        )


if __name__ == "__main__":
    avg_visit_count = 2000
    std_visit_count = 100

    malfunction_chance = 0.035
    break_chance = 0.015

    if len(sys.argv) > 1:
        date_tok = sys.argv[1].split("-")
        date_of_visit = date(int(date_tok[0]), int(date_tok[1]), int(date_tok[2]))
    else:
        date_of_visit = date(2024, 11, 5)

    # create a store
    # store = Store('Lille', 2, AVG_VISIT_COUNT, STD_VISIT_COUNT, MALFUNCTION_CHANCE, BREAK_CHANCE)
    # result = store.simulate_store_visit_count(date_of_visit)

    # create a store_list
    store_names = ["Paris", "Lille", "Marseille", "Lyon", "Grenoble", "Valence"]
    store_sensor_numbers = [2, 2, 2, 2, 2, 2]

    store_averages = [2000, 1500, 1800, 1700, 1000, 800]
    store_stds = [0.2 * store_avg for store_avg in store_averages]

    store_malfunction_chances = [0.035, 0.035, 0.035, 0.035, 0.035, 0.035]
    store_break_chances = [0.015, 0.015, 0.015, 0.015, 0.015, 0.015]

    # print(store_names, store_sensor_numbers,
    #     store_averages, store_stds,
    #     store_malfunction_chances, store_break_chances)

    # [print(name, number, average, std, MALFUNCTION_CHANCE, BREAK_CHANCE)
    #   for name, number,
    #     average, std,
    #     MALFUNCTION_CHANCE, BREAK_CHANCE
    #   in zip(store_names, store_sensor_numbers,
    #       store_averages, store_stds,
    #       store_malfunction_chances, store_break_chances)]

    store_list = [
        Store(name, number, average, std, malfunction_chance, break_chance)
        for name, number, average, std, malfunction_chance, break_chance in zip(
            store_names,
            store_sensor_numbers,
            store_averages,
            store_stds,
            store_malfunction_chances,
            store_break_chances,
        )
    ]
