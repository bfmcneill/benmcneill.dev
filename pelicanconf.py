#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PATH = 'content'
AUTHOR = "Ben McNeill"
SITENAME = "Ben McNeills's Blog"
SITETITLE = SITENAME


RELATIVE_URLS = True
SITEURL = "http://localhost:8000"
SITESUBTITLE = "Engineer | Software Developer | Data Scientist"

DISPLAY_PAGES_ON_MENU = True

ARTICLE_URL = "{slug}.html"
ARTICLE_SAVE_AS = "{slug}.html"

STATIC_PATHS = ["img", "files", "html", "extra", "2020"]

GITHUB_CORNER_URL = "https://github.com/bfmcneill/benmcneill.dev"

TIMEZONE = 'America/Denver'

DEFAULT_LANG = 'en'

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
    ('Podcast', 'https://podcasts.apple.com/us/podcast/profitable-python/id1472548149'),
         )

# Social widget
SOCIAL = (
    ('twitter', 'https://twitter.com/bfmcneill'),
    ('linkedin', 'https://www.linkedin.com/in/bfmcneill/'),
    ('github', 'https://github.com/bfmcneill'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "./themes/Flex"

PLUGIN_PATHS = [
    "./plugins/",
]

PLUGINS = [
    "tipue_search",
    'liquid_tags.img',
    'liquid_tags.youtube',
    "autostatic",
]

USE_TIPUE_SEARCH = True
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'search']
