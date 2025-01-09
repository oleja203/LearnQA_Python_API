import requests
import time
import json

response = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job')

param = json.loads(response.text)
token = {'token': f'{param['token']}'}
sec = param['seconds']

response = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params=token)

param = json.loads(response.text)
status = param['status']

if status == 'Job is NOT ready':
    print(f'status: = {status}')

    time.sleep(int(sec))

    response = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params=token)

    param = json.loads(response.text)
    status = param['status']
    result = param['result']

    if status == 'Job is ready' and int(result) > 0:
        print(f'status: = {status} | result: = {result}')
    else:
        print('Status or result is incorrect')

else:
    print('Status is incorrect')