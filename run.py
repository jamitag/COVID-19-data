import requests
import simpleSearch
url = "https://api.spoonacular.com/recipes/complexSearch?apiKey=c36e1425cde0460bb5ee0bec9952d123"
c = simpleSearch.Cuisine(url)
d = simpleSearch.Diet(url)
print(d.search("french"))
c.printUrl()

