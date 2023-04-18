import requests
import json

post_id = 727758
url = f"https://m.habr.com/kek/v2/articles/{post_id}"

response = requests.get(url)

data = json.loads(response.text)

print(data.keys())
print("Time:", data["timePublished"])
