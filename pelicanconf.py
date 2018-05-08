#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'The DIYnamics Team'
SITENAME = 'DIYnamics'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

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

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_PATHS = ['posts']
STATIC_PATHS = ['images', 'pdfs']

PAGE_ORDER_BY = 'page-order'

THEME = 'themes/pelican-alchemy/alchemy'

PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'liquid_tags.img',
    'liquid_tags.video',
    'liquid_tags.youtube',
           ]

DISPLAY_CATEGORIES_ON_MENU = False

SITEIMAGE = '/images/homepage_slideshow.gif'
