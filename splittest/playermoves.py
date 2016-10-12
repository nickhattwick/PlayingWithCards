def plturn():
    p1.playedland = False
    p1.draw()
    p1.mana = len(p1.lands)
    p1.blockers = list(p1.field)
    print("Hand: ", p1.hand)
    print("Field: ", p1.field)
    print("Mana: ", p1.mana)

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

def playland():
    x = 0
    if not p1.playedland:
        while x < len(p1.hand):
            if p1.hand[x] == "l":
                print("x: ", x)
                y = p1.hand.pop(x)
                p1.lands.append(y)
                p1.mana = len(p1.lands)
                print("Mana: ", p1.mana)
                p1.playedland = True
                prompt()
            else:
                x+=1
        print("No lands in hand")
        prompt()
    else:
        print("You've already played a land this turn")
        prompt()

def summon():
    mhand = [x for x in p1.hand if x != "l"]
    print("Monsters: ", mhand)
    mchoice = input("Which monster would you like to summon?\n")
    if str(mchoice) in mhand:
        if int(mchoice) <= p1.mana:
            y = p1.hand.index(mchoice)
            z = p1.hand.pop(y)
            p1.field.append(z)
            p1.blockers.append(z)
            p1.mana = p1.mana - int(mchoice)
            print(p1.field)
            print("Mana Left: ", p1.mana)
            prompt()
        else:
            print("You can only play monsters less than or equal to your mana")
            prompt()
    else:
        print("That's not a card in your hand")
        prompt()

def attack():
    if not p1.blockers:
        print("there's nothing there")
        opturn()
    else:
        print("Your Attackers: ", p1.blockers)
        print("OP's Blockers: ", p2.blockers)
        global atk
        atk = input("Which creature would you like to attack with?\n")
        if str(atk) in p1.blockers:
            y = p1.blockers.index(atk)
            p1.blockers.pop(y)
            block()
            secatkchoice()
        elif atk in p1.field:
            print("You can't attack with that")
            prompt()
        elif not p1.blockers:
            print("There's nothing there")
            prompt()
        else:
            print("That's not even a thing")
            prompt()

def secatkchoice():
    choice = input("Would you like to attack with another monster?\nY or N\n")
    if choice.upper() == "Y":
        attack()
    elif choice.upper() == "N":
        opturn()
    else:
        print("That's not a thing...")
        secatkchoice()

def main():
	print('This should not have happened')

if __name__ == "__main__": main()
