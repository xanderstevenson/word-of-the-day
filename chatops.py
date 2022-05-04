
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
    access_token = os.environ.get("TEAMS_ACCESS_TOKEN")
    teams_room = "Y2lzY29zcGFyazovL3VzL1JPT00vODJiMzdhODAtOThhYy0xMWVjLTg2ZTItNWJiZDMwODA3OTMx"
    the_message = ""
    # fetch random dictionary containing word as key and definition as value
    random_word = return_word()
    random_word_name = random_word["name"]
    word = "\n" + random_word["name"] + "\n\n"
    word_url = random_word["url"]
    definition = random_word["definition"]
    wiki_link_text = f"Learn More about '{random_word_name}'"
    

    card = [
    {
    "contentType": "application/vnd.microsoft.card.adaptive",
    "content": {
            "type": "AdaptiveCard",
            "version": "1.2",
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
            "size": "ExtraLarge",
            "separator": True,
            "horizontalAlignment": "Center",
            "fontType": "Default",
            "isSubtle": True,
            "color": "Good",
            "weight": "Bolder",
            },
    # code block for definition
            {
            "type": "TextBlock",
            "text": definition,
            "size": "Medium",
            "horizontalAlignment": "Center",
            "fontType": "Default",
            "isSubtle": True,
            "wrap": True
            },
            {
            "type":"ActionSet",
            "horizontalAlignment": "Center",
            "actions": [
                {
                "type": "Action.OpenUrl",
                "url": word_url,
                "title": wiki_link_text,
                "style": "positive",
                "horizontalAlignment": "Center",
                }
            ]

            },

        # code block - use in a sentence
            {
            "type": "TextBlock",
            "text": f"Challenge: See how many times you can you incorporate '{random_word_name}' into your converstions today.",
            "size": "Small",
        #     "separator": True,
            "horizontalAlignment": "Center",
            "fontType": "Default",
            "isSubtle": True,
            "color": "Warning",
            "weight": "Lighter",
            "wrap": True
            },
    ],

        }
        }
        ]


        # Check access token
    teams_access_token = os.environ.get("TEAMS_ACCESS_TOKEN")

    # Now let's post our message to Webex Teams
    res = send_it(teams_access_token, teams_room, the_message)
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

