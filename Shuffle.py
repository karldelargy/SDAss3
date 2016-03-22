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
