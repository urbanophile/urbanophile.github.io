# Overview

This is contains the code I was using make my personal website hosted on github pages. It contains a lot cruft.

Look at this for info on 
  -  [configuring DNS for Github Pages](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)
  - the publishing workflow for [pelican with Github Actions](https://docs.getpelican.com/en/latest/tips.html#publishing-to-github-pages-using-a-custom-github-actions-workflow)
  - [using github actions to deploy the website](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#publishing-with-a-custom-github-actions-workflow) (NB configure [custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site#configuring-a-subdomain) with the repo UI, not a CNAME file)
  - let cloudflare handle HTTPS and certificates (not github pages)
  - ~~remember the `CNAME` file in `content/extra/` and the CNAME config in `pelicanconf.py`. [Relevant pelican docs](https://docs.getpelican.com/en/latest/tips.html#copy-static-files-to-the-root-of-your-site).~~

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


## Blogs using Pelican

using markdown 
- https://github.com/TheDigitalCatOnline/blog_source
- https://github.com/mattmakai/fullstackpython.com
- https://kevinyap.ca/
- https://github.com/rust-lang/this-week-in-rust


using rst:
  - https://github.com/benhoff/blog
  - https://github.com/getpelican/pelican-blog
