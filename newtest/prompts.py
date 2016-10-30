from player import Player

def turn_prompt(player):
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
        turn_prompt(player.opponent)

    elif choice.upper() == "QUIT":
        exit()

    else:
        print("That's not even a thing")
        prompt()
