import requests
import json
import datetime as dt
import sys
import os
import getopt


# Simple Bot Function for passing messages to a room
def send_it(token, room_id, message):

        header = {"Authorization": "Bearer %s" % token,
                  "Content-Type": "application/json"}

        data = {"roomId": room_id,
                "text": message,
                "attachments": card}

        return requests.post("https://api.ciscospark.com/v1/messages/", headers=header, data=json.dumps(data), verify=True)


if __name__ == '__main__':

        # Command line arguments parsing    
        from argparse import ArgumentParser  
        #parser = ArgumentParser("chatops.py")  
        #parser.add_argument("-m", "--message", help="the message text to post to Webex Teams", required=True)
        #parser.add_argument("-r", "--room_id", help="the identifier of the room you added your bot to", required=True)
        #parser.add_argument("-t", "--token", help="[optional] your bot's access token. Alternatively, you can use the TEAMS_ACCESS_TOKEN env variable", required=False)
        #args = parser.parse_args() 
        access_token = os.environ.get("TEAMS_ACCESS_TOKEN")
        teams_room = "Y2lzY29zcGFyazovL3VzL1JPT00vODJiMzdhODAtOThhYy0xMWVjLTg2ZTItNWJiZDMwODA3OTMx"
        message = "testingdude"

         
        card =  [
        {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
                "type": "AdaptiveCard",
                "version": "1.2",
    "body": [
        {
            "type": "TextBlock",
            "text": "Word of the Day",
            "size": "Large",
            "separator": True,
            "horizontalAlignment": "Center",
            "fontType": "Default",
            "isSubtle": True,
            "color": "Accent",
            "weight": "Bolder",
            "wrap": True
        },

        {   "type": "Image",
                "url": "https://fcit.usf.edu/matrix/wp-content/uploads/2017/01/DanceBot-3-Sm.gif",
                "size": "small"
        }
    ],
    "actions": [
        {
            "type": "Action.OpenUrl",
            "url": "https://developer.cisco.com/",
            "title": "DevNet",
            "style": "positive",
            "alignment": "Center"
        }
    ]
        }
        }
        ]


        # Check access token
        teams_access_token = os.environ.get("TEAMS_ACCESS_TOKEN")
        token = access_token if access_token else teams_access_token
        if not token:
            error_message = "You must provide a Webex Teams API access token to " \
                            "interact with the Webex Teams APIs, either via " \
                            "a TEAMS_ACCESS_TOKEN environment variable " \
                            "or via the -t command line argument."
            print(error_message)
            sys.exit(2)

        # Now let's post our message to Webex Teams
        res = send_it(token, teams_room, message)
        if res.status_code == 200:
                print("your message was successfully posted to Webex Teams")
        else:
                print("failed with statusCode: %d" % res.status_code)
                if res.status_code == 404:
                        print ("please check the bot is in the room you're attempting to post to...")
                elif res.status_code == 400:
                        print ("please check the identifier of the room you're attempting to post to...")
                elif res.status_code == 401:
                        print ("please check if the access token is correct...")

