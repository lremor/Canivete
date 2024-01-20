import requests
import json
import pprint 

linkao = "https://api.linketrack.com/track/json?user=teste&token=1abcd00b2731640e886fb41a8a9671ad1434c599dbaa0a0de9a5aa619f29a83f&codigo=NL867716580BR"

response = requests.get(linkao)

if response.status_code == 200:
        data = json.loads(response.text)
        pprint.pprint(data)
    
        codigo = data["codigo"]
        status = data["eventos"][0]["status"]

        print(f"{codigo} status: {status}.")
        
    
else:
        print(f"Error: {response.status_code} - {response.text}")
