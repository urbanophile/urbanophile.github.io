# Overview

This is contains the code I was using make my personal website hosted on github pages. It contains a lot cruft.

## Setup repo

Current bizarre workflow is

```
git clone git@github.com:urbanophile/urbanophile.github.io.git
mv urbanophile.github.io output
```

## Build dev site

Build using the dev settings with

```
pelican content -s pelicanconf.py
```

Serve the site locally with:

```
pelican --autoreload --listen
```

and navigate to <http://localhost:8000/>

## Build prod site

Compile production site with

```
pelican content -s publishconf.py
```

then deploy new changes with

```
cd output
git add .
git commit -m "a change to my website"
git push origin master
```

output is a separate repo for website which is a git submodule. Also the theme is separate submodule, so don't forget to clone that.
