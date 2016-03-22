import itertools, random
from time import sleep              ##sleep(0.5) = half second

class Card(object):
    def __init__(self, name, values=(0, 0), cost=1):
        self.name = name
        self.cost = cost
        self.values = values
    def __str__(self):
                return 'Name %s costing %s with attack %s and money %s' % (self.name, self.cost, self.values[0], self.values[1])
    def get_attack(self):
        return self.values[0]
    def get_money(self):
            return self.values[1]


def playAll(money, attack, playerOne): #this is everything it needs
	if(len(playerOne['hand'])>0):
		for x in range(0, len(playerOne['hand'])):
		    card = playerOne['hand'].pop()
		    playerOne['active'].append(card)
		    money = money + card.get_money()
		    attack = attack + card.get_attack()

	print "\nYour Hand"
	index = 0
	for card in playerOne['hand']:
		print "[%s] %s" % (index, card)
		index = index + 1

	print "\nYour Active Cards"
	for card in playerOne['active']:
		print card
	print "\nYour Values"
	print "Money %s, Attack %s" % (money, attack)

	return (money,attack, playerOne)  ##this is whats updated

def Buy(money, centralLine, playerOne):

    notending = True
    while money > 0:
        print "Available Cards"
        ind = 0
        for card in centralLine['active']:
            print "[%s] %s" % (ind,card)
            ind = ind + 1
        print "Choose a card to buy [0-n], S for supplement, E to end buying, Q to quit the game"
        print "Remaining money %s" % (money)
        bv = raw_input("Choose option: ")
        
        if bv == 'Q':
        	print "Exiting game..."
        	exit()
        
        if bv == 'S':
            if len(centralLine['supplement']) > 0:
                if money >= centralLine['supplement'][0].cost:
                    money = money - centralLine['supplement'][0].cost
                    playerOne['discard'].append(centralLine['supplement'].pop())
                    print "Supplement Bought"
                else:
                    print "insufficient money to buy"
            else:
                print "no supplements left"
        elif bv == 'E':
            notending = False
            break;
        elif bv.isdigit():
            if int(bv) < len(centralLine['active']):
                 if money >= centralLine['active'][int(bv)].cost:
                    money = money - centralLine['active'][int(bv)].cost
                    playerOne['discard'].append(centralLine['active'].pop(int(bv)))
                    if( len(centralLine['deck']) > 0):
                        card = centralLine['deck'].pop()
                        centralLine['active'].append(card)
                    else:
                        centralLine['activeSize'] = centralLine['activeSize'] - 1
                    print "Card bought"
                 else:
                    print "insufficient money to buy"
            else:
                 print "enter a valid index number"
        else:
            print "Enter a valid option"
    return (money, centralLine, playerOne)

def Digit (playerOne, money, attack):
    if( int(act) < len(playerOne['hand'])):
        playerOne['active'].append(playerOne['hand'].pop(int(act)))
        money = money + playerOne['active'][-1].get_money()
        attack = attack + playerOne['active'][-1].get_attack()    
        
    print "\nYour Hand"
    index = 0
    for card in playerOne['hand']:
        print "[%s] %s" % (index, card)
        #sleep(0.5)
        index = index + 1

    print "\nYour Active Cards"
    for card in playerOne['active']:
        print card
        #sleep(0.5)
    print "\nYour Values"
    print "Money %s, Attack %s" % (money, attack)
    #sleep(0.5)
    return (playerOne, money, attack)

def endTurn (playerOne):
    if (len(playerOne['hand']) >0 ):
        for x in range(0, len(playerOne['hand'])):
            playerOne['discard'].append(playerOne['hand'].pop())


    if (len(playerOne['active']) >0 ):
        for x in range(0, len(playerOne['active'])):
            playerOne['discard'].append(playerOne['active'].pop())
    for x in range(0, playerOne['handsize']):
        if len(playerOne['deck']) == 0:
            random.shuffle(playerOne['discard'])
            playerOne['deck'] = playerOne['discard']
            playerOne['discard'] = []
        card = playerOne['deck'].pop()
        playerOne['hand'].append(card)
    
    return (playerOne)

