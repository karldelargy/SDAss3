import itertools, random
from time import sleep              #sleep(0.5) = half second  #from ,file> import *
from playAll import *
from Quit import *
from Buy import *
from Attack import *
from handStrength import *
from Shuffle import *
from Init import *
from Card import * 
from Act import *
from Digit import *
from endTurn import *
from healthUpdate import *
from computerTurn import *


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
    sleep(0.5)
    for card in centralLine['active']:
        print card
        sleep(0.5)

    print "Supplement"
    sleep(0.5)
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
            healthUpddate(playerOne,playerComputer)
            
            print "\nYour Hand"
            index = 0
            for card in playerOne['hand']:
                    print "[%s] %s" % (index, card)
                    sleep(0.5)
                    index = index + 1
            print "\nYour Values"
            print "Money %s, Attack %s" % (money, attack)
            sleep(0.5)
            print "\nChoose Action: (P = play all, [0-n] = play that card, B = Buy Card, A = Attack, E = end turn, Q = Quit game)"


            act = Act()
                
            print act
            
            if act == 'Q':
				Quit()
            
            if act == 'P':
                money, attack, playerOne = playAll(money, attack, playerOne)        #updated    ########   everything it needs
                
            if act.isdigit():
            	playerOne, money, attack = Digit(playerOne, money, attack, act)

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

        healthUpddate(playerOne,playerComputer)
        money = 0
        attack = 0
        
        money, attack, playerOne, playerComputer, centralLine=computerTurn(money, attack, playerOne, playerComputer, centralLine,aggressive)

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
        sleep(0.5)

        print "Available Cards"
        sleep(0.5)
        for card in centralLine['active']:
            print card

        print "Supplement"
        if len(centralLine['supplement']) > 0:
            print centralLine['supplement'][0]
            sleep(0.5)

        print "\nPlayer Health %s" % playerOne['health']
        print "Computer Health %s" % playerComputer['health']
        sleep(0.5)

        if playerOne['health'] <= 0:
            createGame = False
            print "Computer wins"
            sleep(0.5)
        elif playerComputer['health'] <= 0:
            createGame = False
            print 'Player One  wins'
        elif centralLine['activeSize'] == 0:
            print "No more cards available"
            sleep(0.5)
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
