Page View using Google Analytics
================================

If you track your site's page view using Google Analytics, this plugin can pull
the page view information from your Google Analytics profile and add a
``page_view`` attribute to each article and page in your Pelican site. See a
live example here.

http://jhshi.me


Requirements and Setup
----------------------

First, follow the `instructions here
<https://developers.google.com/analytics/devguides/reporting/core/v3/quickstart/service-py>`_
to set up Google API service account.

Then in Google Analytics, add the email address you created above as an user so
that we can access the Google Anaytics API.

At this point, you should have:

- Google API service email: ``<prioject_id>-<unique_id>@developer.gserviceaccount.com``
- Google private key file: ``client_private.p12``. Save this file somewhere
  secure. If you put this file in a Git repository, don't forget to add it to
  ``.gitignore``.


Finally, install the Google API Python library:

.. code-block:: bash

    $ pip install --upgrade google-api-python-client


Settings
--------

You need to provide the following information in your Pelican configuration file
for this plugin to communicate with the Google Analytics API.

- ``GOOGLE_SERVICE_ACCOUNT``: the service email.
- ``GOOGLE_KEY_FILE``: path to the private key file, E.g.
  ``./client_private.p12``.
- ``GA_START_DATE``: start date to count page view. E.g., ``2005-01-01``.
- ``GA_END_DATE``: end date to count page view. E.g., ``today``.
- ``GA_METRIC``: counting metrics, default is ``ga:pageviews``. See other options
  `here
  <https://developers.google.com/analytics/devguides/reporting/core/dimsmets>`_.
  Right now we only support query with ONE metric.
- ``POPULAR_POST_START``: start date to count popular page views. E.g., ``A
  month ago``.


With this plugin installed, each ``article`` and ``page`` object has two extra
attributes:

- ``pageview``: total number of page views between ``GA_START_DATE`` and
  ``GA_END_DATE``.
- ``popular_pageview``: total number of page view between ``POPULAR_POST_START``
  and ``GA_END_DATE``.

And there is one global context named ``total_page_view``,
which is the total page view of the entire site.


Note
----

If you encounter this error while building:

.. code-block:: bash

    NotImplementedError: PKCS12 format is not supported by the PyCrypto library.

Try convert the ``p12`` file to ``pem`` file:

.. code-block:: bash

    $ openssl pkcs12 -in client_private.p12 -nodes -nocerts > client_private.pem

The password should be ``notasecret``.

Then set ``GOOGLE_KEY_FILE`` to be the ``pem`` file just generated.



Resources
---------

- `Google Analytics Core Reporting API
  <https://developers.google.com/analytics/devguides/reporting/core/v3/reference>`_
- `Google Analytics Query Explorer
  <https://ga-dev-tools.appspot.com/query-explorer/>`_
