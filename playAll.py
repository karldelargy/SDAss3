####################################################################################

#Exam number B083194

####################################################################################
from time import sleep   
def playAll(money, attack, playerOne): #this is everything it needs #plays all the cards in your hand
	if(len(playerOne['hand'])>0):
		for x in range(0, len(playerOne['hand'])):
		    card = playerOne['hand'].pop()
		    playerOne['active'].append(card)
		    money = money + card.get_money() #sums attributes for cards in hand
		    attack = attack + card.get_attack()

	print "\nYour Hand"  #tells you whats on the board and in your hand
	index = 0
	for card in playerOne['hand']:
		print "[%s] %s" % (index, card)
		index = index + 1
        sleep(0.5)
	print "\nYour Active Cards"
	for card in playerOne['active']:
		print card
		sleep(0.5)
	print "\nYour Values"
	print "Money %s, Attack %s" % (money, attack)

	return (money,attack, playerOne)  ##this is whats updated
