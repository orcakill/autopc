# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

sys.path.insert(0, os.path.abspath('../autopc'))

project = 'autopc'
copyright = '2024, orcakill'
author = 'orcakill'
release = '1.0'

import mock

mock_list = ['cv2', 'Xlib', 'numpy', 'mss', 'wda', 'ffmpeg', 'logzero', 'PIL', 'psutil']
win_mock_list = [
    'win32api',
    'win32con',
    'win32gui',
    'win32ui',
    'win32clipboard',
    'pywinauto',
    'pywintypes',
    'pywinauto.application',
    'pywinauto.win32functions',
    'pywinauto.win32structures',
    'airtest.core.win.ctypesinput'
]
ios_mock_list = [
    'tidevice', 'tidevice._usbmux', 'tidevice._device', 'tidevice._proto', 'tidevice.exceptions', ]
for mod_name in mock_list + win_mock_list + ios_mock_list:
    sys.modules[mod_name] = mock.MagicMock()

sys.modules["cv2"].__version__ = "3.2.0.7"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.doctest',
              'sphinx.ext.todo',
              'sphinx.ext.coverage',
              'sphinx.ext.imgmath',
              'sphinx.ext.ifconfig',
              'sphinx.ext.viewcode',
              'sphinx.ext.autosectionlabel',
              'sphinx.ext.napoleon',
              'recommonmark',
              'sphinx_markdown_tables',
              'sphinx.ext.intersphinx',
              'sphinx.ext.mathjax', ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'zh_cn'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# source_suffix = '.rst'
from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u''

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

todo_include_todos = True

# -- Options for HTML output ----------------------------------------------


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']
#
# html_css_files = [
#     'css/custom.css',
# ]
# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'airtestdoc'

# -- Options for LaTeX output ---------------------------------------------

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
    (master_doc, 'airtest.tex', u'airtest Documentation',
     u'Game-Netease', 'manual'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'airtest', u'airtest Documentation',
     [author], 1)
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'airtest', u'airtest Documentation',
     author, 'airtest', 'One line description of project.',
     'Miscellaneous'),
]

# default is alphabetical, we trust source sequence
autodoc_member_order = 'bysource'
# remove leading package.module names
add_module_names = False
# napoleaon ext
napoleon_use_param = True
napoleon_use_rtype = True

# internalization
# uncomment following line to make zh_CN html
if os.environ.get("LAN") == "zh":
    language = 'zh_CN'  # language supported
locale_dirs = ['locale/']  # path is example but recommended.
gettext_compact = False  # optional.