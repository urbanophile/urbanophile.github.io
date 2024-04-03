# Overview

This is contains the code I was using make my personal website hosted on github pages. It contains a lot cruft.

Look at this for info on 
  -  [configuring DNS for Github Pages](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)
  - the publishing workflow for [pelican with Github Actions](https://docs.getpelican.com/en/latest/tips.html#publishing-to-github-pages-using-a-custom-github-actions-workflow)

## Build dev site

Build using the dev settings with

```
pelican content -s pelicanconf.py
```

Serve the site locally with:

```
pelican --autoreload --listen
```

and navigate to [http://localhost:8000/](http://localhost:8000/)

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
