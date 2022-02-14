import requests
import re


class Recipes():
    """Unlocking the list of recipes to enable indexing and user selection and
       returning user friendly data from the API
    """

    def __init__(self, res):
        self.values = res["results"]
        self.options = {}

    def select_recipe(self):
        """
        Loops through results and prints each value
        """
        self.options = {}

        for i, value in enumerate(self.values):  # makes list enumerable
            print(str(i+1) + ". " + value["title"])
            # the number the user will choose
            self.options[i+1] = value["title"]

        print(self.options)

        if len(self.options) < 1:
            # if no recipes appear from API call, user is notified
            print("No recipes found")
            return

        choice = input("Select a recipe - ")

        numberChoice = 0

        try:
            numberChoice = int(choice)
            if numberChoice < 1 or numberChoice > 10:
                raise ValueError("Incorrect Input")
        except:
            print("\n Incorrect input \n")
            self.select_recipe()

        title = self.options[numberChoice]
        # storing the name of the recipe that user selects

        for value in self.values:
            # Searching list of recipes for the selected title to see if match
            if value["title"] == title:
                return value["id"]  # Returning recipes id number from api

    def select_ingredients(self, id, url, key):
        """
        Pulling 'ingredient' parameter from object and formatting
        """

        apiInformation = url + str(id) + "/information?apiKey="+key
        # returning the information tag from recipe database
        res = requests.get(apiInformation).json()

        ingredients = res["extendedIngredients"]

        print("ingredients")

        for ingredient in ingredients:
            amount = str(ingredient["measures"]["metric"]["amount"])\
                .replace(".0", "")
            # Represents number within measurement
            unit = str(ingredient["measures"]["metric"]["unitShort"])
            # Represents unit (e.g grams) within measurement
            fullName = ""
            if isinstance(ingredient["nameClean"], str):  # checks wether the value is an instance of string
                if len(unit) > 0:
                    fullName = amount + " " + unit + " " + ingredient["nameClean"]
                # Produces ingredient + amount / unit
                else:
                    fullName = amount + " " + ingredient["nameClean"]

            print(fullName)

    def select_instructions(self, id, url, key):
        """
        Pulling the 'instruction' parameter from the object and manuipulating format
        """

        apiInformation = url + str(id) + "/information?apiKey="+key
        # Returning the information tag from recipe database
        res = requests.get(apiInformation).json()

        instructions = res["instructions"]

        if re.match(r'^\<', instructions):
            instructions = re.sub("<ol>", "\n", instructions)
            instructions = re.sub("<li>", "\n", instructions)
            instructions = re.sub("</li>", "\n", instructions)
            instructions = re.sub("</ol>", "\n", instructions)
        else:
            instructions = re.sub(".", ". \n", instructions)

        print(instructions)


