import random

class CardsPlayer:

	def __init__(self, cards, name):
		self.cards = cards
		self.lastPlayedCard = 0
		self.name = name

	def drawOne(self):
		# Draw one card from the top of the stack
		if len(self.cards) > 0:
			retVal = self.lastPlayedCard = self.cards.pop(0)
			return retVal
		else:
			self.lastPlayedCard = 0
			raise Exception(f"No cards to draw from {self.name}")

	def drawCards(self, num_cards):
		# return multiple cards
		# if impossible to play a card, 
		returnHand = self.cards[:num_cards]
		self.cards = self.cards[num_cards:]
		if len(returnHand) > 0:
			self.lastPlayedCard = returnHand[-1]

		return returnHand

	def getDeckSize(self):
		# get the size of the player's deck
		return len(self.cards)

	def getLastPlayedCard(self):
		# In the case of a long war, get the last played card
		return self.lastPlayedCard

	def getName(self):
		# Get the player's name
		return self.name

	def addToHand(self, cardList):
		# Add to the end of hand in the specified order
		self.cards += cardList

	def isIn(self):
		# Return if the player has cards
		return bool(len(self.cards))