from prompts import prompt
from opblock import block

def attack():
    if not p1.blockers:
        print("there's nothing there")
        prompt()
    else:
        print("Your Attackers: ", p1.blockers)
        print("OP's Blockers: ", p2.blockers)
        global attacker
        attacker = input("Which creature would you like to attack with?\n")
        if str(attacker) in p1.blockers:
            y = p1.blockers.index(attacker)
            block()
            secatkchoice()
        elif attacker in p1.field:
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
        prompt()
    else:
        print("That's not a thing...")
        secatkchoice()
