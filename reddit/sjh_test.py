#!/usr/bin/python
import praw
import datetime

test = False

subreddit_name = "stevehemingway"

#username = "stevehem"
#password = "BLejGjVAk6"

#client_id = 'nALuQXG4fh8ZxmRVhoyCoQ'
#client_secret = 'eso8S8-Ixogmm6pss7uAidrGc_n-Sw'


dt = datetime.datetime.now() #+ datetime.timedelta(days=1)

ds = dt.strftime("%B %d, %Y")

title = "Test post(" + ds + ") This text will appear somewhere"

r = praw.Reddit(
    site_name='steve',        # this links to a section in praw.ini
    user_agent="Steve\s test bot",)

##    client_id = client_id,
##    client_secret = client_secret,
##    username = username,
##    password = password)

# r.login(username,password)

# read lines from GNT file

f = open('body-text.txt','r')

body = f.read()
f.close()

subreddit = r.subreddit(subreddit_name)

# do post
if (test):
    print("TITLE:"+title + "\n\n")   
    print("BODY:"+body + "\n\n")
    print("readonly? {}".format(r.read_only))
    print("display name: {}".format(subreddit.display_name))
    print("subreddit title {}".format(subreddit.title))
    try: 
        print("subreddit descriptionL {}".format(subreddit.description))
    except:
        print("something bad happened")
        exit(False)
    else:
        print("desc. returned without errors")
else:
    submission = subreddit.submit(title, selftext=body) 
    print(submission)
