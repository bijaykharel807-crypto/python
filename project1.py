import requests
import json
api_key = "55f8e565e2f2f530-dfae35ac530449e5-e93d4543f4be0581"


user_id = "XyTuRGd0jRXOKKjcdv/jzg=="

viber_data={
    "auth_token":api_key, 
    "from":user_id, 
    "type":"text", 
    "text":"Hello world!" 
}




viber_data['text']=1

viber_url = "https://chatapi.viber.com/pa/post"
url ="https://mybbc-analytics.files.bbci.co.uk/analytics-remote-config/producers.json"

r = requests.get(url)
if r.status_code == 200:
    data = r.json()

   
    if isinstance(data, dict):
        final = data.items()  
        for key, value in final:
     
            value_str = json.dumps(value) if isinstance(value, dict) else str(value)
            result = f"{key} - {value_str}"

            viber_data['text'] = result

           
            resp = requests.post(
                viber_url,
                headers={"Content-Type": "application/json"},
                data=json.dumps(viber_data)
            )

         
            print("Sent:", result)
            print("Viber response:", resp.json())

    elif isinstance(data, list):
        for item in data:
            
            result = str(item)
            viber_data['text'] = result

            resp = requests.post(
                viber_url,
                headers={"Content-Type": "application/json"},
                data=json.dumps(viber_data)
            )

            print("Sent:", result)
            print("Viber response:", resp.json())

    else:
        print("Unknown JSON structure")

else:
    print("GET request failed with status code:", r.status_code)