<<<<<<< HEAD
#!/usr/bin/env python

=======
>>>>>>> 2fc4ef90c732e7cadb77e64fd705671114cbe3d1
import os.path
from os import path
from datetime import datetime

today_string = datetime.today().strftime('%Y-%m-%d')

fname = today_string+".md"
if path.exists(fname):
<<<<<<< HEAD
    print("File '{}' already exists".format(fname))
=======
    print("File {} already exists".format(fname))
>>>>>>> 2fc4ef90c732e7cadb77e64fd705671114cbe3d1
else:                
    with open(fname, "wt") as f: 
            f.write("status: published\n")
            f.write( "date: "+ today_string+"\n")
            f.write("title: \n")
            f.write( "\n")
            f.write( "# " + datetime.today().strftime("%A %e, %B %Y\n") )

    print("created file '{}'".format(fname))
    print("Note: status set to 'published'")

<<<<<<< HEAD
input()

=======
>>>>>>> 2fc4ef90c732e7cadb77e64fd705671114cbe3d1
