####################################################################################

#Exam number B083194

####################################################################################
from time import sleep    #works out the effects of attack in terms of change of health
def Attack (playerComputer, attack):
    playerComputer['health'] = playerComputer['health'] - attack
    attack = 0
    
    return (playerComputer, attack)
