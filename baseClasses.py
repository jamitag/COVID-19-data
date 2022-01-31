import requests

"""
Sets the base attributes for all cat classes within the programme
"""
class Category(): 
    def __init__(self, api, param):
        self.api = api + "&"+param+"=" 

    def url(self, type):
        return self.api+type # adds the value from the user input

class Search(): 

    def get(api):
        return requests.get(api).json() 
