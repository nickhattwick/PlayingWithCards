def destroy(player, card):
    player.move_card(card, player.field, player.dpile)
    print(player.name, "s ", card, " was destroyed")

def battle(turnplayer, turncard, defendplayer, defendcard):
    if turncard.power > defendcard.power:
        destroy(defendplayer, defendcard)
    elif turncard.power < defendcard.power:
        destroy(turnplayer, turncard)
    else:
        destroy(defendplayer, defendcard)
        destroy(turnplayer, turncard)
