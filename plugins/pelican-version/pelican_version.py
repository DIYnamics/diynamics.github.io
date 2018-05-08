"""
Article list generator plugin for Pelican
================================

The idea is to generate a (json) file to be able to communicate togehter with Ajax calls
This will allow creating single page endless scroll without the need of using server side files
"""

from pelican import signals
from jinja2 import Environment, FileSystemLoader

import os


def generate_version(generator):
    versionPath = generator.settings.get('VERSION_PATH', 'content')
    path = os.path.dirname(os.path.realpath(__file__))
    outputPath = generator.settings.get('OUTPUT_VERSION_PATH', 'output')
    env = Environment(loader=FileSystemLoader(path))
    template = env.get_template('version.html')
    try:
        currentVersionFile = open(versionPath + '/currentVersion', 'r')
        currentVersion = int(currentVersionFile.read()) + 1
    except:
        currentVersion = 0

    output_from_parsed_template = template.render(version=currentVersion)
    with open(versionPath + "/currentVersion", "w+b") as fh:
        fh.write(output_from_parsed_template)
    with open(outputPath + "/version", "wb") as fh:
        fh.write(output_from_parsed_template)


def register():
    signals.finalized.connect(generate_version)
