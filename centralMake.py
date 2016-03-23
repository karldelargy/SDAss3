####################################################################################

#Exam number B083194

####################################################################################
def centralMake(centralLine):  #creates the central line
    max = centralLine['activeSize']
    count = 0
    while count < max:
        card = centralLine['deck'].pop()
        centralLine['active'].append(card)
        count = count + 1
    return(centralLine)
