pelicanthemes-generator
=======================

The pelicantheme-generator that generate the themes  from https://github.com/getpelican/pelican-themes project site

**Dependencies**

    * Python
    * imagemagick
    * CutyCapt
        * Archlinux: https://aur.archlinux.org/packages/cutycapt-qt4-svn/
        * Debian: https://packages.debian.org/stable/web/cutycapt

1. Prepare environment (optional)

.. code-block:: language

    mkvirtualenv --no-site-packages -p /usr/bin/python2.7 pelicanthemes-generator
    pip install -r requirements.txt

2. Prepare the project

.. code-block:: language

   mkdir ~/pelicanthemes-generator
   cd ~/pelicanthemes-generator
   git clone --recursive https://github.com/getpelican/pelican-themes ~/pelican-themes
   git clone https://github.com/badele/pelicanthemes-generator.git pelicanthemes-generator

3. Generate themes previews
   
.. code-block:: language

    cd ~/pelicanthemes-generator/pelicanthemes-generator
    ./generate_pelicanconfs.py ../pelican-themes
    ./generate_articles.py ../pelican-themes

Open two terminal

.. code-block:: language

    # In the first terminal
    make serve

    # In the second terminal
    ./generate_screenshots.py ../pelican-themes


You can see the result in http://pelicanthemes.jesuislibre.org

Sample result

.. image:: http://pelicanthemes.jesuislibre.org/static/jesuislibre_article.png
