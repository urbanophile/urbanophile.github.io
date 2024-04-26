from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

# ?!?!!?
sys.path.append(os.curdir)
from pelicanconf import *

# !!!!!


SITEURL = "https://matthew-gibson.com"
RELATIVE_URLS = False
# DISPLAY_PAGES_ON_MENU = True

ANALYTICS = """<!-- Cloudflare Web Analytics -->
<script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{"token": "8ffcbdbd3968444b8a98497ce18aa242"}'></script>
<!-- End Cloudflare Web Analytics -->
"""
