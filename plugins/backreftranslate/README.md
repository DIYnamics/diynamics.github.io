# pelican-plugin-backref-translate
Pelican Plugin to add {article,page}.is_translation_of attribute

This plugin add a new attribute to every article/page (that is a translation of any other article/page) an attributewhich points back to the original article/page.

For every item in a ``article.translations`` list, a new attribute ``is_translation_of`` is created pointing back to ``article``.

For every item in a ``page.translations`` list, a new attribute ``is_translation_of`` is created pointing back to ``page``.
