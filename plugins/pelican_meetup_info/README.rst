====================
pelican-meetup-info
====================

A Pelican plugin for including Meetup group and event information on generated pages and articles.

***************
Installation
***************

* Install this package:

  .. code-block:: shell

    pip install pelican_meetup_info

* Add the following to your `pelicanconf.py` to activate the plugin:

  .. code-block:: python

    PLUGINS = ['pelican_meetup_info']

* Then add one of the following pairs of configs:

  * If you keep your config file private:

    .. code-block:: python  
  
      MEETUP_API_KEY = 'your key here'
      MEETUP_URLNAME = 'Cleveland-Area-Python-Interest-Group'

    Get your API key here: https://www.google.com/search?q=meetup+api+key&ie=utf-8&oe=utf-8

  * Or if you expose your config file to the public (like in a public repo):

    .. code-block:: python  
  
      MEETUP_GROUP_SIGNED_URL = 'https://api.meetup.com/Cleveland-Area-Python-Interest-Group?photo-host=public&sig_id=1442&sig=3c0d385c607d27a7bd3ae14f220f17856eb163c1'
      MEETUP_EVENTS_SIGNED_URL= 'https://api.meetup.com/Cleveland-Area-Python-Interest-Group/events?photo-host=public&page=20&sig_id=1442&sig=3dcd3aa3bfacf17cb45302a722ced9727e99cd37'
     
    More info about signed URLs here: https://www.meetup.com/meetup_api/auth/#keysign


***************
Usage
***************

With the plugin installed and properly configured, new dictionaries named `meetup_group` and `meetup_events` containg the Meetup API responses will be availabe in your page/article context. You may reference them in templates like this:

meetup_group:

  .. code-block:: html  

    {% if page.meetup_group %}
    <h2>Meetup Info</h2>
    <h3><a href="{{ page.meetup_group.link }}">{{ page.meetup_group.name }}</a></h3>
    {{ page.meetup_group.description }}
    {% endif %}

More info about group data: https://secure.meetup.com/meetup_api/console/?path=/:urlname

meetup_events:

  .. code-block:: html

    {% if page.meetup_events %}
    <h2>Upcoming Meetups</h2>
    <ul>
        {% for meetup_event in page.meetup_events[:3] %}
        <li>
            <h3><a href="{{ meetup_event.link }}">{{ meetup_event.name }}</a></h3>
            <p>{{ meetup_event.local_date }} at {{ meetup_event.local_time }}</p>
            <p>{{ meetup_event.description }}</p>
            <p>At {{ meetup_event.venue.name }} - {{ meetup_event.venue.address_1 }}, {{ meetup_event.venue.city }}, {{ meetup_event.venue.state }} {{meetup_event.venue.zip }}</p>
        </li>
        {% endfor %}
    </ul>
    {% endif %}

More info about events data: https://secure.meetup.com/meetup_api/console/?path=/:urlname/events
