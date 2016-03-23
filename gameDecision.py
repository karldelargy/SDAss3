####################################################################################

#Exam number B083194

####################################################################################
from handStrength import * #decides if the game is over or who won
from time import sleep  

def gameDecision(playerOne, playerComputer, centralLine, createGame):
    if playerOne['health'] <= 0: #player falls below zero, they lose
        createGame = False
        print "Computer wins"
        sleep(0.5)
    elif playerComputer['health'] <= 0: #computer falls below zero you win
        createGame = False
        print 'Player One  wins'
    elif centralLine['activeSize'] == 0: #when health is above zero but there are no more cards, it comes down to who has more health
        print "No more cards available"
        sleep(0.5)
        if playerOne['health'] > playerComputer['health']: #whoever has more health wins
            print "Player One Wins on Health"
        elif playerComputer['health'] > playerOne['health']:
            print "Computer Wins"
        else:
       	
            playerHandStrength=handStrength(playerOne) #if there is still no difference it comes down to card strength
            computerHandStrength=handStrength(playerComputer)
            
            
            if playerHandStrength > computerHandStrength:
                print "Player One Wins on Card Strength"
            elif computerHandStrength > playerHandStrength: #more attributes attack and money mean you win
                print "Computer Wins on Card Strength"
            else:
                print "Draw"
        createGame = False
    return (createGame)
