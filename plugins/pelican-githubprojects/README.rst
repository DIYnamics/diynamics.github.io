=======================
Pelican Github Projects
=======================

Embed a list of your public GitHub projects in your pages.

Installation
============

To install pelican-githubprojects, simply install it from PyPI:

.. code-block:: bash

    $ pip install pelican-githubprojects

Configuration
=============

Enable the plugin in your pelicanconf.py

.. code-block:: python

    PLUGINS = [
        # ...
        'pelican_githubprojects',
        # ...
    ]

Add a setting with your GitHub username.

.. code-block:: python

    GITHUB_USER = 'kura'

Optionally specify the order in which projects appear.
The choices for each parameter are provided at
https://developer.github.com/v3/repos/#list-user-repositories.

.. code-block:: python

    GITHUB_USER_TYPE = "owner"
    GITHUB_SORT_BY = "created"
    GITHUB_DIRECTION = "desc"


Available data
==============

:name:
    The name of your project.
:language:
    The language your project is written in, information on how GitHub detects
    languages is `available here
    <https://help.github.com/articles/my-repository-is-marked-as-the-wrong-language>`_.
    It is GitHub that detects the language, not this plugin. So please, no
    issues about that.
:description:
    The description of your project (as set on GitHub.)
:homepage:
    The homepage of your project (as set on GitHub.)
:github_url:
    The web page URL of your project on GitHub (not the GIT or API URL.)
:stars:
    Number of stars for the project.
:size:
    Size of the project, in kilobytes.
:fork:
    Whether the project is forked from another project.
:forks:
    Number of forks of the project.
:private:
    Whether the repository is private.
:created:
    Time of creation of the repository as a string.
:updated:
    Time of last update of the repository as a string.
:id:
    Repository ID.

Usage
=====

In your templates you will be able to iterate over the `github_projects`
variable, as below.

.. code-block:: html

    {% if GITHUB_USER %}
        <h1>Projects</h1>
        {% for project in github_projects %}
            <h2>{{ project.name }} <sup>({{ project.language }})</sup></h2>
            {% if project.description %}<p>{{ project.description }}</p>{% endif %}
            <p>
                {% if project.homepage %}<a href="{{ project.homepage }}">Homepage</a>{% endif %}
                <a href="{{ project.github_url }}">GitHub</a>
            </p>
        {% endfor %}
    {% endif %}

License
=======

`MIT`_ license.

.. _MIT: http://opensource.org/licenses/MIT
