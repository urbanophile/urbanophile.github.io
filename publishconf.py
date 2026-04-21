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

import urllib.request, json
try:
    with urllib.request.urlopen(
        "https://script.google.com/macros/s/AKfycbylMyfo6MCXTG0ULL6nctqCwmEWIx8MS4s3G0756_PH967xJShv_Nl2nz9PdaECPlA2yw/exec"
    ) as _r:
        SPAM_COUNT = json.loads(_r.read()).get("spam", 0)
except Exception:
    SPAM_COUNT = 0
RELATIVE_URLS = False
# DISPLAY_PAGES_ON_MENU = True

ANALYTICS = """<!-- Cloudflare Web Analytics -->
<script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{"token": "8ffcbdbd3968444b8a98497ce18aa242"}'></script>
<!-- End Cloudflare Web Analytics -->
"""
