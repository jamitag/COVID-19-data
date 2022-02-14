import simpleSearch as ss
import random


class Algorithm():
    """Defines the algorithm for processing natural language inputted by user
    """

    def __init__(self, api, key):
        self.api = api + "complexSearch?number=10&offset="\
             + str(random.randint(0, 100))+"&apiKey=" + key
        self.originalApi = self.api
        self.cuisines = ["chinese", "italian", "british",
                         "greek", "japanese", "indian"]
        self.diets = ["vegetarian", "vegan", "paleo"]

    def search_by(self, text):
        """
        Function description
        """

        for cuisine in self.cuisines:
            if cuisine in text:
                c = ss.Cuisine(self.api)
                self.api = c.url(cuisine)

        for diet in self.diets:
            if diet in text:
                d = ss.Diet(self.api)
                self.api = d.url(diet)

        if self.api == self.originalApi:
            choice = input("You have entered no specific criteria"
                           " would you like to continue? (Y/N) ")

            if choice.upper() == "N":
                raise ValueError()

        return self.api
