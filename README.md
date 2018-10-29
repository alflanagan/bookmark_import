# Bookmarks Parser

A project to develop a parser/importer for Mozilla's 'HTML export' format (which is actually not HTML at all).

Currently developing in parallel:

* a version using the [lxml package](https://lxml.de) to parse file as HTML (problem: it's not, really)

* a version using the [ply package](https://www.dabeaz.com/ply/) to build a parser for the export format

# Status

Firefox now stores backups in JSON format, making this project superfluous. See [MarskManager](https://github.com/alflanagan/MarksManager) for a project to do useful things with those backup files.
