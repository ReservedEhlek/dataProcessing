import matplotlib.pyplot as plt
import matplotlib.dates as dates
import psycopg2
# connection to the db
conn = psycopg2.connect(dbname="SelfDrivingCar", user="postgres", password="postgres", host="10.130.50.7")
cur = conn.cursor()
# Selecting the data and then fetching it
cur.execute('SELECT * FROM public.geolocation ORDER BY "time" ASC')
cords = cur.fetchall()
# Transposing 2d list (swapping rows with colomns)
cords = list(zip(*cords))
cur.execute('SELECT * FROM public.conditions ORDER BY "time" ASC')
conds = cur.fetchall()
conds = list(zip(*conds))

# creating a "blank page" for plots
fig = plt.figure(figsize=(20,20))
# function for creating plot
def plot(i, num, timestamps, data):
    """This function is meant for creating a subplots on a blank page

    Args:
        i (int): is the current number of the subplot
        num (int): total number of subplots
        timestamps (list): is the list of timestamps
        data (list): is the main data that is to be displayed on the subplot
    """
    # dont use first subplot as this is timestamps
    if i == 0:
        return
    # pos on the grid
    pos = num*100+10+i
    # make subplot
    ax1 = fig.add_subplot(pos)
    # title of the subplot (im too lazy to hardcode them)
    ax1.set_title("test")
    # create it on the page with "x" as time stamps and "y" as data
    ax1.plot(timestamps, data)

# looping thru the individual conditions
for i in range(len(conds)):
    plot(i, len(conds), cords[2], conds[i])

# window size
plt.subplots_adjust(hspace=1)
# show it on the screen
plt.show()
