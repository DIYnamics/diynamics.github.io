from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
install_requires = [
        'requests',
        ]

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pelican-meetup-info',
    version='0.0.2',
    description='A Pelican plugin that provides group and event information for a meetup.com group.',
    long_description=long_description,
    url='https://github.com/tylerdave/pelican-meetup-info',
    author='Dave Forgac',
    author_email='tylerdave@tylerdave.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        #'Programming Language :: Python :: 2',
        #'Programming Language :: Python :: 2.6',
        #'Programming Language :: Python :: 2.7',
        #'Programming Language :: Python :: 3',
        #'Programming Language :: Python :: 3.2',
        #'Programming Language :: Python :: 3.3',
        #'Programming Language :: Python :: 3.4',
    ],
    keywords='pelican plugin meetup',
    py_modules=["pelican_meetup_info"],
    install_requires=[install_requires],
)
