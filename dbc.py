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


def playAll(money, attack, pO): #this is everything it needs
	if(len(pO['hand'])>0):
		for x in range(0, len(pO['hand'])):
		    card = pO['hand'].pop()
		    pO['active'].append(card)
		    money = money + card.get_money()
		    attack = attack + card.get_attack()

	print "\nYour Hand"
	index = 0
	for card in pO['hand']:
		print "[%s] %s" % (index, card)
		index = index + 1

	print "\nYour Active Cards"
	for card in pO['active']:
		print card
	print "\nYour Values"
	print "Money %s, Attack %s" % (money, attack)

	return (money,attack, pO)  ##this is whats updated

def Buy(money, central, pO):

    notending = True
    while money > 0:
        print "Available Cards"
        ind = 0
        for card in central['active']:
            print "[%s] %s" % (ind,card)
            ind = ind + 1
        print "Choose a card to buy [0-n], S for supplement, E to end buying, Q to quit the game"
        print "Remaining money %s" % (money)
        bv = raw_input("Choose option: ")
        
        if bv == 'Q':
        	print "Exiting game..."
        	exit()
        
        if bv == 'S':
            if len(central['supplement']) > 0:
                if money >= central['supplement'][0].cost:
                    money = money - central['supplement'][0].cost
                    pO['discard'].append(central['supplement'].pop())
                    print "Supplement Bought"
                else:
                    print "insufficient money to buy"
            else:
                print "no supplements left"
        elif bv == 'E':
            notending = False
            break;
        elif bv.isdigit():
            if int(bv) < len(central['active']):
                 if money >= central['active'][int(bv)].cost:
                    money = money - central['active'][int(bv)].cost
                    pO['discard'].append(central['active'].pop(int(bv)))
                    if( len(central['deck']) > 0):
                        card = central['deck'].pop()
                        central['active'].append(card)
                    else:
                        central['activeSize'] = central['activeSize'] - 1
                    print "Card bought"
                 else:
                    print "insufficient money to buy"
            else:
                 print "enter a valid index number"
        else:
            print "Enter a valid option"
    return (money, central, pO)

def Digit (pO, money, attack):
    if( int(act) < len(pO['hand'])):
        pO['active'].append(pO['hand'].pop(int(act)))
        money = money + pO['active'][-1].get_money()
        attack = attack + pO['active'][-1].get_attack()    
        
    print "\nYour Hand"
    index = 0
    for card in pO['hand']:
        print "[%s] %s" % (index, card)
        #sleep(0.5)
        index = index + 1

    print "\nYour Active Cards"
    for card in pO['active']:
        print card
        #sleep(0.5)
    print "\nYour Values"
    print "Money %s, Attack %s" % (money, attack)
    #sleep(0.5)
    return (pO, money, attack)

