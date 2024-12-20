# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
# ruff: noqa

import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "${{ values.name }}"
copyright = "2024, (C) Science and Technology Facilities Council"
author = "${{ values.gitAuthorName }}"
release = "0.0.0dev0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "autoapi.extension",
    "sphinx-pydantic",
    "sphinx_rtd_theme",
    "sphinx_mdinclude",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# Autoapi Configuration
autoapi_dirs = ["../${{ values.module }}", "../tests"]
autoapi_keep_docs = True
master_doc = "index"
autoapi_options = [
    "members",
    "undoc-members",
    "private-members",
    "show-inheritance",
    "show-module-summary",
    "special-members",
    "imported-members",
]
