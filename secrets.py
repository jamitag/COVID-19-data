import json

"""
Sources the API key to make api call from secrets.json
"""

class ApiKey(): # repr / str means that the class has value i.e in this case a string 'apiKey'
    def __str__(self):
        f = open("secrets.json")
        return json.load(f)["apiKey"]