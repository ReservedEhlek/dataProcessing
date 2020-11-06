from datetime import datetime, timedelta
import psycopg2
import gpxpy
import gpxpy.gpx
# conn to db
conn = psycopg2.connect(dbname="SelfDrivingCar", user="postgres", password="postgres", host="10.130.50.7")
cur = conn.cursor()

# add timestamp and timedelta, to emulate passing time
timestamp = datetime.strptime("2020-11-05 19:09:16.137210", "%Y-%m-%d %H:%M:%S.%f")
delta = timedelta(0, 2.2)
# open gpx (route) file
gpx_file = open('route.gpx', 'r')
# parse it to get gps cord
gpx = gpxpy.parse(gpx_file)
# loop thru seperate crod and save it to db
for track in gpx.tracks:
    for segment in track.segments:
        print(len(segment.points))
        for point in segment.points:
            print('Point at ({0},{1})'.format(point.latitude, point.longitude))
            cur.execute(f"""
            INSERT INTO public.geolocation (
            "X", "Y", "time") VALUES (
            '{point.latitude}'::numeric, '{point.longitude}'::numeric, '{timestamp}'::timestamp with time zone)
            returning "time";
            """)
            timestamp += delta

conn.commit()
