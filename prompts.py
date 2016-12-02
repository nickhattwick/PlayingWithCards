from testplayer import HumanPlayer, AutoPilot

def full_turn(player):
    end_conditions = player.life <= 0 or len(player.board.deck) <= 0
    if end_conditions:
        return False

    can_act = True
    for land in player.board.lands:
        land.untap()
    player.board.playedland = False
    player.board.draw()
    for creature in player.board.field:
        creature.tapped = False
    while can_act:
        can_act = player.turn_prompt()

    return True
