import requests
import json

post_id = 727758
url = f"https://m.habr.com/kek/v2/articles/{post_id}"  # замените на реальный URL API

# Опционально: установить заголовки и параметры запроса, если это требуется API
headers = {'Authorization': 'Bearer <TOKEN>'}  # замените на реальный токен, если это требуется API
params = {'param1': 'value1', 'param2': 'value2'}  # замените на реальные параметры, если это требуется API

# Отправить GET-запрос и получить ответ в формате JSON
response = requests.get(url, headers=headers, params=params)
data = json.loads(response.text)

# Получение всех ключей словаря
keys = data.keys()

# Печать всех ключей
for key in keys:
    print(key)