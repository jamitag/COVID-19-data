import simpleSearch as ss

"""
Defines the algorithm for processing natural language inputted by user
"""
class Algorithm():

    cuisines = ["british", "chinese", "italian"]

    def __init__(self, api):
        self.api = api

    def searchBy(self, text):
        for cuisine in self.cuisines:
            if cuisine in text:
               c = ss.Cuisine(self.api)
               self.api = c.url(cuisine)

        return self.api