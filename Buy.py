####################################################################################

#Exam number B083194

####################################################################################
def Buy(money, centralLine, playerOne):  #this is the entire buying window

    notending = True
    while money > 0: 
        print "Available Cards"
        ind = 0
        for card in centralLine['active']:  #prints central line and associated indexes
            print "[%s] %s" % (ind,card)
            ind = ind + 1
        print "Choose a card to buy [0-n], S for supplement, E to end buying, Q to quit the game" #presents options
        print "Remaining money %s" % (money)  #remaining money to help with cognit. overload
        bv = raw_input("Choose option: ")
        
        if bv == 'Q':
        	print "Exiting game..."  #exit option
        	exit()
        
        if bv == 'S':  #suppliment option
            if len(centralLine['supplement']) > 0:
                if money >= centralLine['supplement'][0].cost:
                    money = money - centralLine['supplement'][0].cost
                    playerOne['discard'].append(centralLine['supplement'].pop())
                    print "Supplement Bought"
                else:
                    print "insufficient money to buy"
            else:
                print "no supplements left"
        elif bv == 'E':  #exit buying window
            notending = False
            break;
        elif bv.isdigit():   #buying cards by their index
            if int(bv) < len(centralLine['active']):
                 if money >= centralLine['active'][int(bv)].cost:
                    money = money - centralLine['active'][int(bv)].cost #updates money
                    playerOne['discard'].append(centralLine['active'].pop(int(bv)))
                    if( len(centralLine['deck']) > 0):
                        card = centralLine['deck'].pop()
                        centralLine['active'].append(card)
                    else:
                        centralLine['activeSize'] = centralLine['activeSize'] - 1
                    print "Card bought"
                 else:
                    print "insufficient money to buy"
            else:
                 print "enter a valid index number"
        else:
            print "Enter a valid option"
    return (money, centralLine, playerOne)
