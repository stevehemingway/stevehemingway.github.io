title: How I set up this site
date: 2020-05-11 10:22
slug: pelican_notes

This is a note for me, to remember how to create a new entry.

I had to fiddle a bit with Pelican to make it work OK on Windows and
to allow me to use a custom domain on github. 
You can see the full gory details at https://github.com/stevehemingway/stevehemingway.github.io.

The things that kept tripping me up were as follows:

* @echo in a makefile in Windows fails. Everything else is fine, but echo fails, 
because it's not a proper command. This is all explained [here](https://stackoverflow.com/questions/20712307/echo-fails-in-make-on-windows).
The solution, as suggested, is to stick a ';' at the end of each echo line,
forcing it to be treated like a command. 
I actually use Pelican both on Windows and Linux systems, so I didn't want
to break portability (although I would gladly have done so if there wasn't an easy workaround).

* It's not sufficient to tell github, via the settings, that you want to use a custom domain.
You have to have a file called CNAME in the root of the project with the custom domain name.
You can read about this [here]( https://help.github.com/en/github/working-with-github-pages/managing-a-custom-domain-for-your-github-pages-site#configuring-a-subdomain).
The key sentence is 'If you use a static site generator to build your site locally and push the generated files to GitHub, pull the commit that added the CNAME file to your local repository. For more information, see "Troubleshooting custom domains and GitHub Pages."' 
The problem is that Pelican just trashes all the files and removes the CNAME file every time the site is generated. It took me a painfully long time to work out what was going wrong. The fix was to insert an extra line into the makefile:
publish:
````
        $(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)
        echo $(CUSTOM_DOMAIN_NAME) > $(OUTPUTDIR)/CNAME
````

That's quite enough tech stuff for today!
