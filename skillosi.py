import requests
import json

headers = {
    'accept': 'application/json, text/plain, */*',
    # 'accept-encoding': 'gzip',
    'accept-language': 'fr',
    'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJXekg2dDhDeEJFbUZibFBSUHRFVl9Pamt1a3JTdHM0cEh0ZGJ0aE5XR0c4In0.eyJleHAiOjE3NDc4MzEzMTAsImlhdCI6MTc0NzgzMTAxMCwianRpIjoiOTM5NTQwMTMtODAxOC00NzUyLWI4NmEtOTVkZDkzZjU4NjdkIiwiaXNzIjoiaHR0cHM6Ly9hdXRoLWpwdi5lbG9zaS5jb20vYXV0aC9yZWFsbXMvZWxvc2kiLCJhdWQiOlsic2tpbGxvc2kiLCJhY2NvdW50Il0sInN1YiI6Ijk2YTNlZjE4LWE4NDUtNDQ5OS05NTZmLWM5Yzg0YjFiY2MyYiIsInR5cCI6IkJlYXJlciIsImF6cCI6InNraWxsb3NpIiwic2Vzc2lvbl9zdGF0ZSI6IjQ2NzljYTI0LTBmMjktNDJmNi05ZGJmLThkYjljMDVmMjc2NyIsImFsbG93ZWQtb3JpZ2lucyI6WyJodHRwczovL3NraWxsb3NpLmVsb3NpLmNvbS8iLCJodHRwczovL2tiZGV2MC1za2lsbG9zaS5lbG9zaS5sYW4iLCJodHRwczovL2prOHNpdGcwMS1za2lsbG9zaS5lbG9zaS5sYW4iXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iLCJkZWZhdWx0LXJvbGVzLWVsb3NpIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJza2lsbG9zaV9hdWRpZW5jZSBncm91cHMgZW1haWwgcHJvZmlsZSIsInNpZCI6IjQ2NzljYTI0LTBmMjktNDJmNi05ZGJmLThkYjljMDVmMjc2NyIsIm5hbWUiOiJZYXNzaW5lIEVsIGhhbGkiLCJncm91cHMiOlsiRUxPU0kgU3RhZ2lhaXJlIiwiZGV2ZWxvcHBlciIsIldJRklfVXNlcnMiLCJFTE9TSSBDb2xsYWJvcmF0ZXVyIl0sInByZWZlcnJlZF91c2VybmFtZSI6Inlhc3NpbmUuZWxoYWxpIiwiZ2l2ZW5fbmFtZSI6Illhc3NpbmUiLCJmYW1pbHlfbmFtZSI6IkVsIGhhbGkiLCJlbWFpbCI6Inlhc3NpbmUuZWxoYWxpQGVsb3NpLmNvbSJ9.Rk23nj5t1mMhuWrc0-f9FOpHpvc2qC6HfFI6kz3Wfh8W-FVBXd-v_ckbOfhB_0STSPao08nvHrRXUW7JpBWCOLpuUUCRf4uKQbIKIaQXSaTMe-PPohQi6r2HNvbfQPwKkDlwnX9TfKBWy0wYDzX1MJsGDeS9mDjgVRUSNRoyuDGtLqESfKXRUY34uuWMUtOVUv2O774vz6Z_IA51klq5M4Jr-cLVJw6m7u_qokzQ8tjkKUqImUwTMtxTGsFqd6UFhH2q3Hyl1aSJg31jXupws0zcwFcbc3DnpzXkaBhKP4jCAgDVSoRXNBpAjyb-3L5JAnX7Dk4l_LtS9J4ZRxE91A',
    'connection': 'keep-alive',
    # 'cookie': '_pk_ref.14.1560=%5B%22%22%2C%22%22%2C1747830225%2C%22https%3A%2F%2Fbookmarks.elosi.com%2F%22%5D; _pk_id.14.1560=2703fa3bcae8c7f7.1747830225.; _pk_ses.14.1560=1',
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