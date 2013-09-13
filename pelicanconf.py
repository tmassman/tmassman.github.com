#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Thomas Massmann'
SITENAME = u'it-spir.it'
SITEURL = 'http://it-spir.it'

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'de'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

GOOGLE_ANALYTICS = u'UA-3549237-1'

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Blogroll
LINKS =  (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
    ('You can modify those links in your config file', '#'),
)

TEMPLATE_PAGES = {
    'src/blog.html': 'blog/index.html',
    'src/imprint.html': 'impressum.html',
}

MENUITEMS = (
    # ('Home', '/'),
    # ('About Us', '/pages/about.html'),
    # ('Contact Us', '/pages/contact.html'),
    # ('Blog', '/blog'),
    ('Impressum', '/impressum.html'),
)

# Social widget
SOCIAL = (
    ('Twitter', 'https://twitter.com/it_spirit'),
    ('Coderwall', 'https://coderwall.com/tmassman'),
    ('Github', 'https://github.com/tmassman'),
    ('Bitbucket', 'https://bitbucket.org/it_spirit'),
    ('LinkedIn', 'http://www.linkedin.com/pub/thomas-massmann/20/393/259'),
)

DEFAULT_PAGINATION = 10
DISPLAY_CATEGORIES_ON_MENU = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

FILES_TO_COPY = (
    ('extra/CNAME', 'CNAME'),
)

THEME = '/Volumes/Work/Repositories/pelican-bootstrap3'

# GITHUB_USER = 'tmassman'
# GITHUB_SKIP_FORK = True
# GITHUB_SHOW_USER_LINK = True

BOOTSTRAP_THEME = ''

PLUGIN_PATH = '/Volumes/Work/Repositories/pelican-plugins'
PLUGINS = []
