def handStrength(playerOne):
    for x in range(0, len(playerOne['hand'])):
        card = playerOne['hand'].pop()
        playerOne['active'].append(card)
        money = money + card.get_money()
        attack = attack + card.get_attack()
    for x in range(0, len(playerOne['deck'])):
        card = playerOne['deck'].pop()
        playerOne['active'].append(card)
        money = money + card.get_money()
        attack = attack + card.get_attack()
    for x in range(0, len(playerOne['discard'])):
        card = playerOne['discard'].pop()
        playerOne['active'].append(card)
        money = money + card.get_money()
        attack = attack + card.get_attack()
    playerHandStrength = money + attack
    return (playerHandStrength)
