import requests

url = "https://cdn.ninjasaga.cc/cdn/swf/latest/swf/panels/clan_panel.swf?_t=1775138288055"
r = requests.get(url)

if r.status_code == 200:
    # Save as binary file
    with open("clan_panel.swf", "wb") as f:
        f.write(r.content)
    print("SWF file downloaded successfully")
else:
    print(f"Failed: {r.status_code}")