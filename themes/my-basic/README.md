# About this theme

- index.html is mapped to blog/index.html
- index.md uses the homepage.html template and maps to the root index.html
- Not really a theme, just website structure. 

```
├── static
│   ├── css
│   └── images
└── templates
    ├── archives.html         // to display archives
    ├── article.html          // processed for each article
    ├── author.html           // processed for each author
    ├── authors.html          // must list all the authors
    ├── categories.html       // must list all the categories
    ├── category.html         // processed for each category
    ├── index.html            // the index (list all the articles)
    ├── page.html             // processed for each page
    ├── period_archives.html  // to display time-period archives
    ├── tag.html              // processed for each tag
    └── tags.html             // must list all the tags. Can be a tag cloud.
```
