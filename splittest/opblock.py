def block():
    if not p2.blockers:
        p2.life = p2.life - int(atk)
        print("OP LP: ", p2.life)
        if p2.life <= 0:
            print("You Win!")
            exit()
    elif max(p2.blockers) >= atk:
        blk = [x for x in p2.blockers if x >= atk]
        if min(blk) > atk:
            a = min(blk)
            c = p1.blockers.index(atk)
            d = p1.field.index(atk)
            p1.blockers.pop(c)
            p1.field.pop(d)
            b = p2.blockers.index(a)
            p2.blockers.pop(b)
            p1.dpile.append(atk)
            print("Opponent blocked with ", a, ". Your ", atk, "was destroyed.")
        else:
            blist = sorted(p2.blockers)
            x = 0
            while x < len(blist):
                if blist[x] >= atk:
                    a = blist[x]
                    b = p2.blockers.index(a)
                    p2.blockers.pop(b)
                    c = p1.blockers.index(atk)
                    d = p1.field.index(atk)
                    p1.blockers.pop(c)
                    p1.field.pop(d)
                    p1.dpile.append(atk)
                    print("Opponent blocked with ", a, ". Both were destroyed.")
                    break
                else:
                    x = x + 1
    elif int(atk) > p2.life:
        bmin = min(p2.blockers)
        x = p2.blockers.index(bmin)
        a = p2.field.index(bmin)
        y = p2.field.pop(a)
        p2.blockers.pop(x)
        p2.dpile.append(y)
        print("OP blocked with ", bmin)
        print("OP's ", bmin, " was destroyed")

    else:
        p2.life = p2.life - int(atk)
        print("OP LP: ", p2.life)
        if p2.life <= 0:
            print("You Win!")
            exit()

def main():
	print('This should not have happened')

if __name__ == "__main__": main()