if __name__ == '__main__':
    pO = {'name': 'player one', 'health': 30, 'deck': None, 'hand': None, 'active': None, 'handsize': 5,
                 'discard': None}
    pC = {'name': 'player computer', 'health': 30, 'deck': None, 'hand': None, 'active': None, 'handsize': 5,
               'discard': None}
    central = {'name': 'central', 'active': None, 'activeSize': 5, 'supplement': None, 'deck': None}
    sdc = [4 * [Card('Archer', (3, 0), 2)], 4 * [Card('Baker', (0, 3), 2)], 3 * [Card('Swordsman', (4, 0), 3)], 2 * [Card('Knight', (6, 0), 5)],3 * [Card('Tailor', (0, 4), 3)],3 * [Card('Crossbowman', (4, 0), 3)],3 * [Card('Merchant', (0, 5), 4)],4 * [Card('Thug', (2, 0), 1)],4 * [Card('Thief', (1, 1), 1)],2 * [Card('Catapault', (7, 0), 6)], 2 * [Card('Caravan', (1, 5), 5)],2 * [Card('Assassin', (5, 0), 4)]]
    playeronedeck = [8 * [Card('Serf', (0, 1), 0)],
                     2 * [Card('Squire', (1, 0), 0)]
                     ]
    pod = list(itertools.chain.from_iterable(playeronedeck))
    pO['deck'] = pod
    pO['hand'] = []
    pO['discard'] = []
    pO['active'] = []
    playertwodeck = [
            8 * [Card('Serf', (0, 1), 0)],
        2 * [Card('Squire', (1, 0), 0)]
    ]
    ptd = list(itertools.chain.from_iterable(playertwodeck))
    pC['deck'] = ptd
    pC['hand'] = []
    pC['discard'] = []
    pC['active'] = []

    supplement = 10 * [Card('Levy', (1, 2), 2)]
    deck = list(itertools.chain.from_iterable(sdc))
    random.shuffle(deck)
    central['deck'] = deck
    central['supplement'] = supplement
    central['active'] = []

    max = central['activeSize']
    count = 0
    while count < max:
        card = central['deck'].pop()
        central['active'].append(card)
        count = count + 1

    for x in range(0, pO['handsize']):
        if (len(pO['deck']) == 0):
            random.shuffle(pO['discard'])
            pO['deck'] = pO['discard']
            pO['discard'] = []
        card = pO['deck'].pop()
        pO['hand'].append(card)

    for x in range(0, pO['handsize']):
        if len(pC['deck']) == 0:
            random.shuffle(pO['discard'])
            pC['deck'] = pC['discard']
            pC['discard'] = []
        card = pC['deck'].pop()
        pC['hand'].append(card)

    print "Available Cards"
    #sleep(0.5)
    for card in central['active']:
        print card
        #sleep(0.5)

    print "Supplement"
    #sleep(0.5)
    if len(central['supplement']) > 0:
        print central['supplement'][0]



    pG = raw_input('Do you want to play a game, yes (Y) or no (N)?:')
    cG = (pG=='Y')
    if (pG is not 'Y'):
		exit()
    oT = raw_input("Do you want an aggressive (A) opponent or an acquisative (Q) opponent?")
    aggressive = (oT=='A')
    acquisative = (oT=='Q')
    if (oT is not 'A' or not 'Q'):
    	exit()
    	
    while cG:
        money = 0
        attack = 0
        while True:

            print "\nPlayer Health %s" % pO['health']
            print "Computer Health %s" % pC['health']
            print "\nYour Hand"
            index = 0
            for card in pO['hand']:
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
            	print "Exiting game..."
            	exit()
            
            if act == 'P':
                money, attack, pO = playAll(money, attack, pO)        #updated    ########   everything it needs
                
            if act.isdigit():
            	pO, money, attack = Digit(pO, money, attack)








            if (act == 'B'):
            	money, central, pO = Buy(money, central, pO)


            if act == 'A':
                pC['health'] = pC['health'] - attack
                attack = 0
            if act == 'E':
                if (len(pO['hand']) >0 ):
                    for x in range(0, len(pO['hand'])):
                        pO['discard'].append(pO['hand'].pop())


                if (len(pO['active']) >0 ):
                    for x in range(0, len(pO['active'])):
                        pO['discard'].append(pO['active'].pop())
                for x in range(0, pO['handsize']):
                    if len(pO['deck']) == 0:
                        random.shuffle(pO['discard'])
                        pO['deck'] = pO['discard']
                        pO['discard'] = []
                    card = pO['deck'].pop()
                    pO['hand'].append(card)
                break

        print "Available Cards"
        for card in central['active']:
            print card

        print "Supplement"
        if len(central['supplement']) > 0:
            print central['supplement'][0]

        print "\nPlayer Health %s" % pO['health']
        print "Computer Health %s" % pC['health']

        money = 0
        attack = 0
        for x in range(0, len(pC['hand'])):
                        card = pC['hand'].pop()
                        pC['active'].append(card)
                        money = money + card.get_money()
                        attack = attack + card.get_attack()

        print " Computer player values attack %s, money %s" % (attack, money)
        print " Computer attacking with strength %s" % attack
        pO['health'] = pO['health'] - attack
        attack = 0
        print "\nPlayer Health %s" % pO['health']
        print "Computer Health %s" % pC['health']
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
                if len(central['supplement']) > 0:
                    if central['supplement'][0].cost <= money:
                        templist.append(("S", central['supplement'][0]))
                for intindex in range (0, central['activeSize']):
                    if central['active'][intindex].cost <= money:
                        templist.append((intindex, central['active'][intindex]))
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
                        if money >= central['active'][int(source)].cost:
                            money = money - central['active'][int(source)].cost
                            card = central['active'].pop(int(source))
                            print "Card bought %s" % card
                            #sleep(0.5)
                            pC['discard'].append(card)
                            
                            if( len(central['deck']) > 0):
                                card = central['deck'].pop()
                                central['active'].append(card)
                            else:
                                central['activeSize'] = central['activeSize'] - 1
                        else:
                            print "Error Occurred"
                            #sleep(0.5)
                    else:
                        if money >= central['supplement'][0].cost:
                            money = money - central['supplement'][0].cost
                            card = central['supplement'].pop()
                            pC['discard'].append(card)
                            
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

        if (len(pC['hand']) >0 ):
            for x in range(0, len(pC['hand'])):
                pC['discard'].append(pC['hand'].pop())
        if (len(pC['active']) >0 ):
            for x in range(0, len(pC['active'])):
                pC['discard'].append(pC['active'].pop())
        for x in range(0, pC['handsize']):
                    if len(pC['deck']) == 0:
                        random.shuffle(pC['discard'])
                        pC['deck'] = pC['discard']
                        pC['discard'] = []
                    card = pC['deck'].pop()
                    pC['hand'].append(card)
        print "Computer turn ending"
        #sleep(0.5)


        print "Available Cards"
        #sleep(0.5)
        for card in central['active']:
            print card

        print "Supplement"
        if len(central['supplement']) > 0:
            print central['supplement'][0]
            #sleep(0.5)

        print "\nPlayer Health %s" % pO['health']
        print "Computer Health %s" % pC['health']
        #sleep(0.5)

        if pO['health'] <= 0:
            cG = False
            print "Computer wins"
            #sleep(0.5)
        elif pC['health'] <= 0:
            cG = False
            print 'Player One  '
        elif central['activeSize'] == 0:
            print "No more cards available"
            #sleep(0.5)
            if pO['health'] > pC['health']:
                print "Player One Wins on Health"
            elif pC['health'] > pO['health']:
                print "Computer Wins"
            else:
            ########################################################################
            	
            	for x in range(0, len(pO['hand'])):
                    card = pO['hand'].pop()
                    pO['active'].append(card)
                    money = money + card.get_money()
                    attack = attack + card.get_attack()
                for x in range(0, len(pO['deck'])):
                    card = pO['deck'].pop()
                    pO['active'].append(card)
                    money = money + card.get_money()
                    attack = attack + card.get_attack()
                for x in range(0, len(pO['discard'])):
                    card = pO['discard'].pop()
                    pO['active'].append(card)
                    money = money + card.get_money()
                    attack = attack + card.get_attack()
                pHT = money + attack
                money=0
                attack=0
                
                for x in range(0, len(pC['hand'])):
                    card = pC['hand'].pop()
                    pC['active'].append(card)
                    money = money + card.get_money()
                    attack = attack + card.get_attack()
                for x in range(0, len(pC['deck'])):
                    card = pC['deck'].pop()
                    pC['active'].append(card)
                    money = money + card.get_money()
                    attack = attack + card.get_attack()
                for x in range(0, len(pO['discard'])):
                    card = pC['discard'].pop()
                    pC['active'].append(card)
                    money = money + card.get_money()
                    attack = attack + card.get_attack()
                pCT = money + attack
                
                if pHT > pCT:
                    print "Player One Wins on Card Strength"
                elif pCT > pHT:
                    print "Computer Wins on Card Strength"
                else:
                    print "Draw"
            cG = False
        if not cG:
            pG = raw_input("\nDo you want to play another game?:")
            cG = (pG=='Y')
            if cG:
                oT = raw_input("Do you want an aggressive (A) opponent or an acquisative (Q) opponent")
                aggressive = (oT=='A')
                pO = {'name': 'player one', 'health': 30, 'deck': None, 'hand': None, 'active': None,
                             'handsize': 5,
                             'discard': None}
                pC = {'name': 'player computer', 'health': 30, 'deck': None, 'hand': None, 'active': None, 'handsize': 5,
                            'discard': None}
                central = {'name': 'central', 'active': None, 'activeSize': 5, 'supplement': None, 'deck': None}
                sdc = [
                                4 * [Card('Archer', (3, 0), 2)],
                                4 * [Card('Baker', (0, 3), 2)],
                                3 * [Card('Swordsman', (4, 0), 3)],
                                2 * [Card('Knight', (6, 0), 5)],
                                3 * [Card('Tailor', (0, 4), 3)],
                                3 * [Card('Crossbowman', (4, 0), 3)],
                                3 * [Card('Merchant', (0, 5), 4)],
                                4 * [Card('Thug', (2, 0), 1)],
                                4 * [Card('Thief', (1, 1), 1)],
                                2 * [Card('Catapault', (7, 0), 6)],
                                2 * [Card('Caravan', (1, 5), 5)],
                                2 * [Card('Assassin', (5, 0), 4)]
                            ]
                playeronedeck = [8 * [Card('Serf', (0, 1), 0)],
                                 2 * [Card('Squire', (1, 0), 0)]
                            ]
                pod = list(itertools.chain.from_iterable(playeronedeck))
                pO['deck'] = pod
                pO['hand'] = []
                pO['discard'] = []
                pO['active'] = []
                playertwodeck = [
                            8 * [Card('Serf', (0, 1), 0)],
                            2 * [Card('Squire', (1, 0), 0)]
                ]
                ptd = list(itertools.chain.from_iterable(playertwodeck))
                pC['deck'] = ptd
                pC['hand'] = []
                pC['discard'] = []
                pC['active'] = []

                supplement = 10 * [Card('Levy', (1, 2), 2)]
                deck = list(itertools.chain.from_iterable(sdc))
                random.shuffle(deck)
                central['deck'] = deck
                central['supplement'] = supplement
                central['active'] = []

                for x in range(0, central['activeSize']):
                    card = central['deck'].pop()
                    central['active'].append(card)

                for x in range(0, pO['handsize']):
                    if len(pO['deck']) == 0:
                        random.shuffle(pO['discard'])
                        pO['deck'] = pO['discard']
                        pO['discard'] = []
                    card = pO['deck'].pop()
                    pO['hand'].append(card)

                for x in range(0, pO['handsize']):
                    if len(pC['deck']) == 0:
                        random.shuffle(pO['discard'])
                        pC['deck'] = pC['discard']
                        pC['discard'] = []
                    card = pC['deck'].pop()
                    pC['hand'].append(card)


                print "Available Cards"
                max = central['activeSize']
                count = 0
                while count < max:
                    print central['active'][count]
                    count = count + 1

                print "Supplement"
                if len(central['supplement']) > 0:
                    print central['supplement'][0]
    exit()
