from Shuffle import *
from Available import *
from Init import *
from playNow import *

def playAgain(createGame, playGame, centralLine):
    playGame, createGame, aggressive =playNow()
        
        
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

    return(aggressive,createGame, playGame, centralLine, playerOne, playerComputer)
