import requests

class Recipes():
    def __init__(self, res):
        self.values = res["results"] 
        self.options = {}

    def selectRecipe(self): # loops through results and prints each value
        for i, value in enumerate(self.values):
            print(str(i+1) + ". " + value["title"])
            self.options[i+1] = value["title"]
        
        choice = input("Select a recipe - ")
        title = self.options[int(choice)] # storing the name of the recipe that user selects

        for value in self.values: # searching each of the ten recipes for the selected title to see if match
            if value["title"] == title:
                return value["id"] #returning recipes id number from api

    def selectIngredients(self, id, url, key):
        apiInformation = url + str(id) + "/information?apiKey="+key # returning the information tag from recipe database
        res = requests.get(apiInformation).json()

        print(res)
