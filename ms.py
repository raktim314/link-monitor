import requests
import json

url = "https://medium.com/dreamcatcher-its-blog?format=json"

response = requests.get(url, verify=True)
txt = response.text
txt = txt.replace('])}while(1);</x>','')
json_string = json.dumps(txt)

data = dict(json.loads(json_string))

# if "payload" in data:
# 	if "collection" in data["payload"]:
# 		print(data["payload"]["collection"])

print(type(data))