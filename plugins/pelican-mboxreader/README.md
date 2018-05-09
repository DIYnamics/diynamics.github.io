# pelican-mboxreader

This pelican plugin adds a generator that can load a Unix style mbox file and
generate articles from all the entries in the mailbox.

This was written to support easy interoperation between pelican and mailman
(which creates mbox archives). Future work, if done, will involve improving the
way (plaintext) email is turned into HTML and adding support for additional
mail directory types.

## Do I need other dependencies?

Yes; you need python's dateutil module (so dates in emails can be parsed without
assuming a standard time format).

The ```setup.py``` script will automatically take care of this when installing
the package.

## How do I install it?

pelican-mboxreader is packaged and available from PyPI; to install it, you can
simply run the following command: ```pip install pelican-mboxreader```.

Alternatively, you can clone the git repository, build it, and install it
yourself by running ```python setup.py install```.

## How does it work?

Enable it using any other Pelican plugin, though note that the plugin is named
```pelican_mboxreader```, then add it to the configuration as follows:

```
PLUGINS = [
    # ...
    'pelican_mboxreader',
    # ...
]
```

Then add the following settings to the configuration:

```
MBOX_PATH = ['/path/to/mail.box']
MBOX_CATEGORY = ['Name of Mbox Category']
```

```MBOX_PATH``` defaults to "input.mbox" in the current directory. If it is not present,
Pelican should behave gracefully. ```MBOX_CATEGORY`` defaults to "Mailbox".

As you might gather from these settings being lists, mboxreader supports taking input
from multiple Mailbox files. You must have one category name per mbox path.

### Other Configuration Options

```
MBOX_AUTHOR_STRING = ''
```

This string is appended to the end of authors created via mbox. This is used to
provide a way to distinguish authors via email and authors via normal Pelican,
if you want that. It is now disabled by default.

```
MBOX_MARKDOWNIFY = False
```

This setting controls whether to feed input emails into Markdown or whether they should
be converted "manually" (i.e. replacing newlines with paragraph tags and break tags as
appropriate), which is the default. Markdown is the closest to "plaintext" (compare to
reStructuredText) though in the future I'll likely add an option to use the rST parser
instead.

## Is support for other mailbox types (maildir, etc.) possible?

Yes. It would need to be programmed in and made configurable, however it would
be trivial if the mailbox type is implemented by [python's mailbox module](https://docs.python.org/2/library/mailbox.html)
(which is what this uses).

## Is this pointless?

Maybe. See the above note about mailman; it was written for a reason but may not
be something that anyone in the real world actually needs.

## Credits

Ben Rosser <rosser.bjr@gmail.com>

Written for use by the [JHUACM](https://www.acm.jhu.edu/).
