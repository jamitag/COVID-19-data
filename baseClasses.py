import requests

class Category():
    def __init__(self, api, param):
        self.api = api + "&"+param+"=" #generlising the init across all category classes

    def printUrl(self):
        print(self.api)

    def search(self, type):
        return requests.get(self.api+type).json() #making the api call
