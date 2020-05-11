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

AUTHOR = 'stevehemingway'
SITENAME = 'Steve Hemingway\'s Blog'
SITESUBTITLE = 'Knebworth musings'
# SITEURL = 'https://stevehemingway.github.io'
# SITEURL = 'https://www.stevehemingway.com'
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

# inserted in hope that this will get rid of pickle error (see https://github.com/getpelican/pelican/issues/2400)
#CACHE_CONTENT = False
#LOAD_CONTENT_CACHE = False


PATH = 'content'

TIMEZONE = 'Europe/London'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True


# typographical improvements!

TYPOGRIFY = True
