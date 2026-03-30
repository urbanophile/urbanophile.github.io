# CLAUDE.md

## Project overview

Personal blog/portfolio static site built with [Pelican](https://getpelican.com/) and deployed to GitHub Pages at `https://matthew-gibson.com`.

## Build

```bash
pip install -r requirements.txt
pelican content              # development build (uses pelicanconf.py)
pelican content -s publishconf.py  # production build
```

Deployed automatically via GitHub Actions on push to `main` (see `.github/workflows/`).

## Content

- Blog posts: `content/Blog/*.md`
- Static pages: `content/pages/*.md`
- Images: `content/images/`

### Frontmatter conventions

Use `Authors:` (plural) not `Author:` — templates loop over `article.authors`.

```markdown
Title: My Post Title
Date: 2025-01-01
Authors: Matt Gibson
Tags: python, data
Summary: A 150–160 character description used as the meta description and in article listings.
```

`Summary` is required for a good meta description. Posts without it fall back to the first ~55 words of content, which may include image markdown.

## Theme

Custom Pelican theme at `themes/my-basic/` using Jinja2 templates.

- `base.html` — shared layout, `<head>`, nav, footer
- `article.html` / `page.html` / `homepage.html` — per-content-type overrides
- `index.html` — blog listing (inherited by `tag.html`, `category.html`, `author.html`)

## Plugins

Configured via namespace auto-discovery (no explicit `PLUGINS` list needed):

| Plugin | Purpose |
|--------|---------|
| `pelican-seo` | Open Graph tags, Twitter cards, SEO report |
| `pelican-sitemap` | Generates `sitemap.xml` |
| `pelican-render-math` | LaTeX math rendering |

## Config

| File | Used for |
|------|---------|
| `pelicanconf.py` | Development (relative URLs, no analytics) |
| `publishconf.py` | Production (sets `SITEURL`, Cloudflare analytics) |

Key settings in `pelicanconf.py`:
- `SUMMARY_MAX_LENGTH = 55` — words used for auto-generated summaries
- `SEO_ENHANCER_OPEN_GRAPH = True` / `SEO_ENHANCER_TWITTER_CARDS = True`
- `CURRENT_YEAR = date.today().year` — used in footer template