def Attack (playerComputer, attack):
    playerComputer['health'] = playerComputer['health'] - attack
    attack = 0
    
    return (playerComputer, attack)

def Quit():
	print "Exiting game..."
	exit()
	
def Init():
    playerOne = {'name': 'player one', 'health': 30, 'deck': None, 'hand': None, 'active': None, 'handsize': 5,
                 'discard': None}
    playerComputer = {'name': 'player computer', 'health': 30, 'deck': None, 'hand': None, 'active': None, 'handsize': 5,
               'discard': None}
    centralLine = {'name': 'centralLine', 'active': None, 'activeSize': 5, 'supplement': None, 'deck': None}
    sdc = [4 * [Card('Archer', (3, 0), 2)], 4 * [Card('Baker', (0, 3), 2)], 3 * [Card('Swordsman', (4, 0), 3)], 2 * [Card('Knight', (6, 0), 5)],3 * [Card('Tailor', (0, 4), 3)],3 * [Card('Crossbowman', (4, 0), 3)],3 * [Card('Merchant', (0, 5), 4)],4 * [Card('Thug', (2, 0), 1)],4 * [Card('Thief', (1, 1), 1)],2 * [Card('Catapault', (7, 0), 6)], 2 * [Card('Caravan', (1, 5), 5)],2 * [Card('Assassin', (5, 0), 4)]]
    playeronedeck = [8 * [Card('Serf', (0, 1), 0)],
                     2 * [Card('Squire', (1, 0), 0)]
                     ]
    pod = list(itertools.chain.from_iterable(playeronedeck))
    playerOne['deck'] = pod
    playerOne['hand'] = []
    playerOne['discard'] = []
    playerOne['active'] = []
    playertwodeck = [
            8 * [Card('Serf', (0, 1), 0)],
        2 * [Card('Squire', (1, 0), 0)]
    ]
    ptd = list(itertools.chain.from_iterable(playertwodeck))
    playerComputer['deck'] = ptd
    playerComputer['hand'] = []
    playerComputer['discard'] = []
    playerComputer['active'] = []

    supplement = 10 * [Card('Levy', (1, 2), 2)]
    deck = list(itertools.chain.from_iterable(sdc))
    random.shuffle(deck)
    centralLine['deck'] = deck
    centralLine['supplement'] = supplement
    centralLine['active'] = []
    return(playerOne, playerComputer, centralLine)

def handStrength(playerOne):
    for x in range(0, len(playerOne['hand'])):
        card = playerOne['hand'].pop()
        playerOne['active'].append(card)
        money = money + card.get_money()
        attack = attack + card.get_attack()
    for x in range(0, len(playerOne['deck'])):
        card = playerOne['deck'].pop()
        playerOne['active'].append(card)
        money = money + card.get_money()
        attack = attack + card.get_attack()
    for x in range(0, len(playerOne['discard'])):
        card = playerOne['discard'].pop()
        playerOne['active'].append(card)
        money = money + card.get_money()
        attack = attack + card.get_attack()
    playerHandStrength = money + attack
    return (playerHandStrength)

def Shuffle(playerOne):
    for x in range(0, playerOne['handsize']):
        if len(playerOne['deck']) == 0:
            random.shuffle(playerOne['discard'])
            playerOne['deck'] = playerOne['discard']
            playerOne['discard'] = []
        card = playerOne['deck'].pop()
        playerOne['hand'].append(card)
    return (playerOne)

def healthUpddate():
    print "\nPlayer Health %s" % playerOne['health']
    print "Computer Health %s" % playerComputer['health']
    return()
    
    
    
