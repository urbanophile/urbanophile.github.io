#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

########## IMPORTANT ###########################
# some settings are only for local development #
################################################

# #### Basic settings ####
AUTHOR = "Matt Gibson"
SITENAME = "Matt Gibson"
SITESUBTITLE = "Artisanal Data and Software Gibbon"

# configure automatically if using githubpages + custom domain
SITEURL = ""


# #### Menu settings ####
MENUITEMS = [
    ("About", "/about.html"),
    ("CV", "/cv.html"),
    ("Blog", "/blog/index.html"),
]
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False


# ▼▼▼▼▼▼▼▼▼▼ OVERWRITTEN in publishconf.py ▼▼▼▼
DEBUG = True
RELATIVE_URLS = True
# ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲


LOAD_CONTENT_CACHE = False
DELETE_OUTPUT_DIRECTORY = True


# #### Path / URL config  ####
PATH = "content"  # where the source content is located
PAGE_PATHS = ["pages"]  # pages are standalone html
ARTICLES_PATH = ["blog"]  # articles are arranged chronologically

# where the output is saved
ARTICLE_URL = "blog/{slug}.html"
ARTICLE_SAVE_AS = "blog/{slug}.html"
INDEX_SAVE_AS = "blog/index.html"

# #### Metadata ####
DEFAULT_LANG = "en"
DEFAULT_DATE_FORMAT = "%Y %B %d"
TIMEZONE = "Australia/Sydney"

# #### Static Assets ####
STATIC_PATHS = ["images", "extra/robots.txt"]
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/favicon.ico": {"path": "favicon.ico"},
}

CATEGORIES_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
TAG_SAVE_AS = ""
TAGS_SAVE_AS = ""

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
SUMMARY_MAX_LENGTH = 40
SUMMARY_END_SUFFIX = "…"


# #### Theme settings ####
THEME = "themes/my-basic"

# ##################
# #### Plugins  ####
# ##################

# #### Plugins - Markdown ####
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {
            "marker": "[TableOfContents]",
            "title": "Table of Contents",
            "anchorlink": True,
            "permalink": True,
            "baselevel": 2,
        },
    },
    "output_format": "html5",
}

# MARKDOWN = {
#     "extension_configs": {
#         "markdown.extensions.toc": {
#             "marker": "[TableOfContents]",
#             "title": "Table of Contents",
#             "anchorlink": True,
#             "permalink": True,
#             "baselevel": 2,
#         }
#     }
# }

# #### Plugins - Typogrify ####
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
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}
