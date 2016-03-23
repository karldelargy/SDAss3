####################################################################################

#Exam number B083194

####################################################################################
import itertools, random

def endTurn (playerOne):
    if (len(playerOne['hand']) >0 ):
        for x in range(0, len(playerOne['hand'])):
            playerOne['discard'].append(playerOne['hand'].pop()) #adds cards to discards pile from hand


    if (len(playerOne['active']) >0 ): #adds cards to discards pile from active area
        for x in range(0, len(playerOne['active'])):
            playerOne['discard'].append(playerOne['active'].pop()) 
    for x in range(0, playerOne['handsize']):
        if len(playerOne['deck']) == 0:  #if deck is empty, shuffle discard pile and use as new deck
            random.shuffle(playerOne['discard'])
            playerOne['deck'] = playerOne['discard']
            playerOne['discard'] = []
        card = playerOne['deck'].pop()
        playerOne['hand'].append(card)
    
    return (playerOne)
