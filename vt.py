mport requests
import json

API_KEY= '93174196079fc424e2d5676fea92b601c7a9e68d76feddb88d9bf4c509a065cd'

check = 'google.com'

url = 'https://www.virustotal.com/vtapi/v2/url/report'

params = {'apikey': API_KEY, 'resource': check}

response = requests.get(url, params=params)

print(response.json())

