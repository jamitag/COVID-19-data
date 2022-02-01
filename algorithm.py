import simpleSearch as ss

"""
Defines the algorithm for processing natural language inputted by user
"""
class Algorithm():

    def __init__(self, api):
        self.api = api
        self.cuisines = ["british", "chinese", "italian"]
        self.diets = ["vegetarian", "vegan", "paleo"]

    def searchBy(self, text):
        for cuisine in self.cuisines:
            if cuisine in text:
               c = ss.Cuisine(self.api)
               self.api = c.url(cuisine)
        
        for diet in self.diets:
            if diet in text:
                d = ss.Diet(self.api)
                self.api = d.url(diet)
        
        return self.api
