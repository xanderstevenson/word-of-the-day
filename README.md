WORD OF THE DAY BOT

Anyone can join the Word of the Day by going here --> webexteams://im?space=82b37a80-98ac-11ec-86e2-5bbd30807931


## Write code that does stuff to a Webex space / room

I prefer using Adaptive Cards when posting to Webex spaces. If you're starting from scratch, you'll definitely need the [Buttons and Cards Designer](https://developer.webex.com/buttons-and-cards-designer) found on Webex for Developers. Play around with it using 'Preview mode' until it looks right and then copy the code with 'Copy card payload'. Save it somewhere.

Next we want to create a message to post in the Webex space that will contain the card we just created. You can test this out with the interactive [Create a Messag](https://developer.webex.com/docs/api/v1/messages/create-a-message) on the Webex for Developers page under the 'Try it' tab. Don't forget to paste you Adaptive Card code you saved into the 'attachments' field. Click 'Run' to create the message. When you get it working, click the 'Example' tab and copy the code. You will use this to build your request.

## Building the App in Python

I use Python and the requests library to do all the work for this app. You can see that the code is pretty simple -> https://github.com/xanderstevenson/word-of-the-day-bot/blob/main/chatops.py The main ingredient is the Adaptive Card we created, some if/else statements and a simple requests function for posting to a Webex room. I import 'return_word' function from a file in the same directory called 'terms'. This is also a Python module and basically picks a random entry from a list to post with the card to the Webex room each time the chatops.py module is run.

## Running the App from your Local Console (for debugging)

To run app from console make sure you're in the virtual environment venv and that the TEAMS_ACCESS_TOKEN environmental variable is available in the environment. You can check this with the command 'echo $TEAMS_ACCESS_TOKEN'. For me, I store that variable in he .bashrc file, so if nothing shows up, I use the command 'source ~/.bashrc' to load it. This time 'echo $TEAMS_ACCESS_TOKEN' will reveal the token. Okay, now I can run the command 'python chatops.py' or 'python3 chatops.py' to run the app locally (since the Python verrsion is 3.8.10). Everytime I run this command, a new random word of the day will appear in the Webex space. I only use this for testing purppses.

## Running the App on Schedule (Using GitHub Workflows and Actions)

In order to run the app on a schedule, we use GitHub workflows. In order to do that, you'll need to create a GitHub repo named '.github' and creat a directory in it called '.github/workflows'. So that structrure will look like this: '.github/.github/workflows/'. 

Next, you want to create a workflow file in the workslows directory. It will contain a name, a trigger, a job, and basic steps (including checkout and run). To learn more about what all this means, check out this tutorial: [How To Build Your First GitHub Actions Workflow](https://www.ipswitch.com/blog/how-to-build-your-first-github-actions-workflow). I also have a 'workflow templates' directory in the '.github' repo that contains the workslow as a template, as well as a properties.json file describing everything. 

This is what mine looks like --> https://github.com/xanderstevenson/.github/blob/default-branch/.github/workflows/wod-workflow.yml

One key component in my workflow is this line 'TEAMS_ACCESS_TOKEN: ${{ secrets.TEAMS_ACCESS_TOKEN }}'. I store that in the repo you're reading now under Settings -> Secrets -> Acions. 

Now we want to connect the Workflow we created with the repo and the code we want to run. In my word-of-the-day-bot GitHub repo, I click on the Actions tab and click on 'New workflow' and find my workflow listed amongst all the recommended and prebuilt workflows in a section titled 'By Alexander Stevenson'. If you've already done this, you can go back a step to Actions and click 'Select workflow' to pick the workflow you want.

If everything is setup correctly, the code will run completely and the Webex space will receive a new message. If not, you'll get an email to the address associated with your GitHub account. You can also click on the 'Actions' tab in your code repo and you'll see a detailed description of why your code failed.