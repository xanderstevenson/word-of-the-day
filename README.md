# WORD OF THE DAY BOT

<p align="center">
<img src='https://github.com/xanderstevenson/word-of-the-day-bot/blob/main/media/WoD-screenshot-enhanced.png' width="614" height="715" border="10">
</p>


Anyone can join the Word of the Day by going here --> webexteams://im?space=82b37a80-98ac-11ec-86e2-5bbd30807931


## Write code that does stuff to a Webex space / room

I prefer using Adaptive Cards when posting to Webex spaces. If you're starting from scratch, you'll definitely need the [Buttons and Cards Designer](https://developer.webex.com/buttons-and-cards-designer) found on Webex for Developers. Play around with it using 'Preview mode' until it looks right and then copy the code with 'Copy card payload'. Save it somewhere.

Next we want to create a message to post in the Webex space that will contain the card we just created. You can test this out with the interactive [Create a Messag](https://developer.webex.com/docs/api/v1/messages/create-a-message) on the Webex for Developers page under the 'Try it' tab. Don't forget to paste you Adaptive Card code you saved into the 'attachments' field. Click 'Run' to create the message. When you get it working, click the 'Example' tab and copy the code. You will use this to build your request.

## Building the App in Python

Create a virtual environment and start building your code inside of it. 

I use Python and the requests library to do all the work for this app. You can see that the code is pretty simple -> https://github.com/xanderstevenson/word-of-the-day-bot/blob/main/chatops.py The main ingredient is the Adaptive Card we created, some if/else statements and a simple requests function for posting to a Webex room. I import 'return_word' function from a file in the same directory called 'terms'. This is also a Python module and basically picks a random entry from a list to post with the card to the Webex room each time the chatops.py module is run.

## Create a Bot to Post the Message to the Webex Space

Go to [Webex for Developers / My Apps](https://developer.webex.com/my-apps) and 'Create a New App' (You'll need to be logged in to do this). Choose 'Create a Bot'. Follow all the steps and create the bot. You'll then get a Bot Access Token. Save this as the TEAMS_ACCESS_TOKEN variable in the '~/.bashrc' file with the line export TEAMS_ACCESS_TOKEN="<Bot Access Token Goes Here>". Use the command 'source ~/.bashrc' to load the variable into the environment. You can check this worked with the command 'echo $TEAMS_ACCESS_TOKEN'. In my main module, chatops.py, you'll see the line 'access_token = os.environ.get("TEAMS_ACCESS_TOKEN"). This sets it up so the bot is the one doing the posting in the Webex space. Cool, right?

## Running the App from your Local Console (for debugging)

Now I can run the command 'python chatops.py' or 'python3 chatops.py' to run the app locally (since the Python verrsion is 3.8.10). Everytime I run this command, a new random word of the day will appear in the Webex space. I only use this for testing purppses.

## Running the App on Schedule (Using GitHub Workflows and Actions)

In order to run the app on a schedule, we use GitHub workflows. In order to do that, you'll need to create a GitHub repo named '.github' and creat a directory in it called '.github/workflows'. So that structrure will look like this: '.github/.github/workflows/'. 

Next, you want to create a workflow file in the workslows directory. It will contain a name, a trigger, a job, and basic steps (including checkout and run). To learn more about what all this means, check out this tutorial: [How To Build Your First GitHub Actions Workflow](https://www.ipswitch.com/blog/how-to-build-your-first-github-actions-workflow). I also have a 'workflow templates' directory in the '.github' repo that contains the workslow as a template, as well as a properties.json file describing everything. 

This is what mine looks like --> https://github.com/xanderstevenson/.github/blob/default-branch/.github/workflows/wod-workflow.yml

One key component in my workflow is this line 'TEAMS_ACCESS_TOKEN: ${{ secrets.TEAMS_ACCESS_TOKEN }}'. I store that in the repo you're reading now under Settings -> Secrets -> Actions. 

Now we want to connect the Workflow we created with the repo and the code we want to run. In my word-of-the-day-bot GitHub repo, I click on the Actions tab and click on 'New workflow' and find my workflow listed amongst all the recommended and prebuilt workflows in a section titled 'By Alexander Stevenson'. If you've already done this, you can go back a step to Actions and click 'Select workflow' to pick the workflow you want.

If everything is setup correctly, the code will run completely and the Webex space will receive a new message. If not, you'll get an email to the address associated with your GitHub account. You can also click on the 'Actions' tab in your code repo and you'll see a detailed description of why your code failed.

## Other Considerations

I had created an empty __init__.py file in the root directory out of habit. Before Python 3.3 this was done to to make Python treat the directories as containing packages and facilitate importing between modules. From Python 3.3+ Implicit Namespace Packages are supported which allows the creation of a package without an __init__.py file. This however only applies to empty __init__.py files. So empty __init__.py files are no longer necessary and can be omitted.
