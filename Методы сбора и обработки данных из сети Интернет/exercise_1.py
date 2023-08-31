import requests
from pprint import pprint

access_token = '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'
url = 'https://api.github.com/users/TuchinRoman1996/repos'
header = {'Accept': 'application/vnd.github+json',
          'Authorization': f'token {access_token}'}

response = requests.get(url, headers=header)
j_data = response.json()

pprint(j_data)

with open('myRepo.json', 'w') as file:
    file.write(str(j_data))
