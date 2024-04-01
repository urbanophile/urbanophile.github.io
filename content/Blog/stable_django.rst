How good is Django?
####################

:date: 2024-03-31
:authors: Matt Gibson
:summary: A brief riff on stable, mature tools


I've been playing around recently with a little project involving recommender systems. Anyway, for the website, I ended up reaching for `Django <https://www.djangoproject.com/>`. Man, it's been over a year since I've done any Django projects, but I forgot how joy it is to use it. The documentation is excellent. The platform is pretty stable and very mature. There's a lot of useful packages and integrations: `DRF <https://github.com/encode/django-rest-framework>`, `Celery <https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html>`, the `debug toolbar <https://github.com/jazzband/django-debug-toolbar>`, `allauth <https://github.com/pennersr/django-allauth>`, `wagtail <https://github.com/wagtail/wagtail>` etc etc.   for It's just lovely, usable technology, and I feel old saying this, but I value that more and more. In my PhD, I had some unpleasant experiences with a rapidly changing landscape for software in AI and ML, and it made me value stability a whole lot more. Let us never talk about NVIDIA drivers on linux or nouveau. 

Another pleasant find was `dokuwiki <https://www.dokuwiki.org/dokuwiki>` which has been a breeze to setup and use. I tried several other wiki implementations for self-hosting on an raspberry pi v1 but they didn't measure up for a few reasons:

* `Wiki.js <https://js.wiki/>` (wants 2GB ram, complex node dependencies, needed constant internet connection and configured domain)
* `wikmd <https://github.com/Linbreux/wikmd>` (slow, didn't work out of the box)
* `wikidocs <https://www.wikidocs.it/>` (didn't work out of the box)
arms

It was eye opening how much harder it was making things work with 32-bit ARM11. I thought ARM support would be much better given the Apple chips. 

