#!/usr/bin/env python

import os.path
from os import path
from datetime import datetime

today_string = datetime.today().strftime('%Y-%m-%d')

fname = today_string+".md"
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

input()

