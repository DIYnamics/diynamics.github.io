# -*- coding: utf-8 -*-
"""
figure_ref
==============

A Pelican plugin that provices a LaTeX-like system for referencing figure
elements within an article or page. Figures whose figcaption elements begin
with the format

    labelname :: caption text

will have `labelname ::` replaced by figure numbering. This figure can
be referenced with the syntax {#labelname}, which will be replaced by
the figure number. The figure number will provide a link to the figure.
"""

import logging
import re

from bs4 import BeautifulSoup, FeatureNotFound

from pelican import signals
from pelican.generators import ArticlesGenerator, PagesGenerator

import sys
if (sys.version_info[0]>2):
    unicode = str

__version__ = '0.0.1'

REF_RE = re.compile("\{#\s*(\w+)\s*\}")
LABEL_RE = re.compile("^\s*(\w+)\s*::")
REF = "<a href='#figref-{}'>{}</a>"
LABEL = "<strong>Figure {}:</strong> "

logger = logging.getLogger(__name__)

def process_content(article):
    """
    Substitute reference links for an individual article or page.
    """
    try:
        soup = BeautifulSoup(article._content,'lxml')
    except FeatureNotFound:
        soup = BeautifulSoup(article._content,'html.parser')
    
    # Get figures and number them
    figlist = []
    for fig in soup.find_all('figcaption'):
        caption = unicode(fig.string)
        m = LABEL_RE.search(caption)
        if m:
            figlist.append(m.group(1))
            fig.parent['id'] = 'figref-' + m.group(1)
            new_tag = soup.new_tag("strong")
            fig.string.replace_with(' ' + caption[m.end():])
            new_tag.string = "Figure {}:".format(len(figlist))
            fig.insert(0,new_tag)
    
    # Replace references to figures with links
    def substitute(match):
        try:
            num = figlist.index(match.group(1)) + 1
        except ValueError:
            logger.warn('`figure_ref` unable to find figure with label "{}" in file {}'.format(match.group(1), article.source_path))
            return match.string
        return REF.format(match.group(1),num)
        
    article._content = REF_RE.sub(substitute, unicode(soup))



def add_figure_refs(generators):
    # Process the articles and pages
    for generator in generators:
        if isinstance(generator, ArticlesGenerator):
            for article in generator.articles:
                process_content(article)
        elif isinstance(generator, PagesGenerator):
            for page in generator.pages:
                process_content(page)



def register():
    signals.all_generators_finalized.connect(add_figure_refs)
