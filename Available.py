from time import sleep 
def Available(centralLine):
    print "Available Cards"
    for card in centralLine['active']:
        print card
        sleep(0.1)

    print "Supplement"
    if len(centralLine['supplement']) > 0:
        print centralLine['supplement'][0]
        sleep(0.1)
