import random
from CardsPlayer import CardsPlayer


NUM_PLAYERS = 3

players = dict()

def playGame():
	global players
	"""
	Make a deck, players, and a pile
	2-10 is 2-10
	11 = J, 12 = Q, 13 = K, 14 = A
	"""
	finishingPlaces = [] # List of players in order of losing

	deck = [i for i in range(2,15)] * 4
	random.shuffle(deck)

	assert len(deck) == 52

	# The players dictionary contains player objects
	players = dict()
	
	# Deal cards
	for i in range(NUM_PLAYERS):
		players[i] = CardsPlayer(deck[i::NUM_PLAYERS], i)

	# The pile is where all cards are placed during the rounds
	pile = []

	# The full pile is where cards are placed after evaulation in the pile
	# Ex. during a war, these are the cards already played
	fullPile = []

	numRounds = 0

	roundWinner = None

	print("Starting the match")
	while len(players) >= 2:
		print(f"\n Round {numRounds}:")
		# Play a turn
		fullPile = []
		pile = [player.drawOne() for player in players.values()]
		print(f"Cards played: {pile}")
		bestCard = max(pile) # This is the best card played
		print(f"Best Card: {bestCard}")
		currentWinners = [player for player in players.values() if player.getLastPlayedCard() == bestCard]
		print(f"currentWinners: {[player.getName() for player in currentWinners]}")
		warLevel = 0
		while(len(currentWinners) > 1): # When a war is still ongoing
			warLevel += 1
			print("War!")
			if warLevel >= 50:
				print("Draw")
				print(f"Winners that tied for first: {[player.getName() for player in currentWinners]}")
				print(f"Other standings: {finishingPlaces[::-1]}")
				break
			fullPile += pile
			pile = []
			for player in players.values():
				if player in currentWinners:
					fullPile += player.drawCards(4)
			
			pile = [player.getLastPlayedCard() for player in players.values() if player in currentWinners] # The last card each player placed
			print(f"War cards played: {pile}")
			bestCard = max(pile) # This is the best card played

			currentWinners = [player for player in players.values() if all([player in currentWinners, player.getLastPlayedCard() == bestCard])]

			pile = []

		fullPile += pile

		roundWinner = currentWinners[0]
		print(f"Play winner: {roundWinner.getName()}")

		print(f"Full pile: {fullPile}")
		if roundWinner.getName() == 1:
			fullPile.sort(reverse=True)
		if roundWinner.getName() == 2:
			random.shuffle(fullPile)
		if roundWinner.getName() == 3:
			fullPile.sort()
		print(f"Adj. Full pile: {fullPile}")

		roundWinner.addToHand(fullPile)

		for player in players.values():
			print(f"Player {player.getName()} has {player.getDeckSize()} cards")

		# Create a list of the deceased
		deletable = []
		
		# Check which players are still in
		for name in players.keys():
			player = players[name]
			if player.isIn() == False:
				print(f"Player {name} has lost")
				finishingPlaces.append(player.getName())
				deletable.append(name)
		
		# Delete losers
		for name in deletable:
			del players[name]

		numRounds += 1

	winner = roundWinner

	finishingPlaces.append(winner.getName())
	print()
	print(f"Standings: {finishingPlaces[::-1]}")
	print(f"Total Rounds: {numRounds}")
	assert winner.getDeckSize() == 52

	return finishingPlaces

if __name__ == "__main__":
	playGame()
	