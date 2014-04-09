#!/usr/bin/env python
import json
from os import path
from pprint import pprint
import urllib

bng = "BNG.json"
allTheData = 'allMagicSets42014.json'
mtgImageUrl = 'http://mtgimage.com/card/{0}.jpg'
#extract imagenames

df = open(path.join(path.dirname(__file__),'resources',bng))
data = json.load(df)
cardList=[]
for card in data['cards']:
    #create proper URLs based on this pattern: http://mtgimage.com/card/Craw%20Wurm.jpg
    cardList.append(mtgImageUrl.format(card['imageName']))

df.close()

urllib.urlretrieve(cardList[1],'image.jpg')



