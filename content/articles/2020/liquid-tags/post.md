Title: Liquid Tags Pelican Plugin
Date: 2020-07-10 10:20
Modified: 2020-07-10 19:30
Category: Dev Resources
Tags: python, pelican, pelican-plugins
Slug: liquid-tags-pelican-plugin
Author: Ben McNeill
Summary: Notes on liquid tag plugin for pelican
cover_image: https://images.unsplash.com/photo-1534712980252-f433e30fa90b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1500&q=80
cover_image_by: Vansh Juneja
cover_image_link: https://unsplash.com/photos/RtPFXUabsBA

<!-- {% img {static|/extra/cactus.jpg} 200 200 "Cactus" "Alt text" %} -->

Pelican has some nice plugins.  The liquid tag plugin is no exception.   I found the [documentation](https://github.com/getpelican/pelican-plugins/tree/master/liquid_tags#image-tag) confusing for how to tag images so I wanted to find some examples instead.  Found a PR with some examples.

Liquid tags handle the formatting but we need a different plugin if we want to use relative references to our media.  I wrote some notes down about the plugin [pelican-autostatic]({filename}../pelican-autostatic/post.md) to accomplish that.  

### pelican auto static example

```markdown
![Cactus Image]({static ./img/cactus100.jpg})
```


### Liguid tag for inserting image with original size

```jinja
{% img {static|./img/cactus100.jpg} %} 
```

### Liguid tag for inserting image with specific size

```jinja
{% img /url/to/image.png [width] [height] [title] [alt] %}
```

### Insert HTML5/flash compatible videos:

```jinja
{% video /url/to/video.mp4 [width] [height] [title] %}
```

### Insert code from a file, with a title and link to download:

```jinja
{% include_code filename [title] %}
```

### Insert an HTML-rendered ipython notebook:

```jinja
{% notebook filename.ipynb [cells[start:end]] %}
```

### Reference:
https://github.com/getpelican/pelican-plugins/pull/21


