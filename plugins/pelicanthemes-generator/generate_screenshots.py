#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: 2013 @ bruno@adele.im / bruno.adele.im
#
# use:
# generate_screenshot.py ../pelican-themes

import time
import sys
import os


# Search all template files
def list_themes(themesroot):
    dirlist = []
    allfiles = os.listdir(themesroot)
    for dirname in allfiles:
        dirname = dirname.lower()
        if os.path.isdir('%s/%s/templates' % (themesroot, dirname)):
            dirlist.append(dirname)

    return sorted(dirlist)


def generate_screenshot(themesroot, theme):
            print ("")

            os.system("cat pelicanconf_default.py > pelicanconf.py")
            os.system("cat confs/%s_pelicanconf.py >> pelicanconf.py" % theme)
            os.system("echo \"THEME = '%s/%s'\" >> pelicanconf.py" % (themesroot, theme))

            print ("generate screenshot for %s" % theme)
            os.system("rm -rf output/*")
            os.system("make html")

            params = '--min-width=1024 --delay=2000 --max-wait=2000'
            os.system("CutyCapt %s --url=http://localhost:8000 --out=content/static/%s_index_tmp.png" % (params, theme))
            os.system("CutyCapt %s --url=http://localhost:8000/details-information-for-%s-theme.html --out=content/static/%s_article_tmp.png" % (params, theme, theme))
            os.system("convert content/static/%s_index_tmp.png -trim content/static/%s_index.png" % (theme, theme)) 
            os.system("convert content/static/%s_article_tmp.png -trim content/static/%s_article.png" % (theme, theme)) 
            os.system("convert content/static/%s_index.png -resize %s -gravity north -crop 410x307 content/static/small_%s_index.png" % (theme, '410x307', theme)) 
            os.system("convert content/static/%s_article.png -resize %s  -gravity north -crop 410x307 content/static/small_%s_article.png" % (theme, '410x307', theme)) 
            os.system("rm content/static/%s_*_tmp.png" % theme)

def create_directories():
    dirs = ['output', 'content/static', 'confs']
    for directory in dirs:
        if not os.path.exists(directory):
            os.makedirs(directory)


def generate_screenshots(themesroot):
    create_directories()
    # Generate all screenshots
    themes = list_themes(themesroot)
    for theme in themes:
        confname = 'confs/%s_pelicanconf.py' % theme
        if os.path.exists(confname):
            generate_screenshot(themesroot, theme)

    generate_screenshot(themesroot, 'jesuislibre')


if len(sys.argv) == 2:
    generate_screenshots(sys.argv[1])
