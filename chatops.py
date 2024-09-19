import re
import json
import requests
import os
from terms import return_word
from datetime import datetime
from passwords import profile_id, li_access_token, TEAMS_ACCESS_TOKEN


# Simple Bot Function for passing messages to a room
def send_it(token, room_id, message):

    header = {"Authorization": "Bearer %s" % token, "Content-Type": "application/json"}

    data = {"roomId": room_id, "text": message, "attachments": card}

    return requests.post(
        "https://api.ciscospark.com/v1/messages/",
        headers=header,
        data=json.dumps(data),
        verify=True,
    )


# post to LinkedIn
# will change to https://api.linkedin.com/rest/posts
def post(profile_id, li_access_token, random_word_name, definition, word_url):

    url = "https://api.linkedin.com/v2/ugcPosts"

    headers = {
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0",
        "Authorization": "Bearer " + li_access_token,
    }
    # make new variable for linkedin hashtag, lowercase it and remove spaces
    random_word_linkedin = random_word_name.lower().replace(" ", "")
    # remove abbreviations for linkedin hashtag
    # remove everything between ()
    random_word_linkedin = re.sub("\(.*?\)", "()", random_word_linkedin)
    # remove (), -.  and /
    random_word_linkedin = random_word_linkedin.replace("(", "").replace(")", "")
    random_word_linkedin = random_word_linkedin.replace("-", "").replace("/", "")
    random_word_linkedin = random_word_linkedin.replace(".", "")
    post_data = {
        "author": "urn:li:person:" + profile_id,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": f"----------------------\nTech Word of the Day\n----------------------\n\n{random_word_name}\n\n\n{definition}\n\n\nThis automated post was created by Alex Stevenson using #Python and a LinkedIn #API.\n\n#Tech #WordOfTheDay #{random_word_linkedin} #Automation #DevNet"
                },
                "shareMediaCategory": "NONE",
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"},
    }

    response = requests.post(url, headers=headers, json=post_data)
    return response


if __name__ == "__main__":

    # Command line arguments parsing
    from argparse import ArgumentParser

    teams_room = (
        "Y2lzY29zcGFyazovL3VzL1JPT00vODJiMzdhODAtOThhYy0xMWVjLTg2ZTItNWJiZDMwODA3OTMx"
    )
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
                        "horizontalAlignment": "center",
                        "fontType": "Default",
                        "isSubtle": True,
                        "color": "Accent",
                        "weight": "Bolder",
                        "wrap": True,
                        "style": "Emphasis",
                    },
                    # code block for word
                    {
                        "type": "TextBlock",
                        "text": word,
                        "size": "ExtraLarge",
                        "separator": True,
                        "horizontalAlignment": "center",
                        "fontType": "Default",
                        "isSubtle": True,
                        "color": "Good",
                        "weight": "Bolder",
                        "wrap": True,
                    },
                    # code block for definition
                    {
                        "type": "TextBlock",
                        "text": definition,
                        "size": "Medium",
                        "horizontalAlignment": "center",
                        "fontType": "Default",
                        "isSubtle": True,
                        "wrap": True,
                    },
                    {
                        "type": "ActionSet",
                        "horizontalAlignment": "center",
                        "actions": [
                            {
                                "type": "Action.OpenUrl",
                                "url": word_url,
                                "title": wiki_link_text,
                                "style": "positive",
                                "horizontalAlignment": "center",
                            }
                        ],
                    },
                    # # code block - use in a sentence
                    #     {
                    #     "type": "TextBlock",
                    #     "text": f"Challenge: See how many times you can you incorporate '{random_word_name}' into your converstions today.",
                    #     "size": "Small",
                    #     "horizontalAlignment": "left",
                    #     "fontType": "Default",
                    #     "isSubtle": True,
                    #     "color": "Warning",
                    #     "weight": "Lighter",
                    #     "wrap": True
                    #     },
                ],
            },
        }
    ]

    # Now let's post our message to Webex Teams
    res = send_it(TEAMS_ACCESS_TOKEN, teams_room, the_message)
    if res.status_code == 200:
        print(f"{word} was successfully posted to Webex Teams on {datetime.now()}")

    else:
        print("failed with statusCode: %d" % res.status_code)
        if res.status_code == 404:
            print("please check the bot is in the room you're attempting to post to...")
        elif res.status_code == 400:
            print(
                "please check the identifier of the room you're attempting to post to..."
            )
        elif res.status_code == 401:
            print("please check if the access token is correct...")

    # post to linkedin
    res2 = post(profile_id, li_access_token, random_word_name, definition, word_url)
    if res2.status_code == 201:
        print(f"{word} was successfully posted to LinkedIn")
    else:
        print("failed with statusCode: %d" % res2.status_code)
