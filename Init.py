####################################################################################

#Exam number B083194

####################################################################################
from Card import *   #initilises the game deck, hands, cards, attributes etc
import itertools, random
from time import sleep   

def Init():
    playerOne = {'name': 'player one', 'health': 30, 'deck': None, 'hand': None, 'active': None, 'handsize': 5,
                 'discard': None} #defining stats for players
    playerComputer = {'name': 'player computer', 'health': 30, 'deck': None, 'hand': None, 'active': None, 'handsize': 5,
               'discard': None}
    centralLine = {'name': 'centralLine', 'active': None, 'activeSize': 5, 'supplement': None, 'deck': None}
    sdc = [4 * [Card('Archer', (3, 0), 2)], 4 * [Card('Baker', (0, 3), 2)], 3 * [Card('Swordsman', (4, 0), 3)], 2 * [Card('Knight', (6, 0), 5)],3 * [Card('Tailor', (0, 4), 3)],3 * [Card('Crossbowman', (4, 0), 3)],3 * [Card('Merchant', (0, 5), 4)],4 * [Card('Thug', (2, 0), 1)],4 * [Card('Thief', (1, 1), 1)],2 * [Card('Catapault', (7, 0), 6)], 2 * [Card('Caravan', (1, 5), 5)],2 * [Card('Assassin', (5, 0), 4)]]
    playeronedeck = [8 * [Card('Serf', (0, 1), 0)],
                     2 * [Card('Squire', (1, 0), 0)]
                     ]
    pod = list(itertools.chain.from_iterable(playeronedeck))
    playerOne['deck'] = pod
    playerOne['hand'] = []
    playerOne['discard'] = []
    playerOne['active'] = []
    playertwodeck = [
            8 * [Card('Serf', (0, 1), 0)], #staring hand for both
        2 * [Card('Squire', (1, 0), 0)]
    ]
    ptd = list(itertools.chain.from_iterable(playertwodeck))
    playerComputer['deck'] = ptd
    playerComputer['hand'] = []
    playerComputer['discard'] = []
    playerComputer['active'] = []

    supplement = 10 * [Card('Levy', (1, 2), 2)] #defines suppliment cards
    deck = list(itertools.chain.from_iterable(sdc))
    random.shuffle(deck)
    centralLine['deck'] = deck
    centralLine['supplement'] = supplement
    centralLine['active'] = []
    return(playerOne, playerComputer, centralLine)
