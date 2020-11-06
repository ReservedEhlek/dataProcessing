import psycopg2
from PIL import Image, ImageDraw
# connection to the db
conn = psycopg2.connect(dbname="SelfDrivingCar", user="postgres", password="postgres", host="10.130.50.7")
cur = conn.cursor()
# fetch data
cur.execute('SELECT * FROM public."eyeTracking" ORDER BY "time" ASC')
data = cur.fetchall()

def createImage(xy):
    """This function creates an image that later will be used as a frame

    Args:
        xy (list): cord of the eye

    Returns:
        PIL.Image.Image: an image with the eyesocket and xy eye in it
    """
    # create black img
    img = Image.new("L", (40, 40))
    dr = ImageDraw.Draw(img)
    # draw an eye socket
    dr.ellipse((0, 5, 39, 34), outline=(255))
    # draw point (eye)
    dr.point(xy, fill=(255))
    return img


imgArray = []
# loop thru xy cord (frame) of the eye and call the func 
for frame in data:
    imgArray.append((createImage(frame[1:3])))
# create an GIF out of it
imgArray[0].save("out.gif", format="GIF",append_images=imgArray[1:], save_all=True, duration=30,loop=0)
