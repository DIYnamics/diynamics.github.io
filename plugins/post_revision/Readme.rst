Post Revision
#############

This Pelican plugin extracts the post's revision history from Git, and offer
several ``article`` and ``page`` attributes. Please see more details and a
working example `here
<http://jhshi.me/2015/10/13/post-revision-plugin-for-pelican/index.html>`_.

Settings
========

- ``GITHUB_URL``: the Github URL where the page source repository is hosted.
  For example: https://github.com/jhshi/blog_source

- ``PROJECT_ROOT``: Root directory of the Pelican project. You should set this
  to ``os.path.dirname(os.path.abspath(__file__))``. I don't know if Pelican
  offers this already in some meta data, so let me know if that's the case and
  this settings is not necessary.
