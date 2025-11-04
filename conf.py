# conf.py

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# Project information
project = 'Project'
author = 'Author'

# -- General configuration ---------------------------------------------------

extensions = [
    'myst_parser',  # to support Markdown files
]

# Source file suffixes - support both reStructuredText and Markdown
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

master_doc = 'index'  # your root document

templates_path = ['_templates']  # Important: enables your custom templates

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_title = "Installing Webroot on Another Computer Made Easy: Reinstall or Download Webroot on Windows 10/11 for Your Already Purchased PC"

# You can still add html_meta here if you want, but with the new Read the Docs addons
# custom template is the reliable way to inject meta tags.

# If you want to add other meta tags, do so in your _templates/layout.html


