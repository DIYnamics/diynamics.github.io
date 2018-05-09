figure-ref
==========

Provides a system to reference figures using labels, as happens in LaTeX.

Requirements
============

`figure-ref` requires `BeautifulSoup4`.

```bash
pip install BeautifulSoup4
```

How to Use
==========

This plugin will search for labels within `<figcaption>` tags. Figures and
figcaptions can be inserted via Restructured Text or using the
[figureAltCaption](https://github.com/jdittrich/figureAltCaption) plugin with
Markdown. Labelled figures take the form:
```html
<figure>
  <img src="path/to/image.png">
  <figcaption>
  labelname :: This is the label text.
  </figcaption>
</figure>
```
In Markdown, using the aforementioned plugin, you can create such a figure
with the syntax `![labelname :: This is the label text.](path/to/image.png)`.

This would be traslated to
```html
<figure id="figref-labelname">
  <img src="path/to/image.png">
  <figcaption>
  <strong>Figure 1:</strong> This is the label text.
  </figcaption>
</figure>
```

This figure can be referenced in a paragraph using the syntax `{#labelname}`.
This will then be replaced by the figure number, which will act as a link
to the figure.
