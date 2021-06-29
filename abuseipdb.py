import requests
import json

# Defining the api-endpoint
url = 'https://api.abuseipdb.com/api/v2/check'

x = input("enter the ip ")
querystring = {
    'ipAddress': x,
    'maxAgeInDays': '90'
}

headers = {
    'Accept': 'application/json',
    'Key': 'c3e20728598eaa98abc0fc6028bfa6e4bf05aee82353a9eac309c19e9370b5712baf650eaaed69d8'
}

response = requests.request(method='GET', url=url, headers=headers, params=querystring)

# Formatted output
decodedResponse = json.loads(response.text)
print json.dumps(decodedResponse, sort_keys=True, indent=4)
