import requests
from itertools import product

methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
params = [
    {'method': 'GET'},
    {'method': 'POST'},
    {'method': 'PUT'},
    {'method': 'PATCH'},
    {'method': 'DELETE'}
]
url = "https://playground.learnqa.ru/ajax/api/compare_query_type/"

for method, param in product(methods, params):
    req = requests.Request(method, url, params=param)
    prepared = req.prepare()
    with requests.Session() as session:
        response = session.send(prepared)
    print(prepared.method, param, response.text)

