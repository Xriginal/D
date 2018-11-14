#Oscar Ruiz, Daniel Midguel
#Cst205
#Lab14
#10/30/18
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request as ur
import cv2
import numpy as np
from cv2 import *
# All the modules I imported some may be useless but better safe than sorryself.
# I created a function for url and bottom of it is the code that was provided in ilearn
# I put the image url, convert it to a NumPy array, and then read it into OpenCV format
# then I closed the fucntion using the return statement.
def url_to_image(url):
    resp = ur.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image
urls= ["https://image.pbs.org/curate/2923d346-5d73-45a9-86ba-090f837be502.png"]
#The Url is the pbs one I used for lab13
#im accessing the url inside Urls so the rest can work( the image and the cv2.imshow)
for url in urls:
    image = url_to_image(url)
    cv2.imshow("Image", image)
    cv2.waitKey(0)
#this loops the image
#the wait key keeps the image displaying
