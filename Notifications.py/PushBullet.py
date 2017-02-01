import requests
import pprint
import json
import config
#prints everything needed
def printr(r):
    print("======PB BREAK======")
    print ("URL = " + r.url)
    print ("Status Code = ")
    print(r.status_code)
    print ("Reason = " + r.reason)
    print ("PPRINT BREAK")
    print ("PPRINT BREAK")
    pprint.pprint (r.json())
    print("======PB BREAK======")
    return;


url = 'https://api.pushbullet.com/v2/users/me'
headers = {'Access-Token':config.PushBulletAcessToken}

r  = requests.get(url, headers=headers)

printr(r)

GetIDEN = r.text
ParsedToken = json.loads(GetIDEN)
IDEN = ParsedToken['iden']
print ("Client IDEN = "+ IDEN)

def push (title, body, notifurl):
    url = 'https://api.pushbullet.com/v2/pushes'
    headers = {'Access-Token':config.PushBulletAcessToken,
               'Content-Type':'application/json',
               'client_iden':IDEN}
    pushinfo = {'type':'link',
                'title':str(title),
                'body':str(body),
                'url':str(notifurl)}
    print ("URL -",url)
    print ("Headers -",headers)
    print ("Push Info -",pushinfo)
    r = requests.post(url, headers=headers, data=json.dumps(pushinfo))
    printr(r)
