#!/usr/bin/env python

import os.path
from os import path
import os
from datetime import datetime

months = ["Not a month","January","February","March"]

today = datetime.today()

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
            f.write( "# " + datetime.today().strftime("%A %e, %B %Y\n") )

    print("created file '{}'".format(fname))
    print("Note: status set to 'published'")

try:
    os.link(fname, "today.md")
except FileExistsError:
    print("Can't link: file already exists")
print("Created link to today's post as today.md")
print("Hit <enter> to continue")
input()

