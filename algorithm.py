import simpleSearch as ss
import random


class Algorithm():
    """Defines the algorithm for processing natural language inputted by user
    """

    def __init__(self, api, key):
        self.api = api + "complexSearch?number=10&offset="\
             + str(random.randint(0, 5))+"&apiKey=" + key  #when the offset of the randint method is too high, the API throws an 404 error(not found) for cuisines that dont have many recipes e.g british. Lowered to decrease chance of error
        self.originalApi = self.api
        self.cuisines = ["chinese", "italian", "british",
                         "greek", "japanese", "indian"]
        self.diets = ["vegetarian", "vegan", "paleo"]

    def search_by(self, text):
        """
        Function description
        """
        text = text.lower()

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