def computerTurn(money, attack, playerOne, playerComputer, centralLine):
    for x in range(0, len(playerComputer['hand'])):
                    card = playerComputer['hand'].pop()
                    playerComputer['active'].append(card)
                    money = money + card.get_money()
                    attack = attack + card.get_attack()

    print " Computer player values attack %s, money %s" % (attack, money)
    print " Computer attacking with strength %s" % attack
    playerOne['health'] = playerOne['health'] - attack
    attack = 0
    print "\nPlayer Health %s" % playerOne['health']
    print "Computer Health %s" % playerComputer['health']
    #sleep(0.5)
    print " Computer player values attack %s, money %s" % (attack, money)
    print "Computer buying"
    #sleep(0.5)
    if money > 0:
        cb = True
        templist = []
        print "Starting Money %s " % (money)
        #sleep(0.5)
        while cb:
            templist = []
            if len(centralLine['supplement']) > 0:
                if centralLine['supplement'][0].cost <= money:
                    templist.append(("S", centralLine['supplement'][0]))
            for intindex in range (0, centralLine['activeSize']):
                if centralLine['active'][intindex].cost <= money:
                    templist.append((intindex, centralLine['active'][intindex]))
            if len(templist) >0:
                highestIndex = 0
                for intindex in range(0,len(templist)):
                    if templist[intindex][1].cost > templist[highestIndex][1].cost:
                        highestIndex = intindex
                    if templist[intindex][1].cost == templist[highestIndex][1].cost:
                        if aggressive:
                            if templist[intindex][1].get_attack() >templist[highestIndex][1].get_attack():
                                highestIndex = intindex
                        else:
                            if templist[intindex][1].get_attack() >templist[highestIndex][1].get_money():
                                highestIndex = intindex
                source = templist[highestIndex][0]
                if source in range(0,5):
                    if money >= centralLine['active'][int(source)].cost:
                        money = money - centralLine['active'][int(source)].cost
                        card = centralLine['active'].pop(int(source))
                        print "Card bought %s" % card
                        #sleep(0.5)
                        playerComputer['discard'].append(card)
                        
                        if( len(centralLine['deck']) > 0):
                            card = centralLine['deck'].pop()
                            centralLine['active'].append(card)
                        else:
                            centralLine['activeSize'] = centralLine['activeSize'] - 1
                    else:
                        print "Error Occurred"
                        #sleep(0.5)
                else:
                    if money >= centralLine['supplement'][0].cost:
                        money = money - centralLine['supplement'][0].cost
                        card = centralLine['supplement'].pop()
                        playerComputer['discard'].append(card)
                        
                        print "Supplement Bought %s. Remaining money %s" % (card, money)
                        #sleep(0.5)
                    else:
                        print "Error Occurred"
                        #sleep(0.5)
            else:
                cb = False
            if money == 0:
                cb = False
    else:
        print "No Money to buy anything"
        #sleep(0.5)
    return(money, attack, playerOne, playerComputer, centralLine)


