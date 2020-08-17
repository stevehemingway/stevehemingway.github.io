title: Text templating using Mustache on Windows
date: 2020-8-17
category: technical
tags: windows

# The problem

I want to generate a series of text files from a template.
I was thinking about using the C preprocessor, cpp.
The advantage is that I have used it for years, 
the disadvantage is that it is specifically written to pre-process C code and is not really general purpose.
An additional disadvantage is that it appears not to be available as a standalone executable on Windows.

Because of this, I decided to use [Mustache](https://mustache.github.io/mustache.1.html).
This uses YAML to represent the variable part (content?) and seems to be available everywhere.
After a few false starts trying to use a Python implementation, I settled on the Ruby one.
It's quite possible to install Ruby and gem on Windows. I think I used [this](https://stackoverflow.com/questions/21625582/is-there-a-standalone-portable-command-line-implementation-of-mustache-for-wind) to get going.
I had to update my Ruby install, as I know nothing about coding in the language and I just wanted a runnable version.

I like YAML, because it's such a lightweight syntax. It's used to create the various headers in Pelican, 
the processor that generates this very page. 

Templates are very powerful. It's a pity that they are not used more. My former colleague Ian Williamson did some wonderful stuff with them,
using a parser he crafted using AWK (I think). 

I got bogged down by the fact that my template had a pound sign in it (&pound;).
After *a lot* of experimenting, I discovered that the solution was to make the original template encoded as UTF-8-BOM (rather than UTF-8).
It's all to do with powershell having an inconsistent handling of encodings, I think,
but I really couldn't care less.

I don't know much about encodings, but I now now that BOM stands for Byte Order Mark. 
I think it's equivalent to the magic byte in unix that allows the file command to know what file type it's looking at.
Whatever it is, it fixes the problem nicely.
Random experimenting with lots of other encodings didn't work nearly so well.

Notepad++, which is an excellent editor, allows a file to be converted to a range of encodings at the click of a menu. 
It worked for me.

Happy Coding!

Steve.
