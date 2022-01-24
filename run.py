import requests
import simpleSearch
import algorithm

url = "https://api.spoonacular.com/recipes/complexSearch?apiKey=c36e1425cde0460bb5ee0bec9952d123"

text = input("What recipes would you like? ")

a = algorithm.Algorithm(url)

print(a.searchBy(text))