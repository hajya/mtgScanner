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
	
#Takes in a list of cards, the output path, and empty list to be populated with the destination greyscales
#Checks to see if the greyscale exists at taget, if not gets them from the mtgimage
#then calls the convertToGrey function and deletes the color version 
def downloadAndGreyscaleCardImages(listOfCardNames,  cardImagePath, listOfGreyscalePaths):
	if not path.exists(path.join(path.join(path.dirname(__file__),cardImagePath))):
		os.makedirs(path.join(path.join(path.dirname(__file__),cardImagePath)))
		
	cardFileFullPathColor = '{0}\{1}'
	
	for card in listOfCardNames[1:10]:
		
		cardFileFullPathColor = cardFileFullPathColor.format(cardImagePath,card.split("/")[-1])
		cardFileFullPathGrey =  cardFileFullPathColor.replace("jpg","png")
		
		if not (path.isfile(cardFileFullPathGrey)):
			urllib.urlretrieve(card, cardFileFullPathColor.format(cardImagePath,card.split("/")[-1]))
			convertToGrey(cardFileFullPathColor, cardFileFullPathGrey)
			listOfGreyscalePaths.add(cardFileFullPathGrey)
			os.remove(cardFileFullPathColor)
		cardFileFullPathColor = '{0}\{1}'
					
#Takes two file path and converts the colorCard to grey and save as greyCard			
def convertToGrey(colorCard, greyCard):
	img = Image.open(colorCard)
	img = ImageOps.grayscale(img)
	img.save(greyCard)
	
		
if __name__ == "__main__":

	bng = "BNG.json"
	cardImagePath = "cardImages"
	cardList = loadCardFromJson(bng)
	outList = []
	downloadAndGreyscaleCardImages(cardList, cardImagePath, outList)
	
	


