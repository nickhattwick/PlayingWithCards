import json

def compiler()
    with open("results.json", 'r') as results:
        print_this = json.loads(results)
        print(print_this)

compiler()
