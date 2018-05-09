#coding: utf-8
import logging
from operator import attrgetter, itemgetter
from collections import defaultdict

from pelican import signals
from pelican.urlwrappers import URLWrapper


class Language(URLWrapper):
    def __init__(self, name, *args, **kwargs):
        super(Language, self).__init__(name.strip(), *args, **kwargs)
        self.lang = self.name

def generate_lang_as_category(generator, writer):
    self = generator
    self.languages = defaultdict(list)

    try:
        template = self.get_template('language')
    except TemplateNotFound:
        template = self.get_template('category')

    if not self.settings['LANGUAGE_SAVE_AS']:
        return

    # If LANGUAGE_URL has a trailing slash, remove it and provide a warning
    logger = logging.getLogger(__name__)
    langurl = self.settings['LANGUAGE_URL']
    if (langurl.endswith('/')):
        self.settings['LANGUAGE_URL'] = langurl[:-1]
        logger.warning("Removed extraneous trailing slash from LANGUAGE_URL.")

    for article in self.articles + self.translations:
        self.languages[article.lang].append(article)

    for lang, items in self.languages.items():
        lang_wrapper = Language(lang, self.settings)
        items.sort(key=attrgetter('date'), reverse=True)
        dates = [article for article in self.dates if article in items]

        # Override Default Language Setting
        self.settings['DEFAULT_LANG'] = lang
        override_in_default_lang_items = []
        for i in items:
            i.lang = lang
            i.in_default_lang = True
            override_in_default_lang_items.append(i)
        items = override_in_default_lang_items

        try:
            import pycountry
            lang_obj = pycountry.languages.get(alpha_2=str(lang))
            language_name = lang_obj.name if lang_obj else lang
        except ImportError:
            language_name = lang
        except KeyError:
            language_name = lang

        writer.write_file(lang_wrapper.save_as,
            template,
            self.context,
            articles=items,
            dates=dates,
            paginated={'articles': items, 'dates': dates},
            page_name=lang_wrapper.page_name,
            language=lang,
            language_name=language_name,
            all_articles=items
        )

def register():
    signals.article_writer_finalized.connect(generate_lang_as_category)
