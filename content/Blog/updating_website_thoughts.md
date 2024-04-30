Title: Updating and reflecting on my website 
Date: 2024-01-15
Authors: Matt Gibson
Modified: 2024-04-30

[TableOfContents]


It's been a little while since I've updated my website. Here's some quick thoughts revisiting this older code. 

# Pelican static website pros and cons 

Good:

* Pelican 👍: having software after not having used it for years is a welcome surprise. Especially given that I migrated from Python 2 to Python 3.
* static site generation 👍: Still handy. Handles a bunch of stuff website bureaucracy and whatnot I'd rather not be bothered with. 

Bad:

* random css 👎: I don't have a great sense of aesthetics so I've typically relied on someone elses'. In practice, that means copying other people's designs and CSS. That CSS, however, has aged poorly.
* using git submodules 👎: my setup for deploying this site was convoluted
* rst 👎: sorry,like mercurial ReStructured text just hasn't had community adoption.
* cli-only 👎: I would probably update my website more if it was easier. This was not helped by keeping content in a separate repo 


# Answers to some common Pelican questions 

[updated: 2024-04-30] Because Pelican is configured to deliver a quick, out of the box blogging experience the documentation is a little more obscure if you want to go off the beaten path. In 2024, Pelican is not as hot as it was in 2015 when I started this site but it there is still a lot of example code slowly rotting on github. Blessedly, Pelican has been fairly stable so much of the old content is handy.

Apologies if none of these responses answer your question. They are mostly for me, so I remember how to do basic things.

## How do I set my homepage as markdown document?

In brief, 

1. create a page `index.md` with the following metadata
```
Title: Welcome to my homepage
Save_as: index.html
Template: homepage.html

blah blah blah
```

2. (optional) create a template `homepage.html`. You can reference `dates` and `page.content` so you could like to recent blog posts say

```
{% extends "base.html" %}
{% block content %}
{% block content_title %}

{{ page.content }}

{% endblock %}
homepage.html
<dl>
{% for article in dates[:4] %}
    <dt>{{ article.locale_date }}</dt>
    <dd><a href="{{ SITEURL }}/{{ article.url }}">{{ article.title }}</a></dd>
{% endfor %}
</dl>

</article>
{% endblock content %}
```

3. modify `pelicanconf.py` with the following
```
ARTICLE_URL = "blog/{slug}.html"
ARTICLE_SAVE_AS = "blog/{slug}.html"
INDEX_SAVE_AS = "blog/index.html"

MENUITEMS = [
 ('home', '/'),
 ('blog', '/blog'),
]
```

