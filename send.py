
# Simple file to test the authentication with JWT, instead of using Postman
import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTI1NTY1MTgzLCJqdGkiOiI1MDdhZWRhMDkxZGE0OWI3YWFhMDcyMDkxMWFmNTg0NiIsInVzZXJfaWQiOjF9.hp5M2h9UUgQ50v25K-CyVz4Cqy_MaGdd7ooow22HJFM'

res = requests.get('http://localhost:8000/api/v1/kids/', headers=headers)
print(res.text)
