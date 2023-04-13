#!/usr/bin/env python

import os.path
from os import path
import os
from datetime import datetime, timedelta
import sys

months = ["Not a month","January","February","March", "April", "May", "June", "July"]

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
    todays_directory = "content/Trading/{}/{}/".format(today.year, months[today.month])
    todays_fname = "{}.md".format(today_string)
    today_path = todays_directory+todays_fname
    print(today_path)
    # print("{}.md".format(today_string))

    fname = today_path
    if path.exists(fname):
        print("File '{}' already exists. You can only post once per day.".format(fname))
    else:
        try:
            with open(fname, "wt") as f: 
                    f.write("status: published\n")
                    f.write( "date: "+ today_string+"\n")
                    f.write("title: \n")
                    f.write( "\n")
                    f.write( "# " + today.strftime("%A %e, %B %Y\n") )
        except FileNotFoundError:
            # probably path not found (new month)
            os.mkdir(todays_directory)
            print("created directory '{}': try again".format(todays_directory))
            

        print("created file '{}'".format(fname))
        print("Note: status set to 'published'")
        
    shortname = "today.md"
    short_dir_name = "today"
    try:
        os.unlink(shortname)
    except FileNotFoundError:
        print("you couldn't delete '{}' it because it was already gone".format(shortname))
    try:
        os.link(fname, shortname)
    except FileExistsError:
        print("Can't link: file already exists")
#    except: 
#        print("some filesystem error")

    # Create a link to this month's directory!
    try:
        os.unlink(short_dir_name)
    except FileNotFoundError:
        print("error ignored")

    # this is broken. The link is not to the right directory
    try:
        os.symlink(todays_directory, short_dir_name, target_is_directory=True) # kludge needed on Windows.
        print("linked {} as target to {} as symbolic link".format(todays_directory, short_dir_name))
    except FileExistsError:
        print("directory exists")
    # some other error will just crash prog.
        
    print("Created link to today's post as {}".format(shortname))
    print("Created link to this month's directory as {}".format(short_dir_name))
    print("Hit <enter> to continue")
    input()

if __name__ == '__main__':
    main()
