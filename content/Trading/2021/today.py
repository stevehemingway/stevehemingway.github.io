
from datetime import datetime
today_string = datetime.today().strftime('%Y-%m-%d')
with open(today_string+".md", "wt") as f:
        f.write( "---\n")
        f.write("status: draft\n")
        f.write( "date: "+ today_string+"\n")
        f.write("title: \n")
        f.write( "---\n")
        f.write( "\n")
        f.write( "# " + datetime.today().strftime("%A %e, %B %Y\n") )

print("done")

