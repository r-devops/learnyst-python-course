import requests 

response = requests.get('https://api.github.com')
print(dir(response))
print(response.status_code)
print(response.text)

