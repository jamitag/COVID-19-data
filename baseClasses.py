import requests

"""
Sets the base attributes for all cat classes within the programme
"""
class Category():
    def __init__(self, api, param):
        self.api = api + "&"+param+"=" #generlising the init across all category classes

    def url(self, type):
        return self.api+type

class Search():

    def get(api):
        return requests.get(api).json() #making the api call
