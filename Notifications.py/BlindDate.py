import json
import sys
import requests
import config
import pprint
import PushBullet as PB

def NotifRead(ID):
    headers = {'Authorization': 'Basic', 'AccessToken': config.Token}
    url = 'https://api.vid.me/notifications/mark-read'
    Auth = (config.VidMeClientKey, config.VidMeClientSecret)
    payload = {'notifications[]': ID}
    r = requests.post(url, headers=headers, auth=Auth, params=payload)

    print("======BD BREAK======")
    print("URL = " + r.url)
    print("Status Code = ")
    print(r.status_code)
    print("Reason = " + r.reason)
    print("PPRINT BREAK")
    print("PPRINT BREAK")
    pprint.pprint(r.json())
    print("======BD BREAK======")

    return

def PBPipe(NTT, Message, URL):
    print ("Start PushBullet Pipe")
    print ("===PB Pipe Break===")
    print ("NTT -",NTT)
    print ("Message -",Message)
    print ("URL -",URL)
    PB.push(title=NTT, body=Message, notifurl=URL)
    print ("Push Sent")
    print("===PB Pipe Break===")
    return
def runnotifs():
    file = open("notifs.txt", "r")

    notifs = json.loads(file.read())
    NotifCount= notifs['unreadCount']

    unread = int(NotifCount)
    if (unread == 0):
        print ("No Unread Notifications")
    elif (unread >= 1):
        print ("You have", unread, "unread notification(s)")
        notif = unread -1
        while True:
            if notif >=0:
                print ("Count - ",notif)
                NotifID = notifs['notifications'][notif]['notification_id']
                NotifType = notifs['notifications'][notif]['type']
                NotifUserName = notifs['notifications'][notif]['actor']['displayname']
                if (NotifUserName == 'None'):
                    NotifUserName = notifs['notifications'][notif]['actor']['username']
                print ("ID - ",NotifID)
                print ("Type - ",NotifType)
                print ("User Name - ",NotifUserName)

                if (NotifType == 'video-commented'):
                    NotifVidName = notifs['notifications'][notif]['video']['title']
                    print ("Video Name - ",NotifVidName)
                    NotifCommentURL = notifs['notifications'][notif]['comment']['full_url']
                    print ("Comment Url - ",NotifCommentURL)

                    Message = (NotifUserName+ " commented on your video "+ NotifVidName)
                    PBPipe(NTT='Someone commented on your video', Message=Message, URL=NotifCommentURL)

                    notif = notif -1
                    NotifRead(ID=NotifID)
                elif (NotifType == 'user-subscribed'):
                    print ("New follower")
                    NotifUserUrl = notifs['notifications'][notif]['actor']['full_url']
                    print ("User URL -",NotifUserUrl)

                    Message = (NotifUserName+ " followed you")
                    PBPipe(NTT='You have a new follower', Message=Message, URL=NotifUserUrl)

                    notif = notif -1
                    NotifRead(ID=NotifID)
                elif (NotifType == 'video-upvoted'):
                    NotifVidName = notifs['notifications'][notif]['video']['title']
                    print ("Video Name - ",NotifVidName)
                    NotifVidUrl = notifs['notifications'][notif]['video']['full_url']
                    print ("Video URL - ",NotifVidUrl)
                    print ("Your video was upvoted")

                    Message = (NotifUserName+ " upvoted your video "+ NotifVidName)
                    PBPipe(NTT='Someone commented on your video', Message=Message, URL=NotifVidUrl)

                    notif = notif -1
                    NotifRead(ID=NotifID)
                elif (NotifType == 'comment-upvoted'):
                    NotifVidName = notifs['notifications'][notif]['video']['title']
                    print ("Video Name - ",NotifVidName)
                    NotifCommentURL = notifs['notifications'][notif]['comment']['full_url']
                    print ("Comment Url - ",NotifCommentURL)
                    print ("Your comment was upvoted")

                    Message = (NotifUserName+ " upvoted your comment on "+ NotifVidName)
                    PBPipe(NTT='Someone upvoted your commented on a video', Message=Message, URL=NotifCommentURL)

                    notif = notif -1
                    NotifRead(ID=NotifID)
                elif (NotifType == 'messaged'):
                    print ("Someone messaged you")
                    NotifMessageURL = notifs['notifications'][notif]['message']['url']
                    print ("Message URL -",NotifMessageURL)

                    Message = (NotifUserName+ " sent you a message")
                    PBPipe(NTT='Someone sent you a message', Message=Message, URL=NotifMessageURL)

                    notif = notif -1
                    NotifRead(ID=NotifID)
                elif (NotifType == 'comment-replied-to'):
                    NotifVidName = notifs['notifications'][notif]['video']['title']
                    print ("Video Name - ",NotifVidName)
                    print ("Someone replied to your comment")
                    NotifCommentURL = notifs['notifications'][notif]['comment']['full_url']
                    print ("Comment Url - ",NotifCommentURL)

                    Message = (NotifUserName+ " replied to your comment on "+ NotifVidName)
                    PBPipe(NTT='Someone replied to you comment', Message=Message, URL=NotifCommentURL)

                    notif = notif -1
                    NotifRead(ID=NotifID)
                elif (NotifType == 'comment-mention'):
                    NotifVidName = notifs['notifications'][notif]['video']['title']
                    print ("Video Name - ",NotifVidName)
                    print ("Someone mentioned you in a comment")
                    NotifCommentURL = notifs['notifications'][notif]['comment']['full_url']
                    print ("Comment Url - ",NotifCommentURL)

                    Message = (NotifUserName+ " mentioned you on " +NotifVidName)
                    PBPipe(NTT='Someone mentioned you', Message=Message, URL=NotifCommentURL)

                    notif = notif -1
                    NotifRead(ID=NotifID)
                elif (NotifType == 'tipped'):
                    NotifVidName = notifs['notifications'][notif]['video']['title']
                    print("Video Name - ", NotifVidName)
                    NotifVidUrl = notifs['notifications'][notif]['video']['full_url']
                    print("Video URL - ", NotifVidUrl)
                    print("Someone tipped your video")

                    Message = (NotifUserName + " tipped your video " + NotifVidName)
                    PBPipe(NTT='Someone tipped your video', Message=Message, URL=NotifVidURL)

                    notif = notif - 1
                    NotifRead(ID=NotifID)
                else:
                    print ("ERROR - Tell TheLazyHatGuy he needs to add this Notification Type:",NotifType)
                    print ("Also send him your notif.txt file")
                    notif = notif -1
            elif notif < 0:
                print ("That's all folks")
                return
            else:
                print ("ERROR - Contact TheLazyHatGuy because something f***ed up")
                sys.exit(-1)
                return
    return
