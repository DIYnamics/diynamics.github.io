# -*- coding: utf-8 -*-
"""
pdf_img
=======

Searches for any `<img>` tags within your article for which the source is a
PostScript, EPS, or PDF file. It will produce a PNG preview of the file,
which will also act as a link to the original file. This can be useful for
including scientific plots in articles and pages.
"""

import logging
import re
import os.path

from bs4 import BeautifulSoup, FeatureNotFound
from wand.image import Image
from wand.color import Color
from wand.exceptions import BlobError

from pelican import signals
from pelican.utils import mkdir_p, get_relative_path, path_to_url
from pelican.generators import ArticlesGenerator, PagesGenerator

import sys
if (sys.version_info[0]>2):
    unicode = str

__version__ = '0.0.1'

logger = logging.getLogger(__name__)

preview_dir = '__pdf_previews__'
FORMAT_RE = re.compile(r'(?:\.pdf|\.ps|\.eps)\s*$',re.IGNORECASE)
pdf_imgs = {}

def process_content(article):
    """
    Get a list of PDF, PS, and EPS files for which PNG previews must be generated.
    Also make the substitutions in article content so that the PNG will be used as
    a preview and provide a link to the original.
    """
    try:
        soup = BeautifulSoup(article._content,'lxml')
    except FeatureNotFound:
        soup = BeautifulSoup(article._content,'html.parser')
    
    for img in soup.find_all('img',src=FORMAT_RE):
        src = re.sub(article.settings['INTRASITE_LINK_REGEX'],'',img['src'].strip())
        if src.startswith(('http://','https://','ftp://')): continue
        if src.startswith('/'):
            src = src[1:]
        else:
            # relative to the source path of this content
            src = article.get_relative_source_path(os.path.join(article.relative_dir, src))
        if src not in article._context['filenames']:
            unquoted_path = src.replace('%20', ' ')
            if unquoted_path in article._context['filenames']:
                src = unquoted_path
        linked_content = article._context['filenames'].get(src)
        if not linked_content:
            continue
        link = img.wrap(soup.new_tag("a"))
        link['href'] = img['src']
        png_save_as = os.path.join(preview_dir, linked_content.save_as + '.png')
        pdf_imgs[linked_content.source_path] = png_save_as
        siteurl = article.get_siteurl()
        if article.settings['RELATIVE_URLS']:
            siteurl = path_to_url(get_relative_path(article.save_as))
        png_url = '/'.join((siteurl, preview_dir, linked_content.url + '.png'))
        png_url = png_url.replace('\\', '/')
        img['src'] = png_url
    
    article._content = unicode(soup)

    
def get_pdf_imgs(generators):
    # Process the articles and pages
    for generator in generators:
        if isinstance(generator, ArticlesGenerator):
            for article in generator.articles:
                process_content(article)
        elif isinstance(generator, PagesGenerator):
            for page in generator.pages:
                process_content(page)
    

def convert_pdfs(pelican):
    """
    Create the PNGs from the original PDF, PS, and EPS files, placing them
    in the approriate location in the output directory.
    """
    with Color('white') as white:
        for path in pdf_imgs:
            outpath = os.path.join(pelican.output_path, pdf_imgs[path])
            mkdir_p(os.path.dirname(outpath))
            try:
                with Image(filename=os.path.join(pelican.path, path)+'[0]',
                           resolution=100, background=white) as img:
                    img.format = 'png'
                    img.save(filename=outpath)
                    logger.info('Creating PNG preview of %s as %s', path,
                                pdf_imgs[path])
            except BlobError:
                logger.warn('Could create PNG preview of `{}`'.format(src))


def register():
    signals.all_generators_finalized.connect(get_pdf_imgs)
    signals.finalized.connect(convert_pdfs)
