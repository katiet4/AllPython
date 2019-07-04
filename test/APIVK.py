import requests
req = requests.get('https://api.vk.com/method/users.get?user_id=1&v=5.52')
print(req.json())