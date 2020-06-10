#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

STATIC_PATHS = [
    'images',
    'extra',  # this
]

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'custom.css'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},  # and this
    'extra/CNAME': {'path': 'CNAME'},
    'extra/LICENSE': {'path': 'LICENSE'},
    'extra/README': {'path': 'README'},
}

AUTHOR = 'me'
SITENAME = 'Monologue Blog'
SITESUBTITLE = 'politics, economics, maths, markets, Knebworth ...'
# SITEURL = 'https://stevehemingway.github.io'
SITEURL = 'https://www.stevehemingway.com'
SUMMARY_MAX_LENGTH = 50
#SLUGIFY_SOURCE = 'basename' # alternative is 'title'. 'basename' uses filename.
SLUGIFY_SOURCE = 'title'
CACHE_CONTENT = False
OUTPUT_PATH = 'output/'
YEAR_ARCHIVE_URL = ''
# PAGINATION_PATTERNS = '{you have to put some regexp here}' # see https://docs.getpelican.com/en/stable/settings.html
# GITHUB_URL = 'https://github.com/stevehemingway/stevehemingway.github.io'
FILENAME_METADATA = '(?P<title>.*)'
DEFAULT_DATE = 'fs'
USE_FOLDER_AS_CATEGORY = False

# add search (see https://snipcart.com/blog/pelican-blog-tutorial-search-comments)
# PLUGINS = ['tipue_search.tipue_search']
# this doesn't work: you have to use a theme that supports this type of search


# inserted in hope that this will get rid of pickle error (see https://github.com/getpelican/pelican/issues/2400)
CACHE_CONTENT = False
LOAD_CONTENT_CACHE = False

PATH = 'content'

TIMEZONE = 'Europe/London'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Epsilon Theory', 'https://www.epsilontheory.com'),
          ('The Felder Report', 'https://thefelderreport.com/'),
          ('Wall Street on Parade', 'https://wallstreetonparade.com'),
          ('Credit Writedowns', 'https://pro.creditwritedowns.com/'),
	('Market Crumbs', 'https://www.marketcrumbs.com/'),
	('KoyFin', 'https://www.koyfin.com/home'),
	('The Market Ear', 'https://themarketear.com/'),)


# Social widget
SOCIAL = (('email', 'steve@stevehemingway.com'),
	('goodreads', 'https://www.goodreads.com/user/show/30000791-stephen-hemingway'),
           ('twitter', 'https://twitter.com/steveknebworth'),)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

FEED_ALL_RSS = 'feeds/all.rss.xml'

# typographical improvements!

TYPOGRIFY = True

# sitemap - may work only on wymondley
PLUGIN_PATHS = ["C:/users/steve/pelican-plugins/",]
PLUGINS=["sitemap",]

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
        "pages": "monthly"
    }
}
