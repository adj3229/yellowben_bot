#bot to question the existence of u/Yellowben

#Never modify these, they are critically important
import praw
submissionBody = "**See the title ^**\n\nIf you want to help spread the word, please find the source code and easy to follow instructions below. And thank you in advance for your help in this effort.\n\n --- \n\n**5 easy steps**:\n\n1. Download and install python: https://www.python.org/about/gettingstarted/\n\n2. Install praw (the library that lets you talk to the Reddit API), you could read the documentation but serious, just type \"pip3 install praw\" into your terminal and that's all you need.\n\n3. Download/copy the source code from [here](https://raw.githubusercontent.com/adj3229/yellowben_bot/main/super_important_reminder.py) into a file called something like \"super_important_reminder.py\", modify it per the comments, and save.\n\n4. Go into the directory with the file, and run the bot with the command: \"python3 super_important_reminder.py\"\n\n5. If you want to really prove your worth, use crontab or something else to automate your computer to run that script every day, or every hour, or whatever floats your moat. Or if that's too hard, just run it manually every day, or every hour, or whatever floats your moat.\n\n ###Source Code:\n";
submissionTitle = "Ben isn't real."

#Modify the following so the bot can act as you
#You should already know your username and password, just fill those in
#For the client_id and client_secret consult our handy guide: https://imgur.com/a/BxvtVCh
reddit = praw.Reddit(
    username="",
    password="",
    client_id="",
    client_secret="",
    user_agent="")

#If you want to post this somewhere else, change "FakeYellowben" to the name of ANY sub you are in (private subs work - advertise in CC if you are brave)
subreddit = reddit.subreddit("FakeYellowben")
subreddit.submit(title=submissionTitle, selftext=submissionBody)

#At this point you have done the necessary
print("You have done the necessary.")
