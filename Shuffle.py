####################################################################################

#Exam number B083194

####################################################################################
def Shuffle(playerOne):  #shuffles cards in discard into deck
    for x in range(0, playerOne['handsize']):
        if len(playerOne['deck']) == 0:
            random.shuffle(playerOne['discard'])
            playerOne['deck'] = playerOne['discard']
            playerOne['discard'] = []
        card = playerOne['deck'].pop()
        playerOne['hand'].append(card)
    return (playerOne)


