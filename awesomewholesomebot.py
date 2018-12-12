import praw
import time
import config
import os
import requests

def login():
    r = praw.Reddit(username = config.username,
           password = config.password,
            client_id = config.client_id,
           client_secret = config.client_secret,
           user_agent = "A wholesome bot that hands out compliments and The Room Quotes!")
    return r
    

    
def runbot(r, commentslist):
    print "Looking for comments"

    
    for test in r.subreddit('awesomewholesomebot').comments(limit=75):
        if "sad" in test.body and test.id not in commentslist and not test.author == r.user.me():
            print "replying to comment id" + test.id
            test.reply("Oh no that's not good!\n\n Why not try [meditation?](https://www.youtube.com/watch?v=1UyJG2b8FMc) \n\n How about go for a jog? \n\n Or you can listen to some relaxing [music!](https://open.spotify.com/user/spotify/playlist/37i9dQZF1DWU0ScTcjJBdj)")
            commentslist.append(test.id)
            
            with open ("commentslist.txt", "a") as f:
                f.write(test.id + "\n")
        
        if "oh hi mark" in test.body and test.id not in commentslist and not test.author == r.user.me():
            print "replying to comment id" + test.id
            test.reply("oh hey johnny")
            commentslist.append(test.id)
            
            with open ("commentslist.txt", "a") as f:
                f.write(test.id + "\n")
                
        if "!music" in test.body and test.id not in commentslist and not test.author == r.user.me():
            print "replying to comment id" + test.id
            test.reply("Check out this [spotify playlist](https://open.spotify.com/user/spotify/playlist/37i9dQZF1DWU0ScTcjJBdj) for some calming music!")
            commentslist.append(test.id)
            
            with open ("commentslist.txt", "a") as f:
                f.write(test.id + "\n")
                
        if "!quote" in test.body and test.id not in commentslist and not test.author == r.user.me():
            print "replying to comment id" + test.id        
            test.reply(">The glow of one warm thought is to me worth more than money - Thomas Jefferson")
            
            commentslist.append(test.id)
            
            with open ("commentslist.txt", "a") as f:
                f.write(test.id + "\n")
                
        if "!joke" in test.body and test.id not in commentslist and not test.author == r.user.me():
            print "replying to comment id" + test.id        
            test.reply(">What did one wall say to the other wall? We'll meet at the corner.")
            
            commentslist.append(test.id)
            
            with open ("commentslist.txt", "a") as f:
                f.write(test.id + "\n")
                
        if "great day" in test.body and test.id not in commentslist and not test.author == r.user.me():
            print "replying to comment id" + test.id
            test.reply("That is great to hear! Stay awesome!")
            commentslist.append(test.id)
            
            with open ("commentslist.txt", "a") as f:
                f.write(test.id + "\n")
                
        if "bad day" in test.body and test.id not in commentslist and not test.author == r.user.me():
            print "replying to comment id" + test.id
            test.reply("Aww man! That's not good. Here's a picture of a [cute dog](https://i.redd.it/dx894sord3w01.jpg)")
            commentslist.append(test.id)
            
            with open ("commentslist.txt", "a") as f:
                f.write(test.id + "\n")
                
        if "depressed" in test.body and test.id not in commentslist and not test.author == r.user.me():
            print "replying to comment id" + test.id
            test.reply("Oh no that's not good!\n\n Maybe you can talk to someone on [7cups.](https://www.7cups.com/)")
            commentslist.append(test.id)
            
            with open ("commentslist.txt", "a") as f:
                f.write(test.id + "\n")
            
        if "happy" in test.body and test.id not in commentslist and not test.author == r.user.me():
            print "replying to comment id" + test.id
            test.reply("Oh boy! That is so great to hear! Keep being awesome!!!!!")
            commentslist.append(test.id)
            
            with open ("commentslist.txt", "a") as f:
                f.write(test.id + "\n")
            
        if "suicidal" in test.body and test.id not in commentslist and not test.author == r.user.me():
            print "replying to comment id" + test.id
            test.reply("That's not good. \n\n Remember, you are worth it. Here are some resources. \n\n [USA Suicide Prevention Lifeline 1-800-273-8255](https://suicidepreventionlifeline.org) \n\n Canada, 211")
            commentslist.append(test.id)
            
            with open ("commentslist.txt", "a") as f:
                f.write(test.id + "\n")
            
        if "bad day" in test.body and test.id not in commentslist and not test.author == r.user.me():
            print "replying to comment id" + test.id
            test.reply("Aww man! That's not good. Here's a picture of a [cute dog](https://i.redd.it/dx894sord3w01.jpg)")
            commentslist.append(test.id)
            
            with open ("commentslist.txt", "a") as f:
                f.write(test.id + "\n")
            
        if "good bot" in test.body and test.id not in commentslist and not test.author == r.user.me():
            print "replying to comment id" + test.id
            test.reply("Thank you!!! I hope you have an amazing day!!!")
            commentslist.append(test.id)
            
            
            with open ("commentslist.txt", "a") as f:
                f.write(test.id + "\n")
                
        if "bad bot" in test.body and test.id not in commentslist and not test.author == r.user.me():
            print "replying to comment id" + test.id
            test.reply("Oh no!!! It's okay, you are entitled to your opinion. I hope you have a nice day!")
            commentslist.append(test.id)
            
            with open ("commentslist.txt", "a") as f:
                f.write(test.id + "\n")
                
        if "that's gay" in test.body and test.id not in commentslist and not test.author == r.user.me():
            print "replying to comment id" + test.id
            test.reply("Hey. Don't say that, that is a derogatory term against the LGBTQ+ community. Why not try a better word?")
            commentslist.append(test.id)
            
        if "!LGBTSupport" in test.body and test.id not in commentslist and not test.author == r.user.me():
            print "replying to comment id" + test.id
            test.reply("Here are some LGBT support platforms \n Youthline 1-800-268-9688 \n Reddit general support group /r/LGBT \n For the youth! /r/LGBTeens")
            commentslist.append(test.id)
            
            with open ("commentslist.txt", "a") as f:
                f.write(test.id + "\n")
            
    print "Sleeping for 2 seconds"    
    time.sleep(2)    

    
def savedcomments():
        if not os.path.isfile("commentslist.txt"):
            commentslist = []
        else:
           with open("commentslist.txt", "r") as f:
                commentslist = f.read()
                commentslist = commentslist.split("\n")
                commentslist = filter(None, commentslist)
    
        return commentslist
    
r = login()
commentslist   = []
while True: 
    runbot(r, commentslist)
    
print commentslist
