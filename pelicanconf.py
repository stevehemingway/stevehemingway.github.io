#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'stevehemingway'
SITENAME = 'Steve Hemingway\'s Blog'
SITESUBTITLE = 'Knebworth musings'
# SITEURL = 'https://stevehemingway.github.io'
# SITEURL = 'https://www.stevehemingway.com'
SUMMARY_MAX_LENGTH = 50
SLUGIFY_SOURCE = 'basename' # alternative is 'title'. 'basename' uses filename.
CACHE_CONTENT = False
OUTPUT_PATH = 'output/'
STATIC_PATHS  = ['images']
YEAR_ARCHIVE_URL = ''
# PAGINATION_PATTERNS = '{you have to put some regexp here}' # see https://docs.getpelican.com/en/stable/settings.html
# GITHUB_URL = 'https://github.com/stevehemingway/stevehemingway.github.io'
FILENAME_METADATA = '(?P<title>.*)'
DEFAULT_DATE = 'fs'


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
