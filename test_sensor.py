from datetime import date

import pandas as pd
from sensor_app import Sensor

# from unittest import

def test_closed_on_sunday(sensor:Sensor)->None:
    sunday_date = date( 2024 ,11 ,3 )
    assert -1 == sensor.simulate_visit_count(sunday_date), \
    f"error : opened this sunday : {sunday_date} with {sensor.simulate_visit_count(sunday_date)} visitors"

# needs to be tested over a set of weekday date (monday, tuesday, wednesday, thursday, friday, saturday
def test_opened_on_worked_days(sensor:Sensor, weekday_list:list[date]):
    for weekday_date in weekday_list:
        assert -1 != sensor.simulate_visit_count(weekday_date), \
        f"error : should be opened this weekday : {weekday_date} but got {sensor.simulate_visit_count(weekday_date)} visitors"

def test_malfunction_day(sensor:Sensor)->None:
    malfunction_date = date(2022, 2 , 17)
    assert 401 == sensor.simulate_visit_count(malfunction_date), \
    (f"error : should malfunction this days {malfunction_date} "
     f"but got {sensor.simulate_visit_count(malfunction_date)} visitors instead of 401")

def test_break_day(sensor:Sensor)->None:
    break_date = date(2022, 2, 4 )
    assert 0 == sensor.simulate_visit_count(break_date), \
    f"error : should be broken this day : {break_date}, got {sensor.simulate_visit_count(break_date)} visitors instead of 0"

if __name__ == "__main__":
    # meaning : do this only if the script is directly run (__name__ = __main__')
    # When it’s imported as a module in another file, __name__ is set to the name of the file/module
    # (without the .py extension).
    avg_visit_count = 2000
    std_visit_count = 100

    malfunction_chance = 0.035
    break_chance = 0.015


    detector = Sensor(avg_visit_count, std_visit_count, malfunction_chance, break_chance)

    #start tests by hand
    test_closed_on_sunday(detector)

    start_date = date(2023, 12, 25)
    end_date = date(2023,12 , 30)
    weekday_lst = pd.date_range(start = start_date, end= end_date).tolist()

    test_opened_on_worked_days(detector, weekday_lst)

    test_malfunction_day(detector)

    test_break_day(detector)


    # # do a date_range using pandas ! and convert it to a list
    # for visit_date in pd.date_range(start = start_date, end= end_date).tolist():
    #     sensor = Sensor(avg_visit_count, std_visit_count, malfunction_chance, break_chance)
    #     result = sensor.simulate_visit_count(visit_date)






# logs :
# Visits count was :401 this day : 2022-02-17 00:00:00 malfunction
# Visits count was :449 this day : 2022-07-13 00:00:00 malfunction
# Visits count was :460 this day : 2022-07-16 00:00:00 malfunction
# Visits count was :390 this day : 2022-07-21 00:00:00 malfunction
# Visits count was :426 this day : 2022-07-27 00:00:00 malfunction
# Visits count was :409 this day : 2022-08-02 00:00:00 malfunction
# Visits count was :473 this day : 2022-08-10 00:00:00 malfunction
# Visits count was :411 this day : 2022-10-05 00:00:00 malfunction
# Visits count was :414 this day : 2023-02-09 00:00:00 malfunction
# Visits count was :372 this day : 2023-02-28 00:00:00 malfunction
# Visits count was :457 this day : 2023-04-28 00:00:00 malfunction
# Visits count was :414 this day : 2023-07-10 00:00:00 malfunction
# Visits count was :455 this day : 2023-07-29 00:00:00 malfunction
# Visits count was :441 this day : 2023-11-16 00:00:00 malfunction
# Visits count was :0 this day : 2022-02-04 00:00:00 break
# Visits count was :-1 this day : 2022-02-06 00:00:00 break
# Visits count was :0 this day : 2022-02-11 00:00:00 break
# Visits count was :0 this day : 2022-02-19 00:00:00 break
# Visits count was :0 this day : 2022-03-03 00:00:00 break
# Visits count was :0 this day : 2022-05-03 00:00:00 break
# Visits count was :0 this day : 2022-08-13 00:00:00 break
# Visits count was :0 this day : 2022-08-22 00:00:00 break
# Visits count was :0 this day : 2022-12-16 00:00:00 break
# Visits count was :0 this day : 2022-12-22 00:00:00 break
# Visits count was :0 this day : 2023-01-25 00:00:00 break
# Visits count was :0 this day : 2023-03-31 00:00:00 break
# Visits count was :0 this day : 2023-04-11 00:00:00 break
# Visits count was :0 this day : 2023-05-01 00:00:00 break
# Visits count was :0 this day : 2023-05-23 00:00:00 break
# Visits count was :0 this day : 2023-06-17 00:00:00 break
# Visits count was :0 this day : 2023-07-03 00:00:00 break
# Visits count was :0 this day : 2023-09-13 00:00:00 break
# Visits count was :0 this day : 2023-10-04 00:00:00 break

