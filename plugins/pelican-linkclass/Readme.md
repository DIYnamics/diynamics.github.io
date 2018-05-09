# Link Class for Pelican

## Description

This plugin allows the setting of the class attribute of `<a>` elements
(generated in Markdown by `[ext](link)`) according to whether the link is
external (i.e. starts with `http://` or `https://`) or internal to the
Pelican-generated site.

For now, this plugin only works with Markdown.

## Usage

### User Settings

The names of the classes can be specified in the Pelican setting files with
the following variables:

- `LINKCLASS_EXTERNAL_CLASS`: name of the class for external links
  (defaults to `'external'`)
- `LINKCLASS_INTERNAL_CLASS`: name of the class for internal links
  (defaults to `'internal'`) 

### Styling the hyperlinks

One of the possible uses of this plugins is for styling.  Suppose that we
have the following in your article written with Markdown:

```markdown
This is an [internal](intenal) link and this is an
[external](http://external.com) link.
```

If the default values of the configuration variables are used, then a
 possible CSS setting would be:

```css
a.external:before {
    content: url('../images/external-link.png');
    margin-right: 0.2em;
}
```

(The file `external-link.png` is also distributed with this plugin.  Just
copy it to the appropriate place in your website source tree, for instance
in `theme/static/images/`.)

Then, the result will look like the following:

![figure](linkclass-example.png)

Note that this plugin also works with reference-style links, as in the
following example:

```markdown
This is an [internal][internal] link and this is an
[external][external] link.

 [internal]: internal
 [external]: http://external.com
```

## Author

Copyright (C) 2015, 2017  Rafael Laboissiere (<rafael@laboissiere.net>)

Released under the GNU Affero Public License, version 3 or later.  No warranties.
