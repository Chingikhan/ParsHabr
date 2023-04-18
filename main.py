import requests
import json

post_id = 727758
url = f"https://m.habr.com/kek/v2/articles/{post_id}"

headers = {'Authorization': 'Bearer <TOKEN>'}
params = {'param1': 'value1', 'param2': 'value2'}

response = requests.get(url, headers=headers, params=params)
data = json.loads(response.text)

keys = data.keys()

for key in keys:
    print(key)
