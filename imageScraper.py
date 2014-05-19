#!/usr/bin/env python
import json
import os
import urllib
from PIL import ImageOps, Image

from os import path



allTheData = 'allMagicSets42014.json'


#extract imagenames
def loadCardFromJson(jsonDB):
	mtgImageUrl = 'http://mtgimage.com/card/{0}.jpg'
	
	df = open(path.join(path.dirname(__file__),'resources',bng))
	data = json.load(df)
	cardList=[]
	for card in data['cards']:
		#create proper URLs based on this pattern: http://mtgimage.com/card/Craw%20Wurm.jpg
		cardList.append(mtgImageUrl.format(card['imageName']).replace(" ","_"))
	return cardList
	df.close()
	
def downloadAndGreyscaleCardImages(listOfCardNames,  cardImagePath):
	if not path.exists(path.join(path.join(path.dirname(__file__),cardImagePath))):
		os.makedirs(path.join(path.join(path.dirname(__file__),cardImagePath)))
		
	cardFileFullPathColor = '{0}\{1}'
	
	for card in listOfCardNames[1:5]:
		print card
		cardFileFullPathColor = cardFileFullPathColor.format(cardImagePath,card.split("/")[-1])
		cardFileFullPathGrey =  cardFileFullPathColor.replace("jpg","png")
		
		print(cardFileFullPathColor)
		print(cardFileFullPathGrey)
		if not (path.isfile(cardFileFullPathGrey)):
			urllib.urlretrieve(card, cardFileFullPathColor.format(cardImagePath,card.split("/")[-1]))
			convertToGrey(cardFileFullPathColor, cardFileFullPathGrey)
		os.remove(cardFileFullPathColor)
		cardFileFullPathColor = '{0}\{1}'
		
			
			
def convertToGrey(colorCard, greyCard):
	img = Image.open(colorCard)
	img = ImageOps.grayscale(img)
	img.save(greyCard)
	return
		

		
		
if __name__ == "__main__":

	bng = "BNG.json"
	cardImagePath = "cardImages"
	cardList = loadCardFromJson(bng)
	downloadAndGreyscaleCardImages(cardList, cardImagePath)
	
	


