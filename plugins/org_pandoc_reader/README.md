org_pandoc_reader
=============

A pandoc [org] reader plugin for [pelican]


Requirements
------------

  - [pandoc] in $PATH


Installation
------------

Instructions for installation of pelican plugins can be obtained from the [pelican plugin manual](https://github.com/getpelican/pelican-plugins/blob/master/Readme.rst).


Configuration
-------------

Additional command line parameters can be passed to pandoc via the ORG_PANDOC_ARGS parameter.

    ORG_PANDOC_ARGS = ['--mathjax',
                       '--smart',
                       '--toc',
                       '--toc-depth=2',
                       '--number-sections',
                       '--standalone',
                       '--highlight-style=espresso',]


Usage Notes
-----------
Simply use org-mode (.org) files instead of markdown files anywhere in your pelican blog.


Note that in order for code blocks in your or files to be formatted with syntax highlighting, 
code block headers should be placed on a separate line from the block demarcation. i.e.:

    #+headers :results code replace output
    #+begin_src sh
    # source code
    #+end_src


Example
-------
[Live example](http://jotham-city.com/)


Contributing
------------
If you have an issue please report it through the GH issues.

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

[org]: http://orgmode.org/
[pandoc]: http://johnmacfarlane.net/pandoc/
[pelican]: http://getpelican.com

Acknowledgements
----------------
[pandoc_reader](https://github.com/liob/pandoc_reader)
