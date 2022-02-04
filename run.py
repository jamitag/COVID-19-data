import requests
import simpleSearch
import secrets
import random
from algorithm import Algorithm as A
from baseClasses import Search
from display import Recipes

key = str(secrets.ApiKey())

url = "https://api.spoonacular.com/recipes/"

text = input("What recipes would you like? ")

a = A(url, key)

search = a.searchBy(text) 

res = Search.get(search)

r = Recipes(res)

id = r.selectRecipe()

r.selectIngredients(id, url, key)