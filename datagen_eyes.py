from datetime import datetime, timedelta
import time
import psycopg2
# conn to db
conn = psycopg2.connect(dbname="SelfDrivingCar", user="postgres", password="postgres", host="10.130.50.7")
cur = conn.cursor()

# make eye movemtns
x = list(range(20, 35)) + list(range(35, 25, -1))
y = list(range(20, 25)) + list(range(25, 0, -1))

# make them eq len
x = x[0:len(y)]
y = y[0:len(x)]
# add timestamp and timedelta, to emulate passing time
timestamp = datetime.now()
delta = timedelta(0, .10)
# save it all to db
for cord in range(len(x)):
    print(x[cord], y[cord])
    cur.execute(f"""
INSERT INTO public."eyeTracking" (
"eye1X", "eye1Y", "eye2X", "eye2Y", "soc1X", "soc1Y", "soc2X", "soc2Y", "time") VALUES (
'{x[cord]}'::integer, '{y[cord]}'::integer, '{x[cord]}'::integer, '{y[cord]}'::integer, '20'::integer, '20'::integer, '20'::integer, '20'::integer, '{timestamp}'::timestamp with time zone)
returning "time";
""")
    timestamp += delta

conn.commit()