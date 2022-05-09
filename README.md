<h1 align="center">WORD OF THE DAY - Webex Space and Bot</h1>


<p align="center">Anyone with a Cisco domain account can join the Word of the Day by going here --> [JOIN - Word of the Day](https://eurl.io/#3wNrmU0-1)</p>


<h2 align="center" color"skyblue">Layout and Functionality</h2>

<p align="center">
<img src='https://github.com/xanderstevenson/word-of-the-day-bot/blob/main/media/WoD-screenshot-enhanced-labeled.png' width="375" height="437" border="10">
</p>

A card similar to the above is posted on a regular schedule to the 'Word of the Day' Webex room. A random word is chosen each time from hundreds of the most cutting-edge and interesting terms relevant to development, coding, networking, cloud computing and the sociology of technology. The word is in green font. A multi-word/sentence definition is provided below that. Below the definition is a button whith green font that is clickable and will take the user to the source and/or more information on the word of the day.


<h2 align="center">Write Code that Posts to a Webex Space / Room</h2>

<h3 align="center">Creat the Webex Room</h3>

Cick on the + sign at the top of Webex and select 'Create a Space'. Then name it and click 'Create'. Now the room is created and you should see it appear in the rooms column on the left of Webex. Now, we need the Room ID of the new room. We can get it by using the [Webex for Developers interactive Rooms API](https://developer.webex.com/docs/api/v1/rooms/list-rooms) call. Make sure you're logged in and select to use your personal access token. In the 'sortBy' field, type 'lastactivity'. Click the 'Run' button and a list of the most recent rooms you've interacted with should be returned. The room you just created will be on top. Save the id of the room. Later, we will use that as the value of our 'teams_room' variable. You can save the other values somewhere as well. It's good practice to keep notes when creating things; you never know when you'll need them.

<h3 align="center">Craft the Template of the Message to Be Posted to Your Webex Room</h3>

I prefer using Adaptive Cards when posting to Webex spaces. If you're starting from scratch, you'll definitely need the [Buttons and Cards Designer](https://developer.webex.com/buttons-and-cards-designer) found on Webex for Developers. Play around with it using 'Preview mode' until it looks right and then copy the code with 'Copy card payload'. Save it somewhere.

Next we want to create a message to post in the Webex space that will contain the card we just created. You can test this out with the interactive [Create a Message](https://developer.webex.com/docs/api/v1/messages/create-a-message) on the Webex for Developers page under the 'Try it' tab. Don't forget to paste you Adaptive Card code you saved into the 'attachments' field. Click 'Run' to create the message. When you get it working, click the 'Example' tab and copy the code. You will use this to build your request.

<h3 align="center">Building the App in Python</h3>

Okay, we have our Webex Room and the core of the message, based on the adaptive card. Now, let's write some Python code that will make everything come together and run. I use the Visual Studio Code IDE.

Create a virtual environment and start building your code inside of it. 

I use Python and the requests library to do all the work for this app. You can see that the code is pretty simple -> https://github.com/xanderstevenson/word-of-the-day-bot/blob/main/chatops.py The main ingredients are the adaptive card we created, some if/else statements and a simple requests function for posting to a Webex room. I import 'return_word' function from a file in the same directory called 'terms'. This is also a Python module and basically picks a random term from a list to post with the card to the Webex room each time the chatops.py module is run.

<h3 align="center">Create a Bot to Post the Message to the Webex Space</h3>

So far you have your Webex Room and you have Python code to post messages to your room. But who will post the messages. That's where the bot comes in.

Go to [Webex for Developers / My Apps](https://developer.webex.com/my-apps) and 'Create a New App' (You'll need to be logged in to do this). Choose 'Create a Bot'. Follow all the steps and create the bot. You'll then get a Bot Access Token. Save this as the TEAMS_ACCESS_TOKEN variable in the '~/.bashrc' file with the line export TEAMS_ACCESS_TOKEN="<Bot Access Token Goes Here>". Use the command 'source ~/.bashrc' to load the variable into the environment. You can check this worked with the command 'echo $TEAMS_ACCESS_TOKEN'. In my main module, chatops.py, you'll see the line 'access_token = os.environ.get("TEAMS_ACCESS_TOKEN"). This sets it up so the bot is the one doing the posting in the Webex space. Cool, right?

  <h2 align="center">Running the App from your Local Console (for debugging)</h2>

Now I can run the command 'python chatops.py' or 'python3 chatops.py' to run the app locally (since the Python verrsion is 3.8.10). Everytime I run this command, a new random word of the day will appear in the Webex space. I only use this for testing purppses.

  <h2 align="center">Running the App on Schedule (Using GitHub Workflows and Actions)</h2>

In order to run the app on a schedule, we use GitHub workflows. In order to do that, you'll need to create a GitHub repo named '.github' and creat a directory in it called '.github/workflows'. So that structrure will look like this: '.github/.github/workflows/'. 

Next, you want to create a workflow file in the workslows directory. It will contain a name, a trigger, a job, and basic steps (including checkout and run). To learn more about what all this means, check out this tutorial: [How To Build Your First GitHub Actions Workflow](https://www.ipswitch.com/blog/how-to-build-your-first-github-actions-workflow). I also have a 'workflow templates' directory in the '.github' repo that contains the workslow as a template, as well as a properties.json file describing everything. 

This is what mine looks like --> https://github.com/xanderstevenson/.github/blob/default-branch/.github/workflows/wod-workflow.yml

One key component in my workflow is this line 'TEAMS_ACCESS_TOKEN: ${{ secrets.TEAMS_ACCESS_TOKEN }}'. I store that in the repo you're reading now under Settings -> Secrets -> Actions. 

Now we want to connect the Workflow we created with the repo and the code we want to run. In my word-of-the-day-bot GitHub repo, I click on the Actions tab and click on 'New workflow' and find my workflow listed amongst all the recommended and prebuilt workflows in a section titled 'By Alexander Stevenson'. If you've already done this, you can go back a step to Actions and click 'Select workflow' to pick the workflow you want.

If everything is setup correctly, the code will run completely and the Webex space will receive a new message. If not, you'll get an email to the address associated with your GitHub account. You can also click on the 'Actions' tab in your code repo and you'll see a detailed description of why your code failed.

<h2 align="center">Other Considerations</h2.

I had created an empty __init__.py file in the root directory out of habit. Before Python 3.3 this was done to to make Python treat the directories as containing packages and facilitate importing between modules. From Python 3.3+ Implicit Namespace Packages are supported which allows the creation of a package without an __init__.py file. This however only applies to empty __init__.py files. So empty __init__.py files are no longer necessary and can be omitted.
