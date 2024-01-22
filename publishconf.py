#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

# ?!?!!?
sys.path.append(os.curdir)
from pelicanconf import *

# !!!!!


# SITEURL = "https://matthew-gibson.com"
RELATIVE_URLS = False
MENUITEMS = [
    ("About", "https://matthew-gibson.com/"),
    # ("Projects", "/pages/projects.html"),
    ("CV", "https://matthew-gibson.com/pages/CV.html"),
    ("Blog", "https://matthew-gibson.com/category/blog.html")
    # ("Contact", "/pages/contact.html"),
]
