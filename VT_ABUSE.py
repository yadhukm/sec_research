import requests
import json

VT_API_KEY= '93174196079fc424e2d5676fea92b601c7a9e68d76feddb88d9bf4c509a065cd'

check = input("enter the IP in double quotes: ")

VTurl = 'https://www.virustotal.com/vtapi/v2/ip-address/report'

VTparams = {'apikey': VT_API_KEY, 'ip': check}

VTresponse = requests.get(VTurl, params=VTparams)

VTresponse_json = json.loads(VTresponse.content)

VT_result= VTresponse_json['detected_urls'][0]['positives']

print ("suspicious score as per virus total: " , VT_result)
#print VTresponse_json['detected_urls'][0]['positives']


# Defining the api-endpoint
ABurl = 'https://api.abuseipdb.com/api/v2/check'

querystring = {
    'ipAddress': check,
    'maxAgeInDays': '90'
    #'confidenceMinimum'>'10'
}

headers = {
    'Accept': 'application/json',
    'Key': 'c3e20728598eaa98abc0fc6028bfa6e4bf05aee82353a9eac309c19e9370b5712baf650eaaed69d8'
}

ABresponse = requests.request(method='GET', url=ABurl, headers=headers, params=querystring)
ABresponse_json = json.loads(ABresponse.content)
AB_result = ABresponse_json['data']['abuseConfidenceScore']


print ("suspicious score as per AbuseIPDB: " , AB_result)
#print ABresponse_json['data']['abuseConfidenceScore']






