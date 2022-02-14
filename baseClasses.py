import requests


class Category():
    """Sets the base attributes for all cat classes within the programme
    """

    def __init__(self, api, param):
        self.api = api + "&"+param+"="

    def url(self, type):
        """
        Function description
        """

        return self.api+type  # adds the value from the user input


class Search():
    """for interactions with the API
    """
    def get(api):
        """
        sends a get request to the api and returns the json response
        """
        return requests.get(api).json()
