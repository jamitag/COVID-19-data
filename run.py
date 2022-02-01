import requests
import simpleSearch
import secrets
from algorithm import Algorithm as A
from baseClasses import Search
from display import Recipes

key = str(secrets.ApiKey())

url = "https://api.spoonacular.com/recipes/complexSearch?number=10&apiKey=" + key

text = input("What recipes would you like? ")

a = A(url) 

search = a.searchBy(text) 


