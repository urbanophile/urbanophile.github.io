# Overview

This is contains the code I was/am using make [my personal website](https://matthew-gibson.com) hosted on github pages. It contains a lot cruft.

Look at this for info on 
  -  [configuring DNS for Github Pages](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)
  - the publishing workflow for [pelican with Github Actions](https://docs.getpelican.com/en/latest/tips.html#publishing-to-github-pages-using-a-custom-github-actions-workflow)
  - using [github actions to deploy](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#publishing-with-a-custom-github-actions-workflow) the website (NB configure [custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site#configuring-a-subdomain) with the repo UI, not a CNAME file)
  - let cloudflare handle HTTPS and certificates (not github pages)
  - ~~remember the `CNAME` file in `content/extra/` and the CNAME config in `pelicanconf.py`. [Relevant pelican docs](https://docs.getpelican.com/en/latest/tips.html#copy-static-files-to-the-root-of-your-site).~~


helpful utilities:
  - [Squoosh app](https://squoosh.app/editor) to compress images

## Build dev site

Build using the dev settings and serve the site locally with:

```
pelican --autoreload --listen
```

and navigate to [http://localhost:8000/](http://localhost:8000/). If you just want to build the site use can use `pelican content -s publishconf.py`

## Build prod site

Compile production site with `pelican content -s publishconf.py`. I am currently deploying to github pages via a github action with [source code at `.github/workflows/pelican.yml`](https://github.com/urbanophile/urbanophile.github.io/blob/main/.github/workflows/pelican.yml)


## Blogs with source code using Pelican

using markdown 
- [Leonardo Giordani's blog](https://github.com/TheDigitalCatOnline/blog_source) (active as of 2024)
- [Full Stack Python site and blog](https://github.com/mattmakai/fullstackpython.com) (active as of 2021)
- [Kevin Yap](https://kevinyap.ca/) (active as of 2021)
- [This week in rust ](https://github.com/rust-lang/this-week-in-rust) (active as of 2024)


using rst:
  - [Ben Hoff's blog](https://github.com/benhoff/blog) (active as of 2019)
  - [Official Pelican blog](https://github.com/getpelican/pelican-blog) (active as of 2023)
