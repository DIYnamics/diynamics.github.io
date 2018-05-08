pelican-langcategory
====================

Plugin for Pelican to make languages behave the same as categories (visitor can browse articles in certain language)


## Usage

Check out the plugin to your pelican's plugins directory 

Edit your *pelicanconf.py*: 

    PLUGINS = ['pelican-langcategory']
    LANGUAGE_URL = 'lang/{lang}/'
    LANGUAGE_SAVE_AS = 'lang/{lang}/index.html'
    
Later you can visit url like '/lang/en/', '/lang/zh/' to browse your articles just like categories.

## Template

By default, this plugin try to find 'language' template to generate language specific pages, if it is not found, then fallback to use 'category' template.

Language template is recommended to be included in your pelican-theme, which can be just like category template with words changed. For example, language.html in your pelican theme repo will be like:

    {% extends "index.html" %}
    {% block content_title %}
    <h2>Articles in {{ language_name }}</h2>
    {% endblock %}

the 'language_name' varible will be automatically replaced by language name.

Available varibles:

  * {{ language }} language such as 'en', 'zh' as you write in your content files
  * {{ language_name}} language name such as 'English', 'Chinese'
    
## Dependencies

In order to use 'language_name' varible, you have to install 'pycountry' package.

    pip install pycountry
    
Without this package installed, 'language_name' will not show language's fullname but language code such as 'en', as same as 'language' varible.
