
from datetime import datetime
today_string = datetime.today().strftime('%Y-%m-%d')
with open(today_string+".md", "wt") as f:
        f.write( "---\n")
        f.write( "date: "+ today_string+"\n")
        f.write("title: \n")
        f.write( "---\n")
        f.write( "\n")

