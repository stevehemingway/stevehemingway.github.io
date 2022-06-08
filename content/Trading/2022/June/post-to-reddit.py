#!/usr/bin/python

import praw
import datetime
from datetime import datetime, timedelta
import sys
import frontmatter
import re
from io import StringIO
from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()
    def handle_data(self, d):
        self.text.write(d)
    def get_data(self):
        return self.text.getvalue()

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()



test = False

subreddit_name = "stevehemingway"

# dt = datetime.datetime.now() #+ datetime.timedelta(days=1)

# ds = dt.strftime("%B %d, %Y")

r = praw.Reddit(
    site_name='steve',        # this links to a section in praw.ini
    user_agent="Steve\s test bot",)


def post_blog(fname):

    body = ''
    title = ''

    print("posting from {}".format(fname))

    with  open(fname,'r') as f:
        linecount = 1
        while True:
            print("line {}: ".format(linecount), end='')
            linecount += 1
            x = f.readline()
        
            print(x)
            if re.search("\A\s*\Z", x):       # empty string is false
                break
            y = re.search("\Atitle:.*", x)
            if y:
                title = y.group()
                title = re.sub("\Atitle:", '', title)
                print("found title: {}".format(title))
            
        body = f.read()

    # print("body: {}".format(body))

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
        submission = subreddit.submit(title, selftext=strip_tags(body)) 
        print(submission)
    # end post_blog


if len(sys.argv) > 1:
    for i in sys.argv[1:]:
        post_blog(i)
else:
    fname = "{}.md".format(datetime.today().strftime('%Y-%m-%d'))
    post_blog(fname)
