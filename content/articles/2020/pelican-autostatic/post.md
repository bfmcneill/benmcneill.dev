Title: Pelican Autostatic Plugin
Date: 2020-07-10 10:20
Modified: 2020-07-10 19:30
Category: Dev Resources
Tags: python, pelican, pelican-plugins
Slug: pelican-autostatic-plugin
Author: Ben McNeill 
Summary: Notes on pelican autostatic plugin
cover_image: https://images.unsplash.com/photo-1527430253228-e93688616381?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1782&q=80
cover_image_by: Rock'n Roll Monkey
cover_image_link: https://unsplash.com/photos/R4WCbazrD1g

<!-- {% img {static|/extra/cactus.jpg} 200 200 "Cactus" "Alt text" %} -->

Pelican autostatic is the plugin you want to use when trying to reference content relative to your markdown file.  It also works with liquid tags.

```jinja
{% img {static|./img/cactus100.jpg} 200 200 "" "Alt text" %}
```

### Additional Resources: 

- pelican-autostatic [git repo](https://github.com/AlexJF/pelican-autostatic)
- pelican-autostatic [pypi](https://pypi.org/project/pelican-autostatic/)


