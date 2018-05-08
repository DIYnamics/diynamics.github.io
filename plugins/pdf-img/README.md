pdf-img
==========

Searches for any `<img>` tags within your article for which the source is a
PostScript, EPS, or PDF file. It will produce a PNG preview of the file and this
PNG will be displayed as the image. This preview
will also act as a link to the original file. If the PDF/PS/EPS file is a
multi-page document, then only the first page will be used for the preview.
This plugin may be useful for including scientific plots in articles and pages.

Note that the previews will be stored in a directory called `__pdf_previews__`
stored at the root of the output directory. Errors may arise in the unlikely
event that one of your static directories also has this name.

Requirements
------------

`figure-ref` requires [BeautifulSoup4](http://www.crummy.com/software/BeautifulSoup/) and [wand](http://docs.wand-py.org/en/0.4.1/). Wand, in turn, requires
that [ImageMagick](http://www.imagemagick.org/script/index.php) be installed.

```bash
pip install BeautifulSoup4 wand
sudo apt-get install imagemagick   # Works for Ubuntu-based Linux distributions
```

