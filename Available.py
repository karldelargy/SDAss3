####################################################################################

#Exam number B083194

####################################################################################
from time import sleep   #prints central mline and suppliment option
def Available(centralLine):
    print "Available Cards"
    for card in centralLine['active']:
        print card
        sleep(0.1)

    print "Supplement"
    if len(centralLine['supplement']) > 0:
        print centralLine['supplement'][0]
        sleep(0.1)
