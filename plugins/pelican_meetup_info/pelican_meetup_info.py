import logging
import requests
from pelican import signals

logger = logging.getLogger(__name__)

class MeetupInfoPluginError(Exception):
    pass

def get_api_urls(settings):
    api_key = settings.get('MEETUP_API_KEY')
    urlname = settings.get('MEETUP_URLNAME')
    if api_key and urlname:
        meetup_group_url = 'https://api.meetup.com/{}?photo_host=public&key={}'.format(urlname, api_key)
        meetup_events_url = 'https://api.meetup.com/{}/events?photo-host=public&page=20&key={}'.format(urlname, api_key)
    else:
        meetup_group_url = settings.get('MEETUP_GROUP_SIGNED_URL')
        meetup_events_url = settings.get('MEETUP_EVENTS_SIGNED_URL')

    if not (meetup_group_url and meetup_events_url):
        raise MeetupInfoPluginError('Either (MEETUP_API_KEY and MEETUP_URLNAME) or '
            '(MEETUP_GROUP_SIGNED_URL and MEETUP_EVENTS_SIGNED_URL) must be provided.')

    return meetup_group_url, meetup_events_url

def get_meetup_info(settings):
    group_url, events_url = get_api_urls(settings)

    # TODO: Handle exceptions and optionally use setting to continue upon error
    logger.info('Getting group info from Meetup.com API...')
    group_response = requests.get(group_url)
    group_response.raise_for_status()
    group_info = group_response.json()
    logger.info('Getting events info from Meetup.com API...')
    events_response = requests.get(events_url)
    events_response.raise_for_status()
    events_info = events_response.json()
    return group_info, events_info

def add_meetup_info(generators):
    group_info, events_info = get_meetup_info(generators[0].settings)

    for generator in generators:
        for attr in ['articles', 'pages']:
            for content in getattr(generator, attr, []):
                content.meetup_group = group_info
                content.meetup_events = events_info

def register():
    signals.all_generators_finalized.connect(add_meetup_info)
