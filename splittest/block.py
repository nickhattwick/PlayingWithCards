def whoblocks():
    print("Attack Phase")
    x = 0
    while x < len(p2.blockers):
        print("A", p2.blockers[x], "is attacking you.")
        if not p1.blockers:
            p1.life = p1.life - int(p2.blockers[x])
            p2.blockers.pop(x)
            print("LP: ", p1.life)
            if p1.life <= 0:
                print("Game Over")
                exit()
            else:
                x = x + 1
        else:
            choice = input("Will you block? Y or N\n")
            if choice.upper() == "Y":
                print(p1.blockers)
                y = input("Who will you block with?\n")
                if y in p1.blockers:
                    yi = int(y)
                    if y > p2.blockers[x]:
                        a = p1.blockers.index(y)
                        p1.blockers.pop(a)
                        z = p2.field.index(p2.blockers[x])
                        p2.blockers.pop(x)
                        c = p2.field.pop(z)
                        p2.dpile.append(c)
                        print("OP's monster was destroyed")
                    elif p2.blockers[x] > y:
                        a = p1.blockers.index(y)
                        p1.blockers.pop(a)
                        p2.blockers.pop(x)
                        z = p1.field.index(y)
                        c = p1.field.pop(z)
                        p1.dpile.append(c)
                        print("Your ", y, " was destroyed")
                    else:
                        z = p2.field.index(p2.blockers[x])
                        c = p2.field.pop(z)
                        p2.dpile.append(c)
                        h = p1.field.index(y)
                        j = p1.blockers.index(y)
                        p1.blockers.pop(j)
                        g = p1.field.pop(h)
                        p2.blockers.pop(x)
                        p1.dpile.append(g)
                        print("It's a draw, both creatures were destroyed")
                    x = x + 1

                elif y in p1.field:
                    print("You can't block with that")
                    whoblocks()
                else:
                    print("That's not even a thing")
                    whoblocks()
            elif choice.upper() == "N":
                p1.life = p1.life - int(p2.blockers[x])
                print("LP: ", p1.life)
                if p1.life <= 0:
                    print("Game Over")
                    exit()
                else:
                    x = x + 1

            else:
                print("That's not even a thing")
                whoblocks()

def main():
    print('This should not have happened')

if __name__ == "__main__": main()
