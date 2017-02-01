# VidMe.Py
What I have managed to do with the Vid.Me API so far.

[Check me out on Vid.Me](https://vid.me/TheLazyHatGuy)
##Setup
[Install Python 3.4.6](https://www.python.org/downloads/release/python-346/)

[Install pip](https://pip.pypa.io/en/stable/installing/)

Install Requests
```
pip install requests
```

Setup a Vid.Me Application - https://vid.me/oauth/clients

Authorise using this format
```
https://vid.me/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&scopes=account
```

Get a PushBullet Access Token - https://www.pushbullet.com/#settings/account

Edit the values in config.py

Run VidMeNotifs.py
```
python VidMeNotifs.py
```
