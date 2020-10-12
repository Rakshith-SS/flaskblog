## fetch  dad jokes from 
## https://icanhazdadjoke.com
## and return an array of 5 jokes

import requests
import random

headers = {"Accept":"Application/json" }
params = {"limit" : 5}
joke = []
def fetch_joke():
    number_of_pages = [i for i in range(1,131)]
    n = random.choice(number_of_pages)
    headers = {"Accept":"Application/json" }
    params = {"page": n,"limit" : 5}
    resp = requests.get('https://icanhazdadjoke.com/search', headers=headers , params = params)
    data = resp.json()
    data_ = data['results']
    for dadjoke in data_:
        joke.append(dadjoke['joke'])
    return joke