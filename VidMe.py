import requests
import pprint
import json

#prints everything needed
def printr():
    print("======BREAK======")
    print ("URL = " + r.url)
    print ("Status Code = ")
    print(r.status_code)
    print ("Reason = " + r.reason)
    print ("PPRINT BREAK")
    print ("PPRINT BREAK")
    pprint.pprint (r.json())
    print("======BREAK======")
    return;

#Check App Works
url = 'https://api.vid.me/auth/check'
Auth = ('YOUR KEY HERE' , 'YOUR SECRET HERE')
headers = {'Authorization':'Basic'}

r  = requests.post(url, headers=headers, auth=Auth)

printr()
#End Check

#Get Token
url = 'https://api.vid.me/auth/create'
user = 'YOUR USERNAME HERE'
passwd = 'YOUR PASSWORD HERE'
payload = {'username': user, 'password':passwd}
r = requests.post(url, headers=headers, auth=Auth, params=payload)

printr()

GetToken = r.text
ParsedToken = json.loads(GetToken)
Token = ParsedToken['auth']['token']
print ("Token = "+ Token)
#We Have Token

headers = {'Authorization':'Basic', 'AccessToken':Token}

#Let's Make an Album
url = 'https://api.vid.me/album'
title = 'Album Title'
payload = {'title': title}
r = requests.post(url, headers=headers, auth=Auth, params=payload)

printr()
