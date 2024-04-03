#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

####### IMPORTANT ######
# this is only for local development


# #### Basic settings ####
AUTHOR = "Matt Gibson"
SITENAME = "Matt Gibson"
SITEURL = "http://www.matthew-gibson.com"
RELATIVE_URLS = True

PATH = "content"
PATH = "content"

TIMEZONE = "Australia/Sydney"
TIMEZONE = "Australia/Sydney"

DEFAULT_LANG = "en"
DEFAULT_LANG = "en"

DEFAULT_DATE_FORMAT = "%Y %B %d"
DEFAULT_DATE_FORMAT = "%Y %B %d"


# these features
# AUTHOR_SAVE_AS = False
# AUTHORS_SAVE_AS = False
# CATEGORY_SAVE_AS = False
# CATEGORIES_SAVE_AS = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# #### URL setttings ####
STATIC_PATHS = ["images", "extra/robots.txt", "extra/favicon.ico"]
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/favicon.ico": {"path": "favicon.ico"},
}
PATH_METADATA = "(?P<path_no_ext>.*)\..*"
ARTICLES_PATH = [
    "articles",
]
ARTICLE_URL = ARTICLE_SAVE_AS = PAGE_URL = PAGE_SAVE_AS = "{path_no_ext}.html"


# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         )

# Social widget
# SOCIAL = (
#     ("linkedin", "https://au.linkedin.com/in/mgibson1"),
#     ("github", "https://github.com/"),
# )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True


# #### Theme settings ####
THEME = "notmyidea"
# THEME = "themes/my-basic"
# USER_LOGO_URL = SITEURL + "/images/ok_photo.JPG"
# GOOGLE_ANALYTICS = "UA-36248181-1"
# TAGLINE = "Code monkey who enjoys accumulating technical knowledge."
