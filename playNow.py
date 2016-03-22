

def playNow():

    playGame = raw_input('Do you want to play a game, yes (Y) or no (N)?:')
    createGame = (playGame=='Y')
    if (playGame is not 'Y'):
		exit()
		print "See you next time"
    opponentType = raw_input("Do you want an aggressive (A) opponent or an acquisitive (Q) opponent?")
    aggressive = (opponentType=='A')


    return(playGame, createGame, aggressive )
