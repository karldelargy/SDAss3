####################################################################################

#Exam number B083194

####################################################################################
from Act import *
from time import sleep   

def Digit (playerOne, money, attack, act): #selects the cards you chose by index and adds them to your hand
    if( int(act) < len(playerOne['hand'])):
        playerOne['active'].append(playerOne['hand'].pop(int(act)))
        money = money + playerOne['active'][-1].get_money()
        attack = attack + playerOne['active'][-1].get_attack()    
        
    print "\nYour Hand"
    index = 0
    for card in playerOne['hand']:
        print "[%s] %s" % (index, card)
        sleep(0.2)
        index = index + 1

    print "\nYour Active Cards" #shows you the cards you have played into your active line
    for card in playerOne['active']:
        print card
        sleep(0.2)
    print "\nYour Values"
    print "Money %s, Attack %s" % (money, attack) #shows you where you stand in terms of attributes
    sleep(0.2)
    return (playerOne, money, attack)
