
import json
import sys
import requests
import os
from terms import return_word


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
        message = ""
        # fetch random dictionary containing word as key and definition as value
        random_word = return_word()
        word = "\n" + random_word["name"] + "\n\n"
        definition = random_word["definition"]
        
        card =  [
        {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
                "type": "AdaptiveCard",
                "version": "1.2",
                # "backgroundImage": {
                #         "url": "https://st.depositphotos.com/1131998/1433/v/950/depositphotos_14331897-stock-illustration-gray-technology-background.jpg"
                # },
    "body": [
        {
            "type": "TextBlock",
            "text": "Word of the Day",
            "size": "ExtraLarge",
            "horizontalAlignment": "Center",
            "fontType": "Default",
            "isSubtle": True,
            "color": "Accent",
            "weight": "Bolder",
            "wrap": True,
            "style": "Emphasis"
        },
# code block for word
        {
            "type": "TextBlock",
            "text": word,
            "size": "Large",
            "separator": True,
            "horizontalAlignment": "Center",
            "fontType": "Default",
            "isSubtle": True,
            "color": "Good",
            "weight": "Bolder",
        #     "wrap": True
        },
# code block for definition
        {
            "type": "TextBlock",
            "text": definition,
            "size": "Medium",
        #     "separator": True,
            "horizontalAlignment": "Center",
            "fontType": "Default",
            "isSubtle": True,
        #     "color": "Accent",
        #     "weight": "Bolder",
            "wrap": True
        },
# code block - use in a sentence
        {
            "type": "TextBlock",
            "text": f"See how many times you can incorporate the word into your speech and text today.",
            "size": "Small",
        #     "separator": True,
            "horizontalAlignment": "Center",
            "fontType": "Default",
            "isSubtle": True,
            "color": "Warning",
            "weight": "Lighter",
            "wrap": True
        },


    {
            "type":"ActionSet",
    "horizontalAlignment": "Center",
    "actions": [
        {
        "type": "Action.OpenUrl",
        "url": "https://developer.cisco.com/site/support/",
        "title": "DevNet Developer Support",
        "style": "positive",
        "horizontalAlignment": "Center",
        # "iconUrl": "https://pubhub.devnetcloud.com/media/support/site/images/cwd.png"
        }
    ]

    }
        # {
        #     "type": "ImageSet",
        #     "images": [
        #         {
        #             "type": "Image",
        #             "url": "https://github.com/xanderstevenson/word-of-the-day-bot/blob/main/media/giphy.gif",
        #             "size": "Medium"
        #         }
        #     ]
        # }
    ],




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

