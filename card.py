from config import blankspace, symbol

class Card:
	cardDictionary = {}

	def __init__(self, name):
		self.name = name
		self.builtFrom_List = []
		self.buildsInto_List = []
		Card.cardDictionary[self.name] = self

	def recGetBuildPath(self, trailingSpaces=''):
		out = ''
		if len(self.builtFrom_List) == 0:  # Base case (If card is not built from anything)
			return '\n' + trailingSpaces + symbol + self.getName()
		for item in self.builtFrom_List:
			out += item.recGetBuildPath(trailingSpaces + blankspace)
		out = '\n' + trailingSpaces + symbol + self.getName() + out
		return out

	def recPrintBuildPath(self):
		print(self.recGetBuildPath())

	def getName(self):
		return self.name

	def getsBuiltFrom(self, prevCard):  # create buildpath Back and forth from card to card
		self.builtFrom_List.append(prevCard)
		prevCard.buildsInto(self)

	def buildsInto(self, nextCard):  # Extension of creating buildPath
		self.buildsInto_List.append(nextCard)
