import logging
import re

from pelican import contents, signals

log = logging.getLogger(__name__)

ERT_WPM = 200  # words per minute by default
ERT_FORMAT = '{time} read'


def initialize(gen):
    global ERT_WPM, ERT_FORMAT
    for option in ['ERT_WPM', 'ERT_FORMAT']:
        if not option in gen.settings.keys():
            log.warning(
                'The necessary config option is missing: {},\
 using default value: \'{}\''.format(option, globals()[option])
            )
        else:
            globals()[option] = gen.settings[option]


def strip_tags(content):
    return re.sub(u'<!--.*?-->|<[^>]*>', '', content)


def estimate(text):
    minutes = len(strip_tags(text).split()) / ERT_WPM
    if minutes < 1:
        time = '< 1 min'
    elif minutes < 60:
        time = '{} min'.format(round(minutes))
    else:
        if time // 60 == 1:
            end = ''
        else:
            end = 's'
        time = '{} hour{} {} min'.format(
            round(minutes // 60),
            end,
            round(minutes - (minutes // 60) * 60)
        )
    return ERT_FORMAT.format(time=time)


def ert(obj):
    if obj._content:
        obj.ert = estimate(obj._content)


def register():
    signals.article_generator_init.connect(initialize)
    signals.content_object_init.connect(ert)
