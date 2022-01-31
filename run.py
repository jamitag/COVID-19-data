import requests
import simpleSearch
from algorithm import Algorithm as A
from baseClasses import Search

url = "https://api.spoonacular.com/recipes/complexSearch?apiKey=c36e1425cde0460bb5ee0bec9952d123"

text = input("What recipes would you like? ")

a = A(url) 

search = a.searchBy(text) 

print(Search.get(search))
