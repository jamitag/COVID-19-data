import requests

class Recipes():
"""Unlocking the list of recipes to enable indexing and user selection and returning user friendly data from the API
"""
    def __init__(self, res):
        self.values = res["results"] 
        self.options = {}

    def select_recipe(self): # loops through results and prints each value
        for i, value in enumerate(self.values): #makes list enumerable
            print(str(i+1) + ". " + value["title"]) # the number user will choose
            self.options[i+1] = value["title"]

        if len(self.options) < 1: # if no recipes appear from API call, user is notified
            print("No recipes found")
            return

        
        choice = input("Select a recipe - ")
        title = self.options[int(choice)] # storing the name of the recipe that user selects

        for value in self.values: # searching each of the ten recipes for the selected title to see if match
            if value["title"] == title:
                return value["id"] #returning recipes id number from api

    def select_ingredients(self, id, url, key):
        apiInformation = url + str(id) + "/information?apiKey="+key # returning the information tag from recipe database
        res = requests.get(apiInformation).json()

        ingredients = res["extendedIngredients"]

        print("ingredients")

        for ingredient in ingredients:
            amount = str(ingredient["measures"]["metric"]["amount"]).replace(".0", "") #represents number within measurement
            unit = ingredient["measures"]["metric"]["unitShort"] #represents unit (e.g grams) within measurement
            fullName = ""
            if len(unit) > 0:
                fullName = amount + " " + unit + " " + ingredient["nameClean"] #produces ingredient + amount / unit
            else:
                fullName = amount + " " + ingredient["nameClean"] 
        
            print(fullName)

    def select_instructions(self, id, url, key):
        apiInformation = url + str(id) + "/information?apiKey="+key # returning the information tag from recipe database
        res = requests.get(apiInformation).json()

        print(res["instructions"])
