from sensor_app import Sensor

class Store(object):
    """
    Store attributes:
    - number_sensors sensors (Sensor object) (2)
    - average_total_visits = sum (visits) for all sensors
    - std_total_visit = std dev of visits for all the sensors (?)
    Store_methods:
    - get_total_visit_count on a given date
    """
    def __init__(self,number_sensors:int,average_total_visits:int, std_total_visit:int,
                 malfunction_rate: float, break_rate: float):
        self.number_sensors = number_sensors # 2 for instance
        self.average_total_visits = average_total_visits
        self.std_total_visit = std_total_visit
        self.malfunction_rate = malfunction_rate
        self.break_rate = break_rate
        self.sensors = self.create_sensors()

    def create_sensors(self):
        list_of_sensors = []
        average_visit_ratios = [0.8, 0.2] # 2 sensors get respectively 80% and 20% of the traffic
        for i in range(self.number_sensors):
            average_visit_sensor = int(average_visit_ratios[i] * self.average_total_visits)
            std_visit_sensor = int(average_visit_ratios[i] * self.std_total_visit)
            list_of_sensors.append(
                Sensor(
                    average_visit_sensor,
                    std_visit_sensor,
                    self.malfunction_rate ,
                    self.break_rate)
            )


