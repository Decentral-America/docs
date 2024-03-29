# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'DecentralChain'
copyright = '2021, Blockchain Costa Rica'
author = 'Josue Rojas'

# The short X.Y version
#version = ''
# The full version, including alpha/beta/rc tags
#release = '0.1'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',	
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.mathjax',
    'sphinx_design',
    'sphinx_copybutton',
    # For extension examples and demos
    'ablog',
    'jupyter_sphinx',
    'matplotlib.sphinxext.plot_directive',
    'myst_nb',
    #'nbsphinx',  # Uncomment and comment-out MyST-NB for local testing purposes.
    'numpydoc',
    'sphinx_togglebutton',
]

html_theme = "pydata_sphinx_theme"
html_logo = "_static/logo.png"
html_favicon = "_static/icon.svg"
html_sourcelink_suffix = ""

html_theme_options = {
   "external_links": [
        {
            "url": "http://decentralchain.io/",
            "name": "Website",
        },
        {
            "url": "http://decentral.exchange/",
            "name": "Wallet & Exchange",
        },
        {
            "url": "https://decentralscan.com/",
            "name": "Explorer",
        },
    ],
   "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/Decentral-America/docs",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/decentralchain",
            "icon": "fa-brands fa-twitter",
        },
        {
            "name": "LinkedIn",
            "url": "https://www.linkedin.com/company/decentralchain/",
            "icon": "fa-brands fa-linkedin",
        },
        {
            "name": "Youtube",
            "url": "https://www.youtube.com/@decentralchain",
            "icon": "fa-brands fa-youtube",
        },
        {
            "name": "Discord",
            "url": "https://discord.gg/9UUbNBPQ3D",
            "icon": "fa-brands fa-discord",
        },
        {
            "name": "Discord",
            "url": "https://www.instagram.com/decentralchain/",
            "icon": "fa-brands fa-instagram",
        },
        #{
        #    "name": "Medium",
        #    "url": "https://medium.com/@decentralchain",
        #    "icon": "fa-brands fa-medium",
        #},
    ],
    "header_links_before_dropdown": 3,
    "logo": {
        #"text": "",
        "image_dark": "logo-dark.png",
        "alt_text": "DecentralChain",
    },
    "use_edit_page_button": True,
    "show_toc_level": 1,
    "navbar_align": "left",  # [left, content, right] For testing that the navbar items align properly
    #"navbar_center": ["version-switcher", "navbar-nav"],
    #"announcement": "https://raw.githubusercontent.com/pydata/pydata-sphinx-theme/main/docs/_templates/custom-template.html",
    # "show_nav_level": 2,
    # "navbar_start": ["navbar-logo"],
    # "navbar_end": ["theme-switcher", "navbar-icon-links"],
    # "navbar_persistent": ["search-button"],
    # "primary_sidebar_end": ["custom-template.html", "sidebar-ethical-ads.html"],
    "footer_items": ["copyright"],# "sphinx-version", "theme-version"],
    # "secondary_sidebar_items": ["page-toc.html"],  # Remove the source buttons
    # "search_bar_position": "navbar",  # TODO: Deprecated - remove in future version
}

# This allows us to use ::: to denote directives, useful for admonitions
myst_enable_extensions = ["colon_fence", "linkify", "substitution"]

myst_heading_anchors = 2
myst_substitutions = {"rtd": "[Read the Docs](https://readthedocs.org/)"}


# True to prefix each section label with the name of the document it is in, followed by a colon
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 7

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ["custom.css"]
todo_include_todos = True

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Documentation'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Documentation.tex', 'Documentation',
     'Josue Rojas', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'Documentation', 'Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Documentation', 'Documentation',
     author, 'Documentation', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------

# add sourcecode to path
import sys, os
sys.path.append("scripts")
from gallery_directive import GalleryDirective
sys.path.insert(0, os.path.abspath('../src'))
 
############################
# SETUP THE RTD LOWER-LEFT #
############################
try:
   html_context
except NameError:
   html_context = dict()
html_context['display_lower_left'] = True

if 'REPO_NAME' in os.environ:
	REPO_NAME = os.environ['REPO_NAME']
else:
	REPO_NAME = ''
 
# SET CURRENT_LANGUAGE
if 'current_language' in os.environ:
   # get the current_language env var set by buildDocs.sh
   current_language = os.environ['current_language']
else:
   # the user is probably doing `make html`
   # set this build's current language to english
   current_language = 'en'
 
# tell the theme which language to we're currently building
html_context['current_language'] = current_language
 
# SET CURRENT_VERSION
from git import Repo
repo = Repo( search_parent_directories=True )
 
if 'current_version' in os.environ:
   # get the current_version env var set by buildDocs.sh
   current_version = os.environ['current_version']
else:
   # the user is probably doing `make html`
   # set this build's current version by looking at the branch
   current_version = repo.active_branch.name
 
# tell the theme which version we're currently on ('current_version' affects
# the lower-left rtd menu and 'version' affects the logo-area version)
html_context['current_version'] = current_version
html_context['version'] = current_version
 
# POPULATE LINKS TO OTHER LANGUAGES
html_context['languages'] = [ ('en', '/en/' +current_version+ '/') ]
 
languages = [lang.name for lang in os.scandir('locales') if lang.is_dir()]
for lang in languages:
   html_context['languages'].append( (lang, '/' +lang+ '/' +current_version+ '/') )
 
# POPULATE LINKS TO OTHER VERSIONS
html_context['versions'] = list()
 
versions = [branch.name for branch in repo.branches]
for version in versions:
   html_context['versions'].append( (version, '/'  +current_language+ '/' +version+ '/') )
 
# POPULATE LINKS TO OTHER FORMATS/DOWNLOADS
 
# settings for creating PDF with rinoh
rinoh_documents = [(
 master_doc,
 'target',
 project+ ' Documentation',
 '© ' +copyright,
)]
today_fmt = "%B %d, %Y"
 
# settings for EPUB
epub_basename = 'target'
 
html_context['downloads'] = list()
#html_context['downloads'].append( ('pdf', '/' +current_language+ '/' +current_version+ '/' +project+ '-docs_' +current_language+ '_' +current_version+ '.pdf') )
html_context['downloads'].append( ('epub', '/' +current_language+ '/' +current_version+ '/' +project+ '-docs_' +current_language+ '_' +current_version+ '.epub') )
 
##########################
# "EDIT ON GITHUB" LINKS #
##########################
 
html_context['display_github'] = True
html_context['github_user'] = 'Decentral-America'
html_context['github_repo'] = 'docs'
html_context['github_version'] = 'master/docs/'
 
def setup(app):
    # Add the gallery directive
    app.add_directive("gallery-grid", GalleryDirective)