class Card:
	cardDictionary = {}
	def __init__(self,name):
		self.name = name
		self.builtFrom_List = []
		self.buildsInto_List = []
		Card.cardDictionary[self.name] = self

	def getName(self):
		return self.name

	def printBuildPathBack(self):
		cardString = ''
		print(f'{self.name} Builds from:', end = ' ')
		for item in self.builtFrom_List:
			cardString += f'{item.getName()}, '
		cardString = cardString[:-2]
		print(cardString)

	def getsBuiltFrom(self,prevCard): # create buildpath Back and forth from card to card
		self.builtFrom_List.append(prevCard)
		prevCard.buildsInto(self)

	def buildsInto(self,nextCard): # Extension of creating buildPath
		self.buildsInto_List.append(nextCard)

	def printBuildPathForward(self):
		cardString = ''
		print(f'{self.name} Builds into:', end = ' ')
		for item in self.buildsInto_List:
			cardString += f'{item.getName()}, '
		cardString = cardString[:-2]
		print(cardString)