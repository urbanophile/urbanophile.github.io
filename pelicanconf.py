#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

########## IMPORTANT #################
# this is only for local development #
######################################

# #### Basic settings ####
AUTHOR = "Matt Gibson"
SITENAME = "Matt Gibson"
SITESUBTITLE = "Artisanal Data and Software Gibbon"
# configure automatically if using githubpages + custom domain
# SITEURL = "https://matthew-gibson.com"
TIMEZONE = "Australia/Sydney"

# where the source is located
PATH = "content"


# ▼▼▼▼▼▼▼▼▼▼ OVERWRITTEN in publishconf.py ▼▼▼▼
RELATIVE_URLS = True
MENUITEMS = [
    ("About", "/"),
    # ("Projects", "/pages/projects.html"),
    ("CV", "/pages/CV.html"),
    ("Blog", "/category/blog.html")
    # ("Contact", "/pages/contact.html"),
]
# ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

DEFAULT_LANG = "en"
DEFAULT_DATE_FORMAT = "%Y %B %d"


# #### Static Assets ####
STATIC_PATHS = ["images", "extra/robots.txt", "extra/favicon.ico", "extra/CNAME"]
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/CNAME": {"path": "CNAME"},
}

# IGNORE_FILES = ["drafts/*"]

# #### URL settings ####
PATH_METADATA = "(?P<path_no_ext>.*)\..*"
ARTICLES_PATH = [
    "Blog",
]
ARTICLE_URL = ARTICLE_SAVE_AS = PAGE_URL = PAGE_SAVE_AS = "{path_no_ext}.html"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# DEFAULT_PAGINATION = 10


# #### Theme settings ####
# THEME = "notmyidea"
THEME = "themes/my-basic"
# USER_LOGO_URL = SITEURL + "/images/ok_photo.JPG"
# GOOGLE_ANALYTICS = "UA-36248181-1"
# TAGLINE = "Code monkey who enjoys accumulating technical knowledge."
