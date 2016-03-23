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
from Available import *
from gameDecision import *
from playAgain import *
from playNow import *
from centralMake import *





if __name__ == '__main__':

    playerOne, playerComputer, centralLine=Init()	#initialisations
	

    centrralLine=centralMake(centralLine)  #makes central line

    playerOne=Shuffle(playerOne) #shuffles player 1s cards
    playerComputer=Shuffle(playerComputer)
    Available(centralLine)

    playGame, createGame, aggressive=playNow() #begins the game after initialisations


    	
    while createGame:
        money = 0
        attack = 0
        while True:
            healthUpddate(playerOne,playerComputer)
            
            print "\nYour Hand" #presents options to player
            index = 0
            for card in playerOne['hand']:
                    print "[%s] %s" % (index, card)
                    sleep(0.5)
                    index = index + 1
            print "\nYour Values"
            print "Money %s, Attack %s" % (money, attack)
            sleep(0.5)
            print "\nChoose Action: (P = play all, [0-n] = play that card, B = Buy Card, A = Attack, E = end turn, Q = Quit game)"


            act = Act() #gets input
                
            print act
            
            if act == 'Q':  #different options of the act, they are self documenting
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

        Available(centralLine)


        healthUpddate(playerOne,playerComputer)
        money = 0
        attack = 0
        
        money, attack, playerOne, playerComputer, centralLine=computerTurn(money, attack, playerOne, playerComputer, centralLine,aggressive) # computers turn


        Available(centralLine)

        healthUpddate(playerOne,playerComputer)
        sleep(0.5)

        createGame=gameDecision(playerOne, playerComputer, centralLine,createGame)  #decides if there is a winner yet/the game ends

        if not createGame:
            aggressive,createGame, playGame, centralLine, playerOne, playerComputer=playAgain(createGame, playGame, centralLine) #asks if you want to play again
            
    exit()
