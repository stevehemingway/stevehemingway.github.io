+++
Tags = ["Development","golang"]
Description = ""
date = "2017-02-24T15:02:38Z"
title = "Update on Blog Setup"
menu = "main"


+++

Git submodules are still a bit of a mystery to me, but I yet again followed the instructions on [this page](https://gohugo.io/tutorials/github-pages-blog/) and this time it kind of worked.

It finally dawned on me that git push and pull link a local work tree to a remote repository. You can't run a web server on the remote machine, point it at the repository, and expect it to serve web pages, even though that's what the repository (possibly) contains. Git gurus, stop rolling your eyes!

You can't even checkout the repository on the local machine because then git push will complain that you're pushing to a master branch that it active and checked out on the remote machine. I discovered that the hard way. My web server does run a git server process. I tried it.

Anyway, after a bit of faffing around (!) I decided to edit the hugo source web file source on my local machine (running msys2 under Windows), push to github.com (because it is so awesome as a git server, and its free), then git pull the (built) website source from github to my web server directory on my dreamhost shared web server machine.

Now to add to my blog I create a markdown file, add it to the github pages repo, then git pull it to the dreamhost machine.

As a slight added complication, I run the DNS for this domain on another machine - a digital ocean dropbox, running mail-in-a-box. I discover I have to look in the dreamhost control panel DNS settings for the domain to see what IP address to use for the A record. I can't just use the main (arago) IP address. 

Who would have thought that something so simple could be so .... messy?
