from Act import *
from time import sleep   

def Digit (playerOne, money, attack, act):
    if( int(act) < len(playerOne['hand'])):
        playerOne['active'].append(playerOne['hand'].pop(int(act)))
        money = money + playerOne['active'][-1].get_money()
        attack = attack + playerOne['active'][-1].get_attack()    
        
    print "\nYour Hand"
    index = 0
    for card in playerOne['hand']:
        print "[%s] %s" % (index, card)
        sleep(0.5)
        index = index + 1

    print "\nYour Active Cards"
    for card in playerOne['active']:
        print card
        sleep(0.5)
    print "\nYour Values"
    print "Money %s, Attack %s" % (money, attack)
    sleep(0.1)
    return (playerOne, money, attack)
