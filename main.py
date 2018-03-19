import praw  #import praw , make sure you do pip-install praw on your terminal
import config #Config , self explanatory , example below
import time #just time

def bot_login():
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "Bucket_Leo")
    print ("Logged In to Reddit successfully ! ")
    print ("20*'_'")

    return r
 
def run_bot(r):
    for comment in r.subreddit('csgo').comments(limit=100):
        if "hello" in comment.body:
            print ("The sentence which has: ", (len(comment.body)),"letters and the sentence :", comment.body,  "has been found!!")
            comment.reply("hello") #Reply with the term given
            print ("Successfully replied to it !" + comment.body)
            Savefile = open("redditcomments.txt" , "w") #Save to file
            Savefile.write(comment.body + comment.id) #Save to file
            Savefile.close() #Saving to file
            print ("Results successfully saved to file!") #Info

            

    time.sleep(3) #Sleepy Bot
 
r = bot_login()
run_bot(r)

#Made by the glorious Leo
