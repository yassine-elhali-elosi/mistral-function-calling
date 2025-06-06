import requests
import json

#####################################################################
### J'avais commencé, mais pas terminé car j'étais passé sur les MCP
#####################################################################

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'fr',
    'authorization': 'Bearer ey...',
    'connection': 'keep-alive',
    'host': 'skillosi.elosi.com',
    'referer': 'https://skillosi.elosi.com/gallery',
    'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
}

response = requests.get('https://skillosi.elosi.com/api/employees/galleries', headers=headers)

print(response)

def store_json_response(response, filename='response.json'):
    with open(filename, 'w') as f:
        json.dump(response, f, indent=4)

#store_json_response(response.json(), 'response.json')