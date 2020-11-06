from datetime import datetime, timedelta
import psycopg2
# conn to db

conn = psycopg2.connect(dbname="SelfDrivingCar", user="postgres", password="postgres", host="10.130.50.7")
cur = conn.cursor()

# add timestamp and timedelta, to emulate passing time
timestamp = datetime.strptime("2020-11-05 19:09:16.137210", "%Y-%m-%d %H:%M:%S.%f")
delta = timedelta(0, 2.2)
# emulate cond and save them
for i in range(119):
    cur.execute(f"""
    INSERT INTO public.conditions (
    "time", light, temp, humidity, visibility) VALUES (
    '{timestamp}'::timestamp with time zone, '20'::numeric, '15'::integer, '{20+i/100}'::numeric, '30'::integer)
    returning "time";
    """)
    timestamp += delta
conn.commit()
