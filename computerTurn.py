from time import sleep    #contains the entire turn of the computer
import itertools, random

def computerTurn(money, attack, playerOne, playerComputer, centralLine, aggressive):
    for x in range(0, len(playerComputer['hand'])):  #computer always plays all their cards
                    card = playerComputer['hand'].pop()
                    playerComputer['active'].append(card)
                    money = money + card.get_money()
                    attack = attack + card.get_attack()

    print " Computer player values attack %s, money %s" % (attack, money)  #outputing stats and whats going on
    print " Computer attacking with strength %s" % attack
    playerOne['health'] = playerOne['health'] - attack
    attack = 0
    print "\nPlayer Health %s" % playerOne['health']
    print "Computer Health %s" % playerComputer['health']
    sleep(0.5)
    print " Computer player values attack %s, money %s" % (attack, money)
    print "Computer buying"
    sleep(0.5)
    if money > 0:  #deciding 
        cb = True
        templist = []
        print "Starting Money %s " % (money)
        sleep(0.5)
        while cb:
            templist = []
            if len(centralLine['supplement']) > 0:
                if centralLine['supplement'][0].cost <= money:
                    templist.append(("S", centralLine['supplement'][0])) #buying suppliment card
            for intindex in range (0, centralLine['activeSize']):
                if centralLine['active'][intindex].cost <= money:
                    templist.append((intindex, centralLine['active'][intindex])) # buying cards from central line
            if len(templist) >0:
                highestIndex = 0
                for intindex in range(0,len(templist)):
                    if templist[intindex][1].cost > templist[highestIndex][1].cost:
                        highestIndex = intindex
                    if templist[intindex][1].cost == templist[highestIndex][1].cost:
                        if aggressive:
                            if templist[intindex][1].get_attack() >templist[highestIndex][1].get_attack(): #aggressive choices for buying cards
                                highestIndex = intindex
                        else:
                            if templist[intindex][1].get_attack() >templist[highestIndex][1].get_money(): #acquisitive options for buying cards
                                highestIndex = intindex
                source = templist[highestIndex][0]
                if source in range(0,5):
                    if money >= centralLine['active'][int(source)].cost:
                        money = money - centralLine['active'][int(source)].cost  #updating money after purchases
                        card = centralLine['active'].pop(int(source)) #takes cards from central line
                        print "Card bought %s" % card
                        sleep(0.5)
                        playerComputer['discard'].append(card)
                        
                        if( len(centralLine['deck']) > 0):
                            card = centralLine['deck'].pop()
                            centralLine['active'].append(card)
                        else:
                            centralLine['activeSize'] = centralLine['activeSize'] - 1 #reduces size of central line
                    else:
                        print "Error Occurred"
                        sleep(0.5)
                else:
                    if money >= centralLine['supplement'][0].cost:
                        money = money - centralLine['supplement'][0].cost  #uppdates money
                        card = centralLine['supplement'].pop()
                        playerComputer['discard'].append(card) #moves card to discard pile
                        
                        print "Supplement Bought %s. Remaining money %s" % (card, money) 
                        sleep(0.5)
                    else:
                        print "Error Occurred"
                        sleep(0.5)
            else:
                cb = False
            if money == 0:
                cb = False
    else:
        print "No Money to buy anything"
        sleep(0.5)
        
    if (len(playerComputer['hand']) >0 ):
        for x in range(0, len(playerComputer['hand'])):
            playerComputer['discard'].append(playerComputer['hand'].pop())
    if (len(playerComputer['active']) >0 ):
        for x in range(0, len(playerComputer['active'])):
            playerComputer['discard'].append(playerComputer['active'].pop())
    for x in range(0, playerComputer['handsize']):
                if len(playerComputer['deck']) == 0: #reshuffles deck once empty
                    random.shuffle(playerComputer['discard'])
                    playerComputer['deck'] = playerComputer['discard']
                    playerComputer['discard'] = []
                card = playerComputer['deck'].pop() #gives card to player from shuffled deck into hand
                playerComputer['hand'].append(card)
    print "Computer turn ending"
    sleep(0.5)
    return(money, attack, playerOne, playerComputer, centralLine)
