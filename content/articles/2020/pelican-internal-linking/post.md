Title: Pelican Internal Article Linking
Date: 2020-07-10 10:20
Modified: 2020-07-10 19:30
Category: Dev Resources
Tags: python, pelican
Slug: pelican-internal-linking
Author: Ben McNeill
Summary: Notes on internal article linking with pelican
cover_image: https://images.unsplash.com/photo-1507171700100-08e9a10401d9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1500&q=80
cover_image_by: Matteo Catanese
cover_image_link: https://unsplash.com/photos/BdPPwNzsa6o

<!-- {% img {static|/extra/cactus.jpg} 200 200 "Cactus" "Alt text" %} -->

When setting up this blog I had a heck of a time figuring out how to do linking between articles.  Turns out it is pretty easy.  The [pelican docs](https://docs.getpelican.com/en/3.5.0/content.html#linking-to-internal-content) show how this is possible.  The key is to use relative references back to the markdown file you are trying to link to.  When it crunches the output, it will be rendered correctly to the html.  

suppose your project is using the following directory structure
```bash
articles
    └── 2020
        ├── first-article
        │   ├── first_article.md
        │   ├── img
        │   │   ├── cactus1.jpg
        │   │   └── cactus2.jpg
        │   └── notebooks
        ├── git-submodules
        │   ├── img
        │   │   ├── cactus1.jpg
        │   │   └── cactus2.jpg
        │   ├── notebooks
        │   └── post.md
        ├── liquid-tags
        │   ├── img
        │   │   ├── cactus1.jpg
        │   │   └── cactus2.jpg
        │   ├── liquid-tags.md
        │   └── notebooks
        ├── pelican-autostatic
        │   ├── img
        │   │   ├── cactus1.jpg
        │   │   └── cactus2.jpg
        │   ├── notebooks
        │   └── post.md
        └── pelican-internal-linking
            ├── img
            │   ├── cactus1.jpg
            │   └── cactus2.jpg
            ├── notebooks
            └── post.md
```

If you want to link to the pelican-autostatic [article]({filename}../pelican-autostatic/post.md) from this article you would create the link like so.  

```Markdown
[pelican-autostatic]({filename}../pelican-autostatic/post.md) 
```

If this is still confusing, check out the raw markdown file for this post so you can see how it works.