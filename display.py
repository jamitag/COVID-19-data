import requests

class Recipes():
    def __init__(self, res):
        self.values = res["results"] 
        self.options = {}

    def selectRecipe(self): # loops through results and prints each value
        for i, value in enumerate(self.values):
            print(str(i+1) + ". " + value["title"])
            self.options[i+1] = value["title"]