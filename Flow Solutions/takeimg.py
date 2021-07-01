import requests
import re
import json
from bs4 import BeautifulSoup
import asyncio
from PIL import Image
from io import BytesIO

def getdata(url):
      r = requests.get(url)
      return r.text

def getflow(x,pack):
      htmldata = getdata(f"https://flowfreesolutions.com/flow/solution/?pack={pack}&level={x}")
      soup = BeautifulSoup(htmldata, 'html.parser')
      res = soup.find_all("img", class_="iphone4in-solution")
     
      urll = re.findall(r'"(.*?)"', str(res))
      image_adress = "http://flowfreesolutions.com" + urll[2][5:]
      
      response = requests.get(image_adress)
      img = Image.open(BytesIO(response.content))
      img.save(str(x)+".jpg")
      
      
getflow(1,'regular')
asyncio.sleep(1.5)


