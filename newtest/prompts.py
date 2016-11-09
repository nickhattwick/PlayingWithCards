from player import Player

def full_turn(player):
    end_conditions = player.life <= 0 or len(player.deck) <= 0
    if end_conditions:
        return False

    can_act = True
    for land in player.lands:
        land.untap()
    player.playedland = False
    player.draw()
    for creature in player.field:
        creature.tapped = False
    while can_act:
        can_act = player.turn_prompt()

    return True
