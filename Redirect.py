import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")


for redirect in response.history:
    print(redirect.url)
print(len(response.history))
