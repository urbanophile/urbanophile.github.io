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
SITEURL = ""

TIMEZONE = "Australia/Sydney"


# configured automatically if using githubpages + custom domain
SITEURL = "https://matthew-gibson.com"

MENUITEMS = [
    ("About", "/index.html"),
    ("CV", "/pages/CV.html"),
    ("Blog", "/category/blog.html"),
]
# ▼▼▼▼▼▼▼▼▼▼ OVERWRITTEN in publishconf.py ▼▼▼▼
DEBUG = True
RELATIVE_URLS = True
# ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲


LOAD_CONTENT_CACHE = False


DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# where the source content is located
PATH = "content"

# pages are standalone html
PAGE_PATHS = ["pages"]

# articles are arranged chronologically
ARTICLES_PATH = ["Blog"]

DEFAULT_LANG = "en"
DEFAULT_DATE_FORMAT = "%Y %B %d"


# #### Static Assets ####
STATIC_PATHS = ["images", "extra/robots.txt"]
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/favicon.ico": {"path": "favicon.ico"},
}


# #### URL settings ####

# should mirror filesystem hierarchy
# see: https://docs.getpelican.com/en/4.9.1/settings.html#url-settings
PATH_METADATA = "(?P<path_no_ext>.*)\..*"  # don't fix this syntax warning
ARTICLE_URL = ARTICLE_SAVE_AS = "{path_no_ext}.html"
PAGE_URL = PAGE_SAVE_AS = "{path_no_ext}.html"

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


TYPOGRIFY = True

# #### Plugins - SEO ####
# src: https://github.com/pelican-plugins/seo
# pelicanconf.py or publishconf.py
SEO_REPORT = True  # SEO report is enabled by default
SEO_ENHANCER = True  # SEO enhancer is disabled by default
SEO_ENHANCER_OPEN_GRAPH = True  # Subfeature of SEO enhancer
SEO_ENHANCER_TWITTER_CARDS = False  # Subfeature of SEO enhancer


# #### Plugins - Sitemap ####
SITEMAP = {
    "format": "txt",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}
