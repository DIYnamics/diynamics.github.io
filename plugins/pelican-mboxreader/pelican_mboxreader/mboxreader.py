"""mboxreader - Pelican plugin to interface with Unix mailboxes.

This pelican plugin implements a custom generator that can read from
an arbitrary number of Unix mboxes (support for maildirs or other types
of mail folders coming soon) and turns them into articles with a unique
SLUG.
"""

from pelican import signals
from pelican.generators import ArticlesGenerator, Generator
from pelican.contents import Article, Page, Static, is_valid_content
from pelican.utils import copy, process_translations, mkdir_p
from pelican.utils import DateFormatter, slugify
from pelican.readers import BaseReader, Readers

from pelican import signals

from itertools import chain, groupby
from operator import attrgetter, itemgetter
from collections import defaultdict
from functools import partial

import datetime
import mailbox
import logging
import os
import pytz
import sys

# Other dependency! dateutil.
try:
    from dateutil import parser
except ImportError:    # NOQA?
    parser = False

# Markdown-- a half-decent plaintext -> HTML converter, for now.
try:
    from markdown import Markdown
except ImportError:
    Markdown = False  # NOQA

# The logger.
logger = logging.getLogger()


# Settings methods, adapted from tag-cloud plugin.
# https://github.com/getpelican/pelican-plugins/blob/master/tag_cloud/tag_cloud.py
def set_default_settings(settings):
    settings.setdefault('MBOX_PATH', '[input.mbox]')
    settings.setdefault('MBOX_CATEGORY', '[Mailbox]')
    settings.setdefault('MBOX_AUTHOR_STRING', '')
    settings.setdefault('MBOX_MARKDOWNIFY', False)


def init_default_config(pelican):
    from pelican.settings import DEFAULT_CONFIG
    set_default_settings(DEFAULT_CONFIG)
    if pelican:
        set_default_settings(pelican.settings)


def plaintext_to_html(plaintext, markdownify=False):
    # If markdownify is True, attempt to use markdown as a basic plaintext to
    # HTML converter. If we fail or if it's false, insert <p> tags as
    # appropriate and do no more.
    try:
        if not markdownify:
            raise RuntimeError
        content = Markdown().convert(plaintext)
    except:
        content = ''
        plaintext = plaintext.replace("\r\n", "\n")
        strings = plaintext.split("\n\n")
        for paragraph in strings:
            paragraph = paragraph.replace("\n", "<br/>")
            content += "<p>" + paragraph + "</p>\n\n"

    return content


