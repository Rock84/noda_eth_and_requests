from fastapi import FastAPI
import requests

headers = {
    'Content-Type': 'application/json',
}

json_data = {
    'jsonrpc': '2.0',
    'method': 'eth_getBalance',
    'params': [
#        '0x6747937e365405adb95aebc7bc0a8db07592bab8', #null money
        '0xdc3EC8947438F7A834C3F38ce98B2243089CF7e6', #many money
        'latest',
    ],
    'id': 1,
}

response = requests.post('http://127.0.0.1:8545', headers=headers, json=json_data)

print(response.text)
