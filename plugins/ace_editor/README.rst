=============================
Ace Editor plugin for Pelican
=============================

This plugin adds an **ace editor** to all code-block.
see more : https://ace.c9.io

The default theme does not include *ace editor**, but it is pretty easy to add one (on base.html):

    {{ ace_editor }}

Settings
--------

settings on **ace editor** are declared with a dictionnary :
``ACE_EDITOR_PLUGIN = {}``

==================================================    =====================================================
Dictionnary parameters (followed by default value)    What does it do?
==================================================    =====================================================
``ACE_EDITOR_THEME = 'chrome'``                       Choose the ace editor's theme https://github.com/ajaxorg/ace/tree/master/lib/ace/theme

``ACE_EDITOR_SCROLL_TOP_MARGIN = 0``                  WWith an anchor Url, this setting applied a top margin (in
                                                      pixels) : Especially used with the **height** of an horizontal menu.
``ACE_EDITOR_MAXLINES = 50``                          Defines the max vertical editor size. After this, editor
                                                      display will be truncate... (defaut theme add vertical scrollbars)
``ACE_EDITOR_READONLY = True``                        Editor will be readable or writable
``ACE_EDITOR_AUTOSCROLL = True``                      Needed if editor is inside a scrollable page
``ACE_EDITOR_SHOW_INVISIBLE = True``                  All white spaces would be displayed
==================================================    =====================================================

If you're using markdown, you must add this settings on your pelicanconf.py:

* if pelican <= 3.6.3 :

    .. code-block:: python

        MD_EXTENSIONS = [
            'codehilite(css_class=highlight, linenums=False, use_pygments=False)'
        ]

* if pelican > 3.6.3 :

    .. code-block:: python

        MD_EXTENSIONS = {
            'markdown.extensions.codehilite': {
                'css_class': 'highlight',
                'linenums': False,
                'use_pygments': False
            }
        }
