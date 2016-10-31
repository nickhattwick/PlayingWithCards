def destroy(player, card):
    player.move_card(card, player.hand, player.dpile)    
    print(player, "s ", card, " was destroyed")

def battle(turnplayer, turncard, defendplayer, defendcard):
    if turncard.power > defendcard.power:
        destroy(defendplayer, defendcard)
    elif x < y:
        destroy(turnplayer, turncard)
    else:
        destroy(defendplayer, defendcard)
        destroy(turnplayer, turncard)
