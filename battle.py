def destroy(player, card):
    player.board.move_card(card, player.board.field, player.board.dpile)
    print(player.name, "s ", card, " was destroyed")

def battle(turnplayer, turncard, defendplayer, defendcard):
    if turncard.power > defendcard.power:
        destroy(defendplayer, defendcard)
    elif turncard.power < defendcard.power:
        destroy(turnplayer, turncard)
    else:
        destroy(defendplayer, defendcard)
        destroy(turnplayer, turncard)
