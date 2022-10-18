#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import platform

PATH = 'content'

# limit of article summary (words)

SUMMARY_MAX_LENGTH = 100
SUMMARY_END_SUFFIX = '…'

# this will force articles with future dates to be set to draft
WITH_FUTURE_DATES = False

# set this to False if problems rebuilding. Should speed up rebuild
CACHE_CONTENT = True
CACHE_PATH = 'cache'

# if false, do not load unmodified content from caches (i.e. don't use cache?)
LOAD_CONTENT_CACHE = True

# don't change this (see docs)
RELATIVE_URLS = True

# these are directories where pelican does not do any processing!
STATIC_PATHS = [
    'images' ,'extra',  'static', 'pages']
    
DISPLAY_PAGES_ON_MENU = True

STATIC_CREATE_LINKS = True

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'custom.css'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},  # and this
    'extra/CNAME': {'path': 'CNAME'},
    'extra/LICENSE': {'path': 'LICENSE'},
    'extra/README': {'path': 'README'},
}

THEME = 'notmyidea'
# THEME = 'themes/Flex'
# THEME = 'themes/notmyidea-tld'

AUTHOR = 'steve'
SITENAME = 'Shouting into the void'
SITESUBTITLE = 'My daily rant'
# SITEURL = 'https://stevehemingway.github.io'
# SITEURL = 'https://www.stevehemingway.com'
SITEURL = 'http://localhost:8001'
SUMMARY_MAX_LENGTH = 50
#SLUGIFY_SOURCE = 'basename' # alternative is 'title'. 'basename' uses filename.
SLUGIFY_SOURCE = 'title'
CACHE_CONTENT = True
OUTPUT_PATH = 'output/'
YEAR_ARCHIVE_URL = ''
# PAGINATION_PATTERNS = '{you have to put some regexp here}' # see https://docs.getpelican.com/en/stable/settings.html
# GITHUB_URL = 'https://github.com/stevehemingway/stevehemingway.github.io'
FILENAME_METADATA = '(?P<title>.*)'
DEFAULT_DATE = 'fs'
DEFAULT_CATEGORY = 'markets'
USE_FOLDER_AS_CATEGORY = False

# inserted in hope that this will get rid of pickle error (see https://github.com/getpelican/pelican/issues/2400)
CACHE_CONTENT = True
LOAD_CONTENT_CACHE = False

TIMEZONE = 'Europe/London'

# Feed generation is usually not desired when developing

FEED_ATOM = 'feeds/atom.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml' # i.e. generate a feed for all languages
CATEGORY_FEED_ATOM = None # i.e. don't create an atom feed for categories.
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll

# reduce link leakage
LINKS = (
    # ('Rudy Havenstein', 'https://rudy.substack.com/'),
    # ('Wall Street on Parade', 'https://wallstreetonparade.com'),
    ('Search this blog', 'https://cse.google.com/cse?cx=ce104668e88a754c6'),
    # ('My Mailing List', 'https://adept-originator-3889.ck.page/f39ac1a146'),
    # eventually get something set up.
    )
# LINKS = ()

Old_LINKS = (
    ('Epsilon Theory', 'https://www.epsilontheory.com'),
    ('Commodity.com LLC', 'https://commodity.com/'),
    ('Epsilon Theory', 'https://www.epsilontheory.com'),
    ('The Felder Report', 'https://thefelderreport.com/'),
    ('Credit Writedowns', 'https://pro.creditwritedowns.com/'),
	('Market Crumbs', 'https://www.marketcrumbs.com/'),
	('KoyFin', 'https://www.koyfin.com/home'),
	('The Market Huddle', 'https://markethuddle.com/'),
	('Matt Taibbi', 'https://taibbi.substack.com/'),
	('Beyond Overton', 'https://beyondoverton.com'), 
	('Wolf Richer', 'https://wolfstreet.com'), 
	('CalculatedRISK', 'https://www.calculatedriskblog.com/'), 
	('Adventures in Capitalism', 'https://adventuresincapitalism.com/'), 
	('Billion Prices Project', 'http://www.thebillionpricesproject.com/'), 
	('Shadow Stats', 'http://www.shadowstats.com/'), 
	('The Convexity Maven', 'https://www.convexitymaven.com/'), 
	('The Market Ear', 'https://themarketear.com/'),
    ('The Daily Shot', 'https://dailyshotbrief.com'),
    ('The Burning Platform Blog', 'https://www.theburningplatform.com'),
    )


# Social widget
SOCIAL = (('email', 'mailto:steve@acksam.com'),
# ('goodreads', 'https://www.goodreads.com/user/show/30000791-stephen-hemingway'),
  ('twitter', 'https://twitter.com/s_hemingway_'),
  ('reddit', 'https://www.reddit.com/r/stevehemingway/'),
  )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

FEED_ALL_RSS = 'feeds/all.rss.xml'
RSS_FEED_SUMMARY_ONLY = False # put the full post, not a summary, in the RSS feed

# typographical improvements!
# you need to install typogrify as a python library (via pip) if you use this.
# you  pelican via pipx (i.e. in virt. env.) but you can't seem to install typogrify inside it.
# installed
TYPOGRIFY = True
SEARCH_BOX = False
TYPOGRIFY_DASHES = 'default'

# sitemap plugin. Needs to work on different OSes

# if (platform.system() == 'Linux'):
	# PLUGIN_PATHS = ["/home/steve/pelican-plugins/",]	
# else:
PLUGIN_PATHS = ["plugins/",'/pelican-plugins']
	
# PLUGINS= ["sitemap",  "readtime", "pelican.plugins.neighbors",  "pelican.plugins.read_more",  "disqus_static", "summary"]
# PLUGINS=["sitemap",  "readtime", "md-metayaml"]
PLUGINS=None

# get rid of tags, because you're too lazy to use them.
#DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', ]
DIRECT_TEMPLATES = ['index',  'categories', 'authors', 'archives', ]

SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "daily"
    }
}

DISQUS_SITENAME = 'stevehem'

DISQUS_SECRET_KEY = 'Ce1OrlwiUJv3UTMIqgX1N9Ejip39vj1espJVz7n4O4yOgUzTZ0GLwNMXdKDqDn7h'

DISQUS_PUBLIC_KEY = 'rOVpMACbjA97SPJiAzGktAByWPRYifNtZT7DMyxNnfBYHVqhL6n3DjYOqqEEpoxx'
