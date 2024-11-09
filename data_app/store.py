import sys
from datetime import date

from data_app.sensor import Sensor


class Store(object):
    """
    Store attributes:
    - sensors_number sensors (Sensor object) (2)
    - average_visits = sum (visits) for all sensors
    - std_visit = std dev of visits for all the sensors (?)
    Store_methods:
    - get_all_traffic on a given date
    """

    def __init__(
        self,
        store_name: str,
        average_visits: int,
        std_total_visit: int,
        malfunction_rate: float = 0,
        break_rate: float = 0,
        sensors_number=8,
    ):
        self.store_name = store_name
        self.sensors_number = sensors_number  # 8 for instance
        self.average_visits = average_visits
        self.std_visit = std_total_visit
        self.malfunction_rate = malfunction_rate
        self.break_rate = break_rate
        self.sensors = self.create_sensors()

    def create_sensors(self) -> list[Sensor]:
        """
        Creates a list of self.sensors_number with attributes :
        - average_visits shared between all sensors (2 for instance) using :
            - average_visit_ratios list (each sensor has a fraction of the total traffic
        :return: list_of_sensors created
        """
        list_of_sensors = []
        average_visit_ratios = [
            0.2,
            0.2,
            0.2,
            0.2,
            0.05,
            0.05,
            0.05,
            0.05,
        ]  # 4-4 sensors get 80% and 20%
        # print(f"self.sensors_number : {self.sensors_number}")
        for i in range(self.sensors_number):
            average_visit_sensor = int(average_visit_ratios[i] * self.average_visits)
            std_visit_sensor = int(average_visit_ratios[i] * self.std_visit)
            list_of_sensors.append(
                Sensor(
                    average_visit_sensor,
                    std_visit_sensor,
                    self.malfunction_rate,
                    self.break_rate,
                )
            )
        return list_of_sensors

    def get_sensor_traffic(self, sensor_id: int, business_date: date) -> int:
        """Return the traffic for one sensor at a date"""
        return self.sensors[sensor_id].get_visit_count(business_date)

    def get_all_traffic(self, visit_date: date) -> int:
        """Return the total traffic count at a date"""
        return sum([sensor.get_visit_count(visit_date) for sensor in self.sensors])


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

    # create a store_list
    store_names = ["Paris", "Lille", "Marseille", "Lyon", "Grenoble", "Valence"]
    store_sensor_numbers = [8, 8, 8, 8, 8, 8]

    store_averages = [2000, 1500, 1800, 1700, 1000, 800]
    store_stds = [0.1 * store_avg for store_avg in store_averages]

    store_malfunction_chances = [0.035, 0.035, 0.035, 0.035, 0.035, 0.035]
    store_break_chances = [0.015, 0.015, 0.015, 0.015, 0.015, 0.015]

    # [print(name, number, average, std, MALFUNCTION_CHANCE, BREAK_CHANCE)
    #   for name, number,
    #     average, std,
    #     MALFUNCTION_CHANCE, BREAK_CHANCE
    #   in zip(store_names, store_sensor_numbers,
    #       store_averages, store_stds,
    #       store_malfunction_chances, store_break_chances)]

    store_list = [
        Store(name, average, std, malfunction_chance, break_chance, number)
        for name, number, average, std, malfunction_chance, break_chance in zip(
            store_names,
            store_sensor_numbers,
            store_averages,
            store_stds,
            store_malfunction_chances,
            store_break_chances,
        )
    ]

    lille_store = Store("Lille", 1200, 300)
    visits = lille_store.get_sensor_traffic(2, date(2023, 9, 13))

    print(
        f" for sensor 2, visits are {visits} on this peculiar day :{date(2023, 9, 13).weekday()}"
    )

    lille_store = Store("Lille", 1200, 300)
    visits = lille_store.get_all_traffic(date(2023, 9, 13))
    print(
        f"total visits are {visits} on this peculiar day :{date(2023, 9, 13).weekday()}"
    )
