#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PATH = "content"
AUTHOR = "Ben McNeill"
SITENAME = "Ben McNeill's Blog"
SITETITLE = SITENAME


RELATIVE_URLS = False
# SITEURL = "http://localhost:8000"
# SITEURL = "https://sad-raman-4ee550.netlify.app/"
SITEURL = "https://benmcneill.dev"

SITESUBTITLE = "Engineer | Software Developer | Data Scientist"

# DISPLAY_PAGES_ON_MENU = True

ARTICLE_URL = "{slug}.html"
ARTICLE_SAVE_AS = "{slug}.html"

STATIC_PATHS = ["img", "files", "html", "extra", "2020"]
EXTRA_PATH_METADATA = {
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/jm-photo.jpg": {"path": "jm-photo.jpg"},
    "extra/CNAME": {"path": "CNAME"},
    "extra/cactus.jpg": {"path": "cactus.jpg"},
}

GITHUB_CORNER_URL = "https://github.com/bfmcneill/benmcneill.dev"

TIMEZONE = "America/Denver"

DEFAULT_LANG = "en"

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    (
        "Profitable Python Podcast",
        "https://podcasts.apple.com/us/podcast/profitable-python/id1472548149",
    ),
)

# Social widget
SOCIAL = (
    ("twitter", "https://twitter.com/bfmcneill"),
    ("linkedin", "https://www.linkedin.com/in/bfmcneill/"),
    ("github", "https://github.com/bfmcneill"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "./themes/Flex"

PLUGIN_PATHS = [
    "./plugins/",
]

PLUGINS = [
    "tipue_search",
    "liquid_tags.img",
    "liquid_tags.youtube",
    "autostatic",
    "pelican-cover-image",
]

USE_TIPUE_SEARCH = True
DIRECT_TEMPLATES = ["index", "tags", "categories", "authors", "archives", "search"]


MENUITEMS = (
    # ("Authors", "/authors.html"),
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
    # ("Sitemap", "/sitemap.xml"),
    # ('RSS', "feeds/all.atom.xml")
    # ("Search","/search.html")
)
