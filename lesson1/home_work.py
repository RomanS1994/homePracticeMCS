import cv2 as cv
import urllib
import numpy as np
from google.colab.patches import cv2_imshow as cv_imshow

# Read an image
def read_image_by_url(url):
    req = urllib.request.urlopen(url)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv.imdecode(arr, -1)
    return img

url = 'https://gptchat.in.ua/wp-content/uploads/2023/02/iryna_kunichenko_many_colored_balloons_over_the_grand_canyon_hd_06263781-130a-4137-a4c8-2e7454b401c7.jpg'

img = read_image_by_url(url)
print(img)