def prompt():
    choice = input("It's your turn. What will you do? \n LAND SUMMON ATTACK DONE\n")
    if choice.upper() == "LAND":
        playland()
    elif choice.upper() == "SUMMON":
        summon()
    elif choice.upper() == "ATTACK":
        attack()
    elif choice.upper() == "DONE":
        print("Turn End.\n Opponent's Turn")
        p1.blockers = list(p1.field)
        opturn()

    elif choice.upper() == "QUIT":
        exit()

    else:
        print("That's not even a thing")
        prompt()
