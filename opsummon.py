def opsummon():
    print("in summon phase test")
    mhand = [x for x in p2.hand if x != "l"]
    p2.mana = len(p2.lands)
    rhand = sorted(mhand, reverse=True)
    x = 0
    while x < len(rhand) and p2.mana > 0:
        if int(rhand[x]) <= p2.mana:
            a = rhand[x]
            b = p2.hand.index(a)
            c = p2.hand.pop(b)
            rhand.pop(x)
            print("OP summons ", a)
            p2.field.append(c)
            p2.mana = p2.mana - int(a)
        else:
            x = x + 1

    print("OP's field: ", p2.field)
    p2.blockers = list(p2.field)
    if not p2.blockers:
        print("End of OP's turn")
    else:
        whoblocks()
    plturn()
