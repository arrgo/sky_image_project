# Scrape webcam hosting websites to extract images 
# Arvind Govinday 06/2021

from bs4 import BeautifulSoup 
import requests 

image_url1 = 'https://images-webcams.windy.com/64/1512053164/current/full/1512053164.jpg' #london eye
image_url2 = 'https://images-webcams.windy.com/69/1512053169/current/full/1512053169.jpg' #westminster hall
image_url3 = 'https://api.deckchair.com/v1/viewer/image/60bdd58beea25f000183056b' #shard west

img_data = requests.get(image_url1).content
with open('london_eye.jpg', 'wb') as handler:
    handler.write(img_data)

img_data = requests.get(image_url2).content
with open('westminister.jpg', 'wb') as handler:
    handler.write(img_data)

img_data = requests.get(image_url3).content
with open('shard_west.jpg', 'wb') as handler:
    handler.write(img_data)