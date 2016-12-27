import json

def compiler():
    with open("results.json", 'r') as results:
        datas = json.load(results)
        numnums = datas["number"]
        print(numnums)

compiler()
