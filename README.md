# Source code for the DIYnamics website: https://diynamics.github.io/

This repository holds the source code for the website of the
"DIYnamics" science education and outreach project.

## For students and educators
Want to use or learn more about the DIYnamics materials?  Visit the
page directly: https://diynamics.github.io/

## For DIYnamics team members (and others who want to chip in)
If you are a DIYnamics member or someone else interested in improving
our website, then feel free to browse our source code and/or open an
Issue with any questions or suggestions.  Thanks!

## Instructions for rendering updates to the site
(Note: for internal use only.  Only select DIYnamics team members have
write access to the repo.  Contact Spencer to request write
permission.)

Our builds use [Pelican](https://docs.getpelican.com/en/stable/) and
the [ghp-import](https://github.com/c-w/ghp-import) utility, both of
which you can install via pip or conda.

To build the site, from the repo top-level directory:

```sh
git checkout develop
make clean && make html
ghp-import output -b master
git checkout master
git push origin master
git checkout develop
```

<div align="center">
  <img src="https://diynamics.github.io/images/eyu-2017/eyu2017_baroclinic.jpg"><br>
</div>
