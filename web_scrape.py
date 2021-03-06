# Scrape webcam hosting websites to extract images 
# Arvind Govinday 06/2021

from bs4 import BeautifulSoup #not neccessary? 
import requests 

image_url1 = 'https://images-webcams.windy.com/64/1512053164/current/full/1512053164.jpg' #london eye
image_url2 = 'https://images-webcams.windy.com/69/1512053169/current/full/1512053169.jpg' #westminster hall
image_url3 = 'https://images-webcams.windy.com/54/1490712854/current/full/1490712854.jpg' #shard west
image_url4 = 'https://images-webcams.windy.com/44/1222340244/current/full/1222340244.jpg' #park tower knightsbridge
image_url5 = 'https://images-webcams.windy.com/08/1576526008/current/full/1576526008.jpg' #hilton park lane




img_data = requests.get(image_url1).content
with open('london_eye.jpg', 'wb') as handler:
    handler.write(img_data)

img_data = requests.get(image_url2).content
with open('westminister.jpg', 'wb') as handler:
    handler.write(img_data)

img_data = requests.get(image_url3).content
with open('shard_west.jpg', 'wb') as handler:
    handler.write(img_data)

img_data = requests.get(image_url4).content
with open('knightsbridge.jpg', 'wb') as handler:
    handler.write(img_data)

img_data = requests.get(image_url5).content
with open('hilton_pl.jpg', 'wb') as handler:
    handler.write(img_data)

