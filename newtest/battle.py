def destroy(player, card):
    cardindex = player.field.index(card)
    movingcard = player.field.pop(cardindex)
    player.dpile.append(movingcard)
    print(player, "s ", card, " was destroyed")

def battle(turnplayer, turncard, defendplayer, defendcard):
    if turncard.power > defendcard.power:
        destroy(defendplayer, defendcard)
    elif x < y:
        destroy(turnplayer, turncard)
    else:
        destroy(defendplayer, defendcard)
        destroy(turnplayer, turncard)