class MboxGenerator(ArticlesGenerator):

    def __init__(self, *args, **kwargs):
        """initialize properties"""
        self.articles = []  # only articles in default language
        self.translations = []
        self.dates = {}
        self.categories = defaultdict(list)
        self.authors = defaultdict(list)
        super(MboxGenerator, self).__init__(*args, **kwargs)

    # Private helper function to generate
    def _generate_mbox_articles(self, mboxPath, mboxCategory):

        baseReader = BaseReader(self.settings)
        category = baseReader.process_metadata('category', mboxCategory)

        # Complain if the mbox path does not exist and is not readable.
        try:
            if not os.path.exists(mboxPath):
                raise RuntimeError
            mbox = mailbox.mbox(mboxPath)
        except:
            logger.error('Could not process mbox file %s', mboxPath)
            return

        # Retrieve some fields from the settings.
        authorString = self.settings.get('MBOX_AUTHOR_STRING')
        markdownify = self.settings.get('MBOX_MARKDOWNIFY')

        # Loop over all messages, turn them into article objects.
        all_articles = []
        slugs = []

        for message in mbox.itervalues():
            # Get author name.
            author = message['from']
            if author is None:
                author = 'Unknown'
            else:
                if '<' and '>' in author:
                    author = author[:author.find(' <')]
                author = author.replace('"', '').replace("'", '')
            # As a hack to avoid dealing with the fact that names can collide.
            if authorString is not None and authorString != '':
                author += ' ' + authorString
            authorObject = baseReader.process_metadata('author', author)

            # Get date object, using python-dateutil as an easy hack.
            # If there is no date in the message, abort, we shouldn't bother.
            if message['date'] is None:
                continue
            if parser:
                date = parser.parse(message['date'])
            else:
                logger.error('No python-dateutil, we cannot continue as ' +
                             'date formats cannot be parsed. ')
                continue
            monthYear = date.strftime('%B-%Y').lower()

            # Get title and slug; build year + month into slug.
            subject = message['subject']
            slugSubject = slugify(subject)
            slug = os.path.join(slugify(mboxCategory), monthYear, slugSubject)

            # Hack to handle multiple messages with the same subject.
            if slug in slugs:
                slug += "_%d"
                count = 2
                testSlug = slug % count
                while testSlug in slugs:
                    count += 1
                    testSlug = slug % count
                slug = testSlug
            slugs.append(slug)

            # Code adapted from Stackoverflow for parsing email messages.
            # https://stackoverflow.com/questions/4824376/parse-multi-part-email-with-sub-parts-using-python
            # Code is clumsy, should be refactored.
            if message.is_multipart():
                plaintext = None
                html = None
                for part in message.get_payload():
                    payload = part.get_payload(decode=True)
                    if payload is not None:
                        for charset in message.get_charsets():
                            if charset is not None and charset != 'x-unknown':
                                # These probably shoudldn't be 'ignore'.
                                if sys.version_info.major >= 3 and not isinstance(payload, str):
                                    payload = payload.decode(charset, "ignore")
                                elif sys.version_info.major <= 2:
                                    payload = unicode(payload, charset, "ignore").encode("ascii", "replace")
                    if part.get_content_type() == 'text/plain':
                        plaintext = payload
                    if part.get_content_type() == 'text/html':
                        html = payload
                if plaintext is None and html is None:
                    continue
                elif plaintext is None:
                    content = html
                else:
                    if sys.version_info.major >= 3 and isinstance(plaintext, bytes):
                        plaintext = plaintext.decode("utf-8", "ignore")
                    content = plaintext_to_html(plaintext, markdownify)
            else:
                payload = message.get_payload(decode=True)
                for charset in message.get_charsets():
                    if charset is not None and charset != 'x-unknown':
                        if sys.version_info.major < 3:
                            payload = unicode(payload, charset, "ignore").encode("ascii", "replace")
                        else:
                            payload = payload.decode(charset)
                if sys.version_info.major >= 3 and isinstance(payload, bytes):
                    payload = payload.decode("utf-8", "ignore")
                content = plaintext_to_html(payload, markdownify)

            # On python 2, it seems that we need to do this final check of content.
            if sys.version_info.major <= 2:
                content = unicode(content, "us-ascii", "ignore").encode("ascii", "replace")

            metadata = {'title': subject,
                        'date': date,
                        'category': category,
                        'authors': [authorObject],
                        'slug': slug}

            article = Article(content=content,
                              metadata=metadata,
                              settings=self.settings,
                              source_path=mboxPath,
                              context=self.context)

            # This seems like it cannot happen... but it does without fail.
            article.author = article.authors[0]
            all_articles.append(article)

        return all_articles

    # For now, don't generate feeds.
    def generate_feeds(self, writer):
        return

    def generate_pages(self, writer):
        """Generate the pages on the disk"""
        write = partial(writer.write_file,
                        relative_urls=self.settings['RELATIVE_URLS'],
                        override_output=True)

        # to minimize the number of relative path stuff modification
        # in writer, articles pass first
        self.generate_articles(write)
        self.generate_period_archives(write)
        self.generate_direct_templates(write)

        # and subfolders after that
        self.generate_categories(write)
        self.generate_authors(write)

    def generate_articles(self, write):
        """Generate the articles."""
        # Hm... this is a bit clunky; it overrides override_output.
        # It appears that this is not a problem.
        for article in chain(self.translations, self.articles):
            write(article.save_as, self.get_template(article.template),
                  self.context, article=article, category=article.category,
                  override_output=True, blog=True)

    def generate_context(self):
        # Update the context (only articles in default language)
        self.articles = self.context['articles']

        # Complain if MBOX_PATH and MBOX_CATEGORY are not of the same length.
        mboxPaths = self.settings.get('MBOX_PATH')
        mboxCategories = self.settings.get('MBOX_CATEGORY')
        errMsg = 'MBOX_PATH, MBOX_CATEGORY not of equal length or non-empty.'
        if len(mboxPaths) != len(mboxCategories) or len(mboxPaths) <= 0:
            logger.error(errMsg)
            return

        all_articles = []
        # To avoid pulling in a dependency, define this convenient lambda.
        future_range = lambda x: range(x) if not sys.version_info.major <= 2 else xrange(x)
        for i in future_range(len(mboxPaths)):
            mboxPath = mboxPaths[i]
            mboxCategory = mboxCategories[i]

            new_articles = self._generate_mbox_articles(mboxPath, mboxCategory)
            all_articles.extend(new_articles)

            # Log that we did stuff.
            print(('Read in %d messages from %s and converted to articles in ' +
                  'category %s.') % (len(new_articles), mboxPath, mboxCategory))
        print('Read in %d messages from all mailboxes.' % (len(all_articles)))

        # Continue with the rest of ArticleGenerator, code adapted from:
        # https://github.com/getpelican/pelican/blob/master/pelican/generators.py#L548

        # ARTICLE_ORDER_BY doesn't exist in 3.3, which was in Fedora 21.
        # (I wanted to be able to build this on F21 at the time).
        articles, translations = process_translations(all_articles)
        # , order_by=self.settings['ARTICLE_ORDER_BY'])
        self.articles.extend(articles)
        self.translations.extend(translations)

        # Disabled for 3.3 compatibility, great.
        # signals.article_generator_pretaxonomy.send(self)

        for article in self.articles:
            # only main articles are listed in categories and tags
            # not translations
            # We have to use django for this, unfortunately.
            if article.date.tzinfo is None:
                article.date = pytz.UTC.localize(article.date)
            self.categories[article.category].append(article)
            # Support for Author and Authors.
            if hasattr(article, 'author') and article.author.name != '':
                self.authors[article.author].append(article)
            else:
                for author in getattr(article, 'authors', []):
                    self.authors[author].append(article)

        # This may not technically be right, but...
        # Sort the articles by date too.
        self.articles = list(self.articles)
        self.dates = self.articles
        self.dates.sort(key=attrgetter('date'),
                        reverse=self.context['NEWEST_FIRST_ARCHIVES'])

        # and generate the output :)

        # order the categories per name
        self.categories = list(self.categories.items())
        self.categories.sort(reverse=self.settings['REVERSE_CATEGORY_ORDER'])

        self.authors = list(self.authors.items())
        self.authors.sort()

        self._update_context(('articles', 'dates', 'categories', 'authors'))
        # Disabled for 3.3 compatibility for now, great.
        # self.save_cache()
        # self.readers.save_cache()

        # And finish.
        # signals.article_generator_finalized.send(self)


def get_generators(pelican_object):
    return MboxGenerator


def register():
    signals.initialized.connect(init_default_config)
    signals.get_generators.connect(get_generators)
