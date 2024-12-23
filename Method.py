import requests
from itertools import product

url = "https://playground.learnqa.ru/ajax/api/compare_query_type/"
method_get = ['GET']
methods = ['POST', 'PUT', 'PATCH', 'DELETE']
params = [
    {'method': 'GET'},
    {'method': 'POST'},
    {'method': 'PUT'},
    {'method': 'PATCH'},
    {'method': 'DELETE'}
]

for get, param in product(method_get, params):
    req = requests.Request(get, url, params=param)
    prepared = req.prepare()
    with requests.Session() as session:
        response = session.send(prepared)
    print(prepared.method, param, response.text)

for method, param in product(methods, params):
    req = requests.Request(method, url, data=param)
    prepared = req.prepare()
    with requests.Session() as session:
        response = session.send(prepared)
    print(prepared.method, param, response.text)