if __name__ == '__main__':

    playerOne, playerComputer, centralLine=Init()	
	
    max = centralLine['activeSize']
    count = 0
    while count < max:
        card = centralLine['deck'].pop()
        centralLine['active'].append(card)
        count = count + 1

    playerOne=Shuffle(playerOne)
    playerComputer=Shuffle(playerComputer)

    print "Available Cards"
    #sleep(0.5)
    for card in centralLine['active']:
        print card
        #sleep(0.5)

    print "Supplement"
    #sleep(0.5)
    if len(centralLine['supplement']) > 0:
        print centralLine['supplement'][0]



    playGame = raw_input('Do you want to play a game, yes (Y) or no (N)?:')
    createGame = (playGame=='Y')
    if (playGame is not 'Y'):
		exit()
    opponentType = raw_input("Do you want an aggressive (A) opponent or an acquisitive (Q) opponent?")
    aggressive = (opponentType=='A')
    acquisitive = (opponentType=='Q')
    if (opponentType is not 'A' or not 'Q'):
    	exit()
    	
    while createGame:
        money = 0
        attack = 0
        while True:
            healthUpddate()
            
            print "\nYour Hand"
            index = 0
            for card in playerOne['hand']:
                    print "[%s] %s" % (index, card)
                    #sleep(0.5)
                    index = index + 1
            print "\nYour Values"
            print "Money %s, Attack %s" % (money, attack)
            #sleep(0.5)
            print "\nChoose Action: (P = play all, [0-n] = play that card, B = Buy Card, A = Attack, E = end turn, Q = Quit game)"

            act = raw_input("Enter Action: ")
            print act
            
            if act == 'Q':
				Quit()
            
            if act == 'P':
                money, attack, playerOne = playAll(money, attack, playerOne)        #updated    ########   everything it needs
                
            if act.isdigit():
            	playerOne, money, attack = Digit(playerOne, money, attack)

            if (act == 'B'):
            	money, centralLine, playerOne = Buy(money, centralLine, playerOne)

            if act == 'A':
				playerComputer, attack=Attack(playerComputer, attack)

            if act == 'E':
            	playerOne=endTurn(playerOne)
            	break


        print "Available Cards"
        for card in centralLine['active']:
            print card

        print "Supplement"
        if len(centralLine['supplement']) > 0:
            print centralLine['supplement'][0]

        healthUpddate()
        money = 0
        attack = 0
        
        money, attack, playerOne, playerComputer, centralLine=computerTurn(money, attack, playerOne, playerComputer, centralLine)

        if (len(playerComputer['hand']) >0 ):
            for x in range(0, len(playerComputer['hand'])):
                playerComputer['discard'].append(playerComputer['hand'].pop())
        if (len(playerComputer['active']) >0 ):
            for x in range(0, len(playerComputer['active'])):
                playerComputer['discard'].append(playerComputer['active'].pop())
        for x in range(0, playerComputer['handsize']):
                    if len(playerComputer['deck']) == 0:
                        random.shuffle(playerComputer['discard'])
                        playerComputer['deck'] = playerComputer['discard']
                        playerComputer['discard'] = []
                    card = playerComputer['deck'].pop()
                    playerComputer['hand'].append(card)
        print "Computer turn ending"
        #sleep(0.5)

        print "Available Cards"
        #sleep(0.5)
        for card in centralLine['active']:
            print card

        print "Supplement"
        if len(centralLine['supplement']) > 0:
            print centralLine['supplement'][0]
            #sleep(0.5)

        print "\nPlayer Health %s" % playerOne['health']
        print "Computer Health %s" % playerComputer['health']
        #sleep(0.5)

        if playerOne['health'] <= 0:
            createGame = False
            print "Computer wins"
            #sleep(0.5)
        elif playerComputer['health'] <= 0:
            createGame = False
            print 'Player One  '
        elif centralLine['activeSize'] == 0:
            print "No more cards available"
            #sleep(0.5)
            if playerOne['health'] > playerComputer['health']:
                print "Player One Wins on Health"
            elif playerComputer['health'] > playerOne['health']:
                print "Computer Wins"
            else:
            ########################################################################
            	
                playerHandStrength=handStrength(playerOne)
                computerHandStrength=handStrength(playerComputer)
                
                
                if playerHandStrength > computerHandStrength:
                    print "Player One Wins on Card Strength"
                elif computerHandStrength > playerHandStrength:
                    print "Computer Wins on Card Strength"
                else:
                    print "Draw"
            createGame = False
        if not createGame:
        
        
            playGame = raw_input("\nDo you want to play another game?:")
            createGame = (playGame=='Y')
            if createGame:
                opponentType = raw_input("Do you want an aggressive (A) opponent or an acquisitive (Q) opponent")
                aggressive = (opponentType=='A')
                
                
                playerOne, playerComputer, centralLine=Init()

                for x in range(0, centralLine['activeSize']):
                    card = centralLine['deck'].pop()
                    centralLine['active'].append(card)

                playerOne=Shuffle(playerOne)
                playerComputer=Shuffle(playerComputer)


                print "Available Cards"
                max = centralLine['activeSize']
                count = 0
                while count < max:
                    print centralLine['active'][count]
                    count = count + 1

                print "Supplement"
                if len(centralLine['supplement']) > 0:
                    print centralLine['supplement'][0]
    exit()
