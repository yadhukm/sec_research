import requests
import json

API_KEY= '93174196079fc424e2d5676fea92b601c7a9e68d76feddb88d9bf4c509a065cd'

check = input("enter the url in double quotes: ")

url = 'https://www.virustotal.com/vtapi/v2/url/report'

params = {'apikey': API_KEY, 'resource': check}

response = requests.get(url, params=params)

response_json = json.loads(response.content)

y= response_json['positives']

x=response_json['url']

print(x)

if y==0:
        print("non malicious")
elif y>0 and y<50:
        print("suspicious")
elif y>50:
        print ("higly suspicious")

else:
        print("url not_detected")

