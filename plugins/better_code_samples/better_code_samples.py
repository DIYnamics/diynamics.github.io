# The MIT License (MIT)
#
# Copyright (c) 2014 Christoph Lassner
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""
Better Code Samples
-------------------

This plugin:

- Adds a div wrapper around all tables with class name 'codehilitetable'
- The surrounding div is of class 'hilitewrapper' and can be used to
  add an appropriate style to the code samples, e.g. for making them
  scrollable.
"""

from pelican import signals

from bs4 import BeautifulSoup

import logging
logger = logging.getLogger(__name__)

def content_object_init(instance):
    if instance._content is not None:
        content = instance._content
        soup = BeautifulSoup(content, "html5lib")

        if 'table' in content:
            for ctbl in soup.find_all('table', class_="codehilitetable"):
                wrapper_tag = soup.new_tag('div')
                wrapper_tag['class'] = 'hilitewrapper'
                ctbl.wrap(wrapper_tag)
        instance._content = soup.decode()
        # If beautiful soup appended html tags.
        if instance._content.startswith('<html>'):
          instance._content = instance._content[12:-14]

def register():
    signals.content_object_init.connect(content_object_init)
