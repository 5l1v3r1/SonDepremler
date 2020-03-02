# xml çekmek ve okumak için
import os
import requests
import xml.etree.ElementTree as ET

# timer için
import sys
import time
import subprocess

# resim çizdirme
from PIL import Image, ImageDraw, ImageFont

i=0
#while True:
baseUrl = 'http://udim.koeri.boun.edu.tr/zeqmap/xmlt/son24saat.xml'
resp = requests.get(baseUrl)
msg = resp.content

tree = ET.fromstring(msg)
for place in tree.findall('earhquake'):
        
    i += 1

    # resim arkaplan
    img = Image.new('RGB', (500, 500), color = (73, 109, 137))

    # yazı tipi ve boyutu
    fnt = ImageFont.truetype('arial.ttf', 20)

    # çizmeye başla
    d = ImageDraw.Draw(img)

    # yazı
    d.text((20,20), place.get("lokasyon"), font=fnt, fill=(255, 255, 0))
    d.text((20,60), "Saat: " + place.get("name"), font=fnt, fill=(255, 255, 0))
    d.text((20,100), "Büyüklük: " + place.get("mag"), font=fnt, fill=(255, 255, 0))
    d.text((20,140), "Derinlik: " + place.get("Depth"), font=fnt, fill=(255, 255, 0))

    # kaydet
    img.save("Resimler/" + str(i) + "-" + place.get("lokasyon").strip().replace(":", ".") + ".png")

#time.sleep(10)