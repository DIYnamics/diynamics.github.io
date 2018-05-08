from pelican import signals


def get_article_translations(article_generator):
    for article in article_generator.articles:
        for translation in article.translations:
            translation.is_translation_of = article


def get_page_translations(page_generator):
    for page in page_generator.pages:
        for translation in page.translations:
            translation.is_translation_of = page


def register():
    signals.article_generator_finalized.connect(get_article_translations)
    signals.page_generator_finalized.connect(get_page_translations)
