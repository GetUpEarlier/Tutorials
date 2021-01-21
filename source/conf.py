# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------
from datetime import datetime
import re
import sphinx
import megengine

# -- Project information -----------------------------------------------------

project = 'MegEngine'
copyright = f'2020-{datetime.now().year}, Megvii Inc'
author = 'Megvii Inc'
version = megengine.__version__
release = version
language = 'zh_CN'

# -- General configuration ---------------------------------------------------

extensions = [
    'nbsphinx',
    'recommonmark',
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.autosummary',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
#    'sphinxcontrib.bibtex',
    'sphinx_copybutton'
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
source_encoding = "utf-8"

master_doc = 'index'
templates_path = ['_templates']
exclude_patterns = [
    '_build', 
    '_drafts', 
    'examples', 
    '**.ipynb_checkpoints'
]

# nbconvert can convert .ipynb files to sphinx outputs
try:
    import nbconvert
except ImportError:
    logger.warning("nbconvert not installed. Skipping notebooks.")
    exclude_patterns.append("**/*.ipynb")
else:
    try:
        nbconvert.utils.pandoc.get_pandoc_version()
    except nbconvert.utils.pandoc.PandocMissing:
        logger.warning("Pandoc not installed. Skipping notebooks.")
        exclude_patterns.append("**/*.ipynb")

# -- Options for HTML output -------------------------------------------------

html_theme = 'pydata_sphinx_theme'
html_theme_path = ['_themes']
html_theme_options = {
    "external_links": [],
    "github_url": "https://github.com/MegEngine/MegEngine"
}
html_static_path = ['_static']
html_css_files = [
    'css/custom.css'
]

html_sourcelink_suffix = ''

html_search_language = 'zh'
html_search_options = {
    'dict': 'jieba'
}
