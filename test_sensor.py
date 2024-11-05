from datetime import date

import pandas as pd
from sensor_app import Sensor

# from unittest import

if __name__ == "__main__":
    # meaning : do this only if the script is directly run (__name__ = __main__')
    # When it’s imported as a module in another file, __name__ is set to the name of the file/module
    # (without the .py extension).
    avg_visit_count = 2000
    std_visit_count = 100

    malfunction_chance = 0.035
    break_chance = 0.015

    start_date = date(2022, 1, 1)
    end_date = date(2023,12 , 31)

    # do a date_range using pandas ! and convert it to a list
    for visit_date in pd.date_range(start = start_date, end= end_date).tolist():
        sensor = Sensor(avg_visit_count, std_visit_count, malfunction_chance, break_chance)
        result = sensor.simulate_visit_count(visit_date)





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

