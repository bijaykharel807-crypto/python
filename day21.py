import requests
url = "https://www.onlinekhabar.com/smtm/home/high-52-week"

r = requests.get (url=url)
if r.status_code ==200 :
    data = r.json ()["response"]
    for i in data :
        print(f"{i['ticker']}")