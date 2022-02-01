class Recipes():
    def __init__(self, res):
        self.values = res["results"]

    def selectRecipe(self): # loops through results and prints each value
        for i, value in enumerate(self.values):
            print(str(i+1) + ". " + value["title"])

