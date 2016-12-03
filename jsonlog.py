import json

def results_log(func):
    def inner(self, *args, **kwargs):
        func(self, *args, **kwargs)
        game = {"W": winner.name, "L": loser.name}
        with open("results.json", 'a') as results:
            json.dump(game, results)

def moves_log(func):
    def inner(self, *args, **kwargs):
        
