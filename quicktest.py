test = []
with open("parsed.json", 'r') as joe:
    try:
        for key in joe:
            test.append(joe[key])
            print("appended")
    except:
        print("there's nothing there, bro")
print(test)
