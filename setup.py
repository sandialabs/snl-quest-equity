from setuptools import setup, find_packages
from distutils.core import Extension

DISTNAME = "quest-equity"
VERSION = "1.0"
EXTENSIONS = []
PYTHON_REQUIRES = ">=36"
DESCRIPTION = "Sandia National Laboratories application suite for energy storage equity and environmental justice analysis and evaluation tools."
LONG_DESCRIPTION = open("README.md").read()
AUTHOR = "Sandia National Laboratories"
MAINTAINER_EMAIL = "dmrose@sandia.gov"
LICENSE = "BSD 3-clause"
URL = "https://www.github.com/snl-quest/snl-quest-equity"

setuptools_kwargs = {
    "scripts": [],
    "include_package_data": True,
    "install_requires": [
        "numpy",
        "scipy",
        "pandas>=0.24.2",
        "pyomo>=5.6",
        "matplotlib>=3.5.1",
        "kivy>=2.2.1",
        "kivy-garden",
        "xlrd",
        "six",
        "jinja2",
        "bs4",
        "requests",
        "urllib3",
        "holidays",
        "seaborn",
        "eppy",
        "openpyxl",
        "pyutilib",
        "numpy_financial",
    ],
}

setup(
    name=DISTNAME,
    version=VERSION,
    packages=find_packages(),
    ext_modules=EXTENSIONS,
    python_requires=PYTHON_REQUIRES,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    maintainer_email=MAINTAINER_EMAIL,
    license=LICENSE,
    url=URL,
    **setuptools_kwargs
)
