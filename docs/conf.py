"""Sphinx configuration."""

project = "Nusselt"
author = "Fábio P. Fortkamp"
copyright = "2024, Fábio P. Fortkamp"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
