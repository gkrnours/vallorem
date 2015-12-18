#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ludovic Coues'
SITENAME = u'Pelican Test Site'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

THEME = 'themes/basic'
PLUGINS = ['plugin']


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


DEFAULT_PAGINATION = 20
DEFAULT_ORPHANS = 4
PAGINATION_PATTERNS = (
	(1, '{base_name}/', '{base_name}/index.html'),
	(2, '{base_name}/{number}/', '{base_name}/{number}/index.html'),
)


SLUGIFY_SOURCE = 'title'
PAGE_SAVE_AS     = '{category}/{slug}/index.html'
PAGE_URL         = '{category}/{slug}'
PAGE_LANG_SAVE_AS= '{category}/{slug}/{lang}/index.html'
PAGE_LANG_URL    = '{category}/{slug}/{lang}'
ARTICLE_SAVE_AS     = 'publications/{date:%Y}/{slug}/index.html'
ARTICLE_URL         = 'publications/{date:%Y}/{slug}'
ARTICLE_LANG_SAVE_AS= 'publications/{date:%Y}/{slug}/{lang}/index.html'
ARTICLE_LANG_URL    = 'publications/{date:%Y}/{slug}/{lang}'
YEAR_ARCHIVE_SAVE_AS = 'publications/{date:%Y}/index.html'


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
