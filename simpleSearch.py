import requests
import baseClasses as bc

class Cuisine(bc.Category):
    def __init__(self, api):
        bc.Category.__init__(self, api, "cuisine") #initialises the api to search by cuisine