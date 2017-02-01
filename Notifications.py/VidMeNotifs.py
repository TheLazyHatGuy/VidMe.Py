import json
import pprint
import time
import requests
import config
import BlindDate as BD


#https://vid.me/oauth/authorize?client_id=khLRjt0oQrI4hKUkUWJFveXEd47VcymF&redirect_uri=http://flyingtoilet.co.uk&scopes=albums%20account
#prints everything needed
def printr():
    print("======VidMe BREAK======")
    print ("URL = " + r.url)
    print ("Status Code = ")
    print(r.status_code)
    print ("Reason = " + r.reason)
    print ("PPRINT BREAK")
    print ("PPRINT BREAK")
    pprint.pprint (r.json())
    print("======VidMe BREAK======")
    return;

#Check App Works
url = 'https://api.vid.me/auth/check'
Auth = (config.VidMeClientKey , config.VidMeClientSecret)
headers = {'Authorization':'Basic'}

r  = requests.post(url, headers=headers, auth=Auth)

printr()
#End Check

while True:
    # Get Token
    url = 'https://api.vid.me/auth/create'
    payload = {'username': config.VidMeUserName, 'password': config.VidMePassword}
    r = requests.post(url, headers=headers, auth=Auth, params=payload)

    printr()

    GetToken = r.text
    ParsedToken = json.loads(GetToken)
    Token = ParsedToken['auth']['token']
    config.Token = Token
    print("Token = " + Token)
    # We Have Token

    headers = {'Authorization': 'Basic', 'AccessToken': Token}

    print ("RUN NOTIFICATION.PY")
    #Let's Try Notifications
    #The Notifcations URL ouputs everything so save it to a file
    url = 'https://api.vid.me/notifications'
    r = requests.get(url, headers=headers, auth=Auth)

    print ("Creating Notifs.txt")

    file = open("notifs.txt", "w")
    file.write(r.text)
    file.close()

    print ("Notifs.txt created")
    BD.runnotifs()
    print ("Now we Sleep")
    time.sleep(60)
    print ("Here we go again")

