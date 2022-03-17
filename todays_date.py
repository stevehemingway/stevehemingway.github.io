#!/usr/bin/env python

import os.path
from os import path
import os
from datetime import datetime, timedelta
import sys

months = ["Not a month","January","February","March"]

def main():

    today = datetime.today()
#    print("today: {}".format(today))
#    print(int(sys.argv[1]))
    if len(sys.argv) > 1:
        days_to_bump = int(sys.argv[1])
        today = today + timedelta(days_to_bump)
        print("bumped date {} days to {}".format(days_to_bump, today.date()))
#    print("today: {}".format(today))
    
    # bump to tomorrow if run with arg 1
    
    today_string = today.strftime('%Y-%m-%d')

    #print(months[today.month])
    # print (today_path)
    today_path = "content/Trading/{}/{}/{}.md".format(today.year, months[today.month],today_string)
    print(today_path)
    # print("{}.md".format(today_string))

    fname = today_path
    if path.exists(fname):
        print("File '{}' already exists".format(fname))
    else:                
        with open(fname, "wt") as f: 
                f.write("status: published\n")
                f.write( "date: "+ today_string+"\n")
                f.write("title: \n")
                f.write( "\n")
                f.write( "# " + today.strftime("%A %e, %B %Y\n") )

        print("created file '{}'".format(fname))
        print("Note: status set to 'published'")
        
    shortname = "today.md"

    try:
        os.unlink(shortname)
        os.link(fname, shortname)
    except FileExistsError:
        print("Can't link: file already exists")
    except: 
        print("some filesystem error")
        
    print("Created link to today's post as today.md")
    print("Hit <enter> to continue")
    input()

if __name__ == '__main__':
    main()
