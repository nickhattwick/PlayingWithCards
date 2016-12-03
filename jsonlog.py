import json

def results_log(func):
    def inner(self, *args, **kwargs):
        func(self, *args, **kwargs)
        result = {
        "Game": None
        "W":
        }
        with open("results.json", '') as r:
            
