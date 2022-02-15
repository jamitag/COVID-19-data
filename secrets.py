import json


class ApiKey():
    """
    Sources the API key to make api call from creds.json
    """
    def __str__(self):
        f = open("creds.json")
        return json.load(f)["apiKey"]
