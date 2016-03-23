from handStrength import *
from time import sleep  

def gameDecision(playerOne, playerComputer, centralLine, createGame):
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
       	
            playerHandStrength=handStrength(playerOne)
            computerHandStrength=handStrength(playerComputer)
            
            
            if playerHandStrength > computerHandStrength:
                print "Player One Wins on Card Strength"
            elif computerHandStrength > playerHandStrength:
                print "Computer Wins on Card Strength"
            else:
                print "Draw"
        createGame = False
    return (createGame)
