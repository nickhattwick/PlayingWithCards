import json

test = []
with open("nonexistent.json", 'r') as joe:
    data = json.load(joe)

    try:
        for key in data:
            test.append(data[key])
            print("appended")
    except:
        print("there's nothing there, bro")
print(test)
