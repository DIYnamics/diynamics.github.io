#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'The DIYnamics Team'
SITENAME = 'DIYnamics'
SITEURL = ''
SITESUBTITLE = 'Affordable materials for geoscience teaching demonstrations'
SITEIMAGE = '/images/homepage_slideshow.gif'
DESCRIPTION = ('DIYnamics: affordable, accessible Earth science demonstration '
               'and teaching materials')
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'

GOOGLE_ANALYTICS = 'UA-146133798-1'

IGNORE_FILES = ['.#*', '__pycache__']

INDEX_SAVE_AS = '/pages/blog.html'

PATH = 'content'
ARTICLE_PATHS = ['blog']
PAGE_PATHS = ['pages', 'guides']
STATIC_PATHS = ['images', 'pdfs']

ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
DRAFT_URL = 'blog/drafts/{slug}.html'
DRAFT_SAVE_AS = 'blog/drafts/{slug}.html'
CATEGORY_URL = 'blog/category/{slug}.html'
CATEGORY_SAVE_AS = 'blog/category/{slug}.html'
TAG_URL = 'blog/tag/{slug}.html'
TAG_SAVE_AS = 'blog/tag/{slug}.html'
AUTHOR_URL = 'blog/author/{slug}.html'
AUTHOR_SAVE_AS = 'blog/author/{slug}.html'


ICONS = [
    ['twitter', 'https://twitter.com/DIYnamicsTeam'],
    ['youtube', 'https://www.youtube.com/channel/UCnUHxOSVY4G4OFbF8XL1qUg'],
    ['github', 'https://github.com/DIYnamics/diynamics.github.io']
]

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True
USE_FOLDER_AS_CATEGORY = True

# Slight hack to get pages ordered how we want them in the Header.  The LINKS
# setting is unique to the "alchemy" theme that we're using, and I've also
# modified the theme so that the items in it open in the same tab, not a new
# tab.
LINKS = [
    ['about', '/pages/about.html'],
    ['kits', '/pages/kits.html'],
    ['diyrotate', '/pages/diyrotate.html'],
    ['videos', 'https://www.youtube.com/channel/UCnUHxOSVY4G4OFbF8XL1qUg'],
    ['teaching', '/pages/teaching.html'],
    ['events', '/pages/events.html'],
    ['blog', '/pages/blog.html'],
    ['links', '/pages/links.html'],
    ['team', '/pages/people.html'],
    ['acknowledgments', '/pages/acknowledgments.html'],
]

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

CACHE_CONTENT = True
CACHE_PATH = 'cache'
LOAD_CONTENT_CACHE = True

DEFAULT_PAGINATION = False

THEME = 'themes/pelican-alchemy/alchemy'

PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'liquid_tags',
    'liquid_tags.img',
    'liquid_tags.video',
    'liquid_tags.youtube',
]
TYPOGRIFY = True

DISQUS_SITENAME = "diynamics"
TWITTER_USERNAME = "DIYnamicsTeam"
