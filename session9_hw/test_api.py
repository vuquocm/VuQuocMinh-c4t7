import requests
import json
r = requests.get('https://jsonplaceholder.typicode.com/users')
list_json = r.json()
a = str.upper(input('enter a username'))
for i in list_json:
    # if i['username'] == 'Delphine':
    if str.upper(i['username']) == a:
        print(i)
    