from player import Player

def turn_prompt(player):
    print("It's", player.name, "s turn.")
    choice = input("It's your turn. What will you do? \n LAND TAP SUMMON ATTACK DONE\n")

    if choice.upper() == "LAND":
        player.play_land()

    elif choice.upper() == "VIEW":
        player.hand_view()

    elif choice.upper() == "SUMMON":
        choice = input("Which monster will you summon?")
        player.summon(choice)

    elif choice.upper() == "TAP":
        for land in player.lands:
            if not land.tapped:
                player.tap_for_mana(land)
            print(player.mana.amount)


    elif choice.upper() == "ATTACK":
        attacker = input("Which monster will attack?")
        player.attack(attacker)

    elif choice.upper() == "DONE":
        return False

    elif choice.upper() == "QUIT":
        exit()

    else:
        print("That's not even a thing")
        turn_prompt(player)

    return True

def full_turn(player):
    end_conditions = player.life <= 0 or len(player.deck) <= 0
    if end_conditions:
        return False

    can_act = True
    player.playedland = False
    player.draw()
    for creature in player.field:
        creature.tapped = False
    while can_act:
        can_act = turn_prompt(player)

    return True