[[src](https://stackoverflow.com/a/59508010/1888465)]

**Comment**: I think maybe you run into a problem here because you have a page but you want an article context. You have to also decide what to do with `index.html` and the blog focus part of the website. 

## How do I suppress the autogenerate category pages? 

In brief:

```
    CATEGORY_SAVE_AS = ""
    CATEGORIES_SAVE_AS = ""
```
similarly for tags:
```
    TAGS_SAVE_AS = ""
    TAG_SAVE_AS = ""
```

Note: you have to render pairs. It seems like just doing one or the other won't work. 
[src]()

another option is change 
```
 DIRECT_TEMPLATES = ['index', 'authors', 'categories', 'tags', 'archives']
```
to 
```
DIRECT_TEMPLATES = ['index', 'archives']
```
[src](https://docs.getpelican.com/en/stable/settings.html#template-pages)

**Comment**: Haven't tried working with `DIRECT_TEMPLATES`, need to look up how  this is used in the codebase. 

## How do I make templates/themes?

In brief, look at:

1. the [docs on themes](https://docs.getpelican.com/en/latest/themes.html) 
2. some examples:
    - the default theme, [simple](https://github.com/getpelican/pelican/tree/master/pelican/themes/simple/templates)
    - a more complex theme like [`flex`](https://github.com/alexandrevicenzi/Flex) or [`simplify`](https://github.com/vuquangtrong/simplify-theme)
    - config for an existing website e.g. for [simplify](https://github.com/vuquangtrong/simplify-theme/blob/master/build/pelicanconf.py)
3. it's also helpful to have high level understanding of the [pelican architecture](https://docs.getpelican.com/en/latest/report.html).

Consult these as required:

1. the jinja2 [template reference docs](https://jinja.palletsprojects.com/en/3.1.x/templates/) because it's mostly jinja2
2. the markup library reference docs, either the python [Markdown library](https://python-markdown.github.io/) (variously, python-markdown, markdown, or Markdown) or restructured text [docutils](https://docutils.sourceforge.io/). 

**Comment:** It's helpful to know that pelican outsources most of the heavy lifting to jinja2 and markup to the aforementioned libraries. Other libraries which do heavy lifting in pelican are pygments and feedgenerator.  I don't really know how the header level is passed into writer, `##` in the present document converts to `h3`.

## How do I render math in my markup? 

Not sure about the best way, but I am currently doing just doing 
```
python -m pip install pelican-render-math
```

and then you can just use pseudo-latex instructions in the text body:

```
this is an inline formula $\text{if } n=5 \text{ then } \operatorname {Aut}⁡( A_5 ) =  S_5$ and this is a display formula:
$$
{\displaystyle \langle s,t\mid s^{2},t^{3},(st)^{5}\rangle }
$$ 
```

this is an inline formula $\text{if } n=5 \text{ then } \operatorname {Aut}⁡( A_5 ) =  S_5$ and this is a display formula:
$$
{\displaystyle \langle s,t\mid s^{2},t^{3},(st)^{5}\rangle }
$$ 
[Link to the plugin here](https://github.com/pelican-plugins/render-math)

Comment: I think there's probably a better way to do this, maybe with a markdown plugin and the mathml core support.


## How do I link to internal content?

In brief:

```
[a link relative to content root]({filename}/this-is-the-source-file.md)
```
[[src](https://stackoverflow.com/questions/21867070/how-to-link-your-own-articles-on-a-pelican-blog)]

Comment: if you want to link to internal parts of the same page (i.e. send people to specific questions), this is not supported out of the box. With markdown you will need the the ToC extension [[src](https://github.com/getpelican/pelican/issues/1357)], so with markdown you will need to 
```
pip install markdown-toc --upgrade
```
and then slap 
```
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
```
into `pelicanconf.py` [[src](https://github.com/tohuw/pelicanmdoptionstest/blob/master/pelicanconf.py)].

Now you can link inside a document like so:
```
[TableOfContents]

# Pelican static website pros and cons

[reconsider pros and cons]({filename}/blog/updating_website_thoughts.md#pelican-static-website-pros-and-cons)
```
and maybe it's time to [reconsider pros and cons]({filename}/blog/updating_website_thoughts.md#pelican-static-website-pros-and-cons).

## How do I add images to my content? 

In brief:

```
![energy]({attach}images/energy.png)
```
[[src](https://stackoverflow.com/questions/35733496/how-do-i-attach-images-in-pelican)]

in generally static content can be linked with 
```
.. raw:: html

    <div id="demo"></div>
    <script src="{static}/js/demo.js"></script>

```
assuming it's in `content/static/js/demo.js`

## How do just make a static website?

In brief:

```
PATH_METADATA = '(?P<path_no_ext>.*?)([.-]\w\w)?\.[^.]+'
ARTICLE_TRANSLATION_ID = PAGE_TRANSLATION_ID = "path_no_ext"
```

but you probably also have to tinker with the jinja templates.  You may want to suppress the generation the author, tag, category html pages as well. Maybe you only want to use pages.

[[src](https://github.com/getpelican/pelican/issues/686)]


## How do I force a custom template?

In brief, if using Markdown put add the following metadata to my_page.md or my_article.md:
```
Save_as: index.html
Use_Template: homepage.html
```

## How do I get better SEO?

In brief, honestly I have no idea but Google says to [create helpful, reliable, people-first content.](https://developers.google.com/search/docs/fundamentals/creating-helpful-content). The basic theme does not have good descriptor metadata, Open Graph or  Rich Snippets support so if you like to waste a lot of time you can fiddle around with those. 
