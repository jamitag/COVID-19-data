import requests
import baseClasses as bc
"""
Searching by cuisine
"""
class Cuisine(bc.Category):
    def __init__(self, api):
        bc.Category.__init__(self, api, "cuisine") #initialises the api to search by cuisine

"""
Searching by diet
"""
class Diet(bc.Category):
    def __init__(self, api):
        bc.Category.__init__(self, api, "diet") #initialises the api to search by diet
