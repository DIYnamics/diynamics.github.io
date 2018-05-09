from pelican import signals
from pelican.generators import ArticlesGenerator, PagesGenerator

from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials

import httplib2

import parsedatetime as pdt
import datetime
import sys


def get_service(api_name, api_version, scope, key_file_location,
                service_account_email):
    """Get a service that communicates to a Google API.

    Args:
      api_name: The name of the api to connect to.
      api_version: The api version to connect to.
      scope: A list auth scopes to authorize for the application.
      key_file_location: The path to a valid service account p12 key file.
      service_account_email: The service account email address.

    Returns:
      A service that is connected to the specified API.
    """

    f = open(key_file_location, 'rb')
    key = f.read()
    f.close()

    credentials = SignedJwtAssertionCredentials(service_account_email, key,
                                                scope=scope)

    http = credentials.authorize(httplib2.Http())

    # Build the service object.
    service = build(api_name, api_version, http=http)

    return service


def get_first_profile_id(service):
    # Use the Analytics service object to get the first profile id.

    # Get a list of all Google Analytics accounts for this user
    accounts = service.management().accounts().list().execute()

    if accounts.get('items'):
        # Get the first Google Analytics account.
        account = accounts.get('items')[0].get('id')

        # Get a list of all the properties for the first account.
        properties = service.management().webproperties().list(
            accountId=account).execute()

        if properties.get('items'):
            # Get the first property id.
            property = properties.get('items')[0].get('id')

            # Get a list of all views (profiles) for the first property.
            profiles = service.management().profiles().list(
                accountId=account,
                webPropertyId=property).execute()

            if profiles.get('items'):
                # return the first view (profile) id.
                return profiles.get('items')[0].get('id')

    return None


def get_page_view(generators):
    generator = generators[0]
    service_account_email = generator.settings.get(
        'GOOGLE_SERVICE_ACCOUNT', None)
    key_file_path = generator.settings.get('GOOGLE_KEY_FILE', None)

    page_view = dict()
    popular_page_view = dict()

    try:
        scope = ['https://www.googleapis.com/auth/analytics.readonly']
        service = get_service('analytics', 'v3', scope, key_file_path,
                            service_account_email)
        profile_id = get_first_profile_id(service)

        start_date = generator.settings.get('GA_START_DATE', '2005-01-01')
        end_date = generator.settings.get('GA_END_DATE', 'today')
        metric = generator.settings.get('GA_METRIC', 'ga:pageviews')

        result = service.data().ga().get(ids='ga:' + profile_id, start_date=start_date,
                                        end_date=end_date, max_results=999999, metrics=metric,
                                        dimensions='ga:pagePath').execute()
        for slug, pv in result['rows']:
            page_view[slug] = int(pv)

        popular_start_str = generator.settings.get('POPULAR_POST_START', 'a month ago')
        popular_start_date = str(pdt.Calendar().parseDT(
            popular_start_str, datetime.datetime.now())[0].date())
        popular_result = service.data().ga().get(
            ids='ga:' + profile_id, start_date=popular_start_date,
            end_date=end_date, max_results=999999, metrics=metric,
            dimensions='ga:pagePath').execute()

        for slug, pv in popular_result['rows']:
            popular_page_view[slug] = int(pv)
    except:
        sys.stderr.write("[ga_page_view] Failed to fetch page view information.\n")

    article_generator = [g for g in generators if type(g) is ArticlesGenerator][0]
    page_generator = [g for g in generators if type(g) is PagesGenerator][0]

    ARTICLE_SAVE_AS = generator.settings['ARTICLE_SAVE_AS']
    PAGE_SAVE_AS = generator.settings['PAGE_SAVE_AS']

    total_page_view = 0
    for pages, url_pattern in [(article_generator.articles, ARTICLE_SAVE_AS),
                               (page_generator.pages, PAGE_SAVE_AS)]:
        for page in pages:
            url = '/%s' % (url_pattern.format(**page.__dict__))
            pv = page_view.get(url, 0)
            setattr(page, 'pageview', pv)
            setattr(page, 'popular_pageview', popular_page_view.get(url, 0))
            total_page_view += pv

    generator.context['total_page_view'] = total_page_view


def register():
    signals.all_generators_finalized.connect(get_page_view)
