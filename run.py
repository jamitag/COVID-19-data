import requests
import simpleSearch
url = "https://api.spoonacular.com/recipes/complexSearch?apiKey=c36e1425cde0460bb5ee0bec9952d123"
c = simpleSearch.Cuisine(url)
print(d.search("italian"))
d.printUrl()


