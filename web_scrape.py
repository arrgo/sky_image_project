# Scrape webcam hosting websites to extract images 
# Arvind Govinday 06/2021

from bs4 import BeautifulSoup 
import requests 

image_url1 = 'https://images-webcams.windy.com/64/1512053164/current/full/1512053164.jpg'
image_url2 = 'https://images-webcams.windy.com/69/1512053169/current/full/1512053169.jpg'
img_data = requests.get(image_url1).content
with open('london_eye.jpg', 'wb') as handler:
    handler.write(img_data)

img_data = requests.get(image_url2).content
with open('westminister.jpg', 'wb') as handler:
    handler.write(img_data)