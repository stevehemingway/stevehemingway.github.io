title: I'm back, sort of
date: 2020-05-04T15:58:44+01:00
category: misc
tags: 


# Background to this blog

I had a pile of markdown stuff from my time as a councillor, which was turned into a website
using the hpstr template for jekyll. TBH, I never really understood Jekyll, and I found hugo 
pretty difficult to use. I've been getting into Python more recently, and I wondered if
there was some sort of static site generator, written in Python, which had good support
for github pages (which is where I decided to host my site now I've retired my old 
cloud server I rented from digital ocean). Pelican seemed well liked, and I managed,
with the help of a lot of fairly hairy regexp conversions,
to turn my old Jekyll blog into a Pelican one. My first hit was [this one](https://opensource.com/article/19/5/run-your-blog-github-pages-python) by Erik O'Shaughnessy, who seems to be a cool dude. In fact, when you search for tutorials on Pelican, 
you'll get a bazillion hits, all of which are probably fine, but Erik's is the only one I've read.
He focusses on using Markdown, rather than RST, which seems to be the native markdown
language for Pelican. I don't know RST: I use Markdown for a lot of stuff, 
mainly because it seems to be so widely supported.

Pelican is very neat, because it automates (via a makefile) the uploading of the file to github pages. It's probably me, but whenever I try to use git to do anything which isn't totally 
bog standard I feel like an idiot. Fortunately, the makefile hides all that, and works fine
in Windows powershell.


## Update 7 Dec 2020

Well, I've used Pelican for six months. 
I have hit a few little niggles, and I haven't moved to a different template, even though this was one of the reasons I'd wanted to move to it for.
It has been better since I started using Zettlr (although I'm actually editing this in Vim, a workalike of the classic unix editor *vi*).





