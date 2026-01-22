import requests
import json
api_key = "55e1ee6facb2561a-816352c07d3a5846-4c5a2e3606d12391"


user_id = 'R8jZNLHDJja7VAWIxaH3BQ=='



data= {
   "auth_token":"55e1ee6facb2561a-816352c07d3a5846-4c5a2e3606d12391",
   "from":"R8jZNLHDJja7VAWIxaH3BQ==",
    "type":"text",
    "text":"Hello sir "
}

url = "https://chatapi.viber.com/pa/post"
r = requests.post(url=url, data=json.dumps(data))
if r.status_code == 200:
    print(r.json())