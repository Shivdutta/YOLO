# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 19:22:34 2020

@author: shivd
"""
from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO

#search = input("Search For:")
#params = {"q": search}
r = requests.get("https://www.bing.com/images/search?q=steel+coil")

soup= BeautifulSoup(r.text,"html.parser")
links = soup.findAll("a",{"class":"thumb"})

print(links)

for item in links:
    img_obj = requests.get(item.attrs["href"])
    print("Getting", item.attrs["href"])
    title = item.attrs["href"].split("/")[-1]
    img=Image.open(BytesIO(img_obj.content))
    img.save("./scrapped_images/"+title,img.format)