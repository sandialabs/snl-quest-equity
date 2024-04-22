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
        "numpy==1.22.4",
        "scipy==1.6.2",
        "pandas==1.4.3",
        "pyomo==6.1.2",
        "matplotlib==3.5.1",
        "kivy==2.2.1",
        "kivy-garden==0.1.4",
        "xlrd==2.0.1",
        "six==1.15.0",
        "jinja2==2.11.3",
        "bs4==0.0.1",
        "requests==2.28.1",
        "urllib3==1.26.4",
        "holidays==0.11.2",
        "seaborn==0.11.1",
        "eppy==0.5.59",
        "openpyxl==3.0.7",
        "pyutilib==6.0.0",
        "numpy_financial==1.0.0",
        "geopandas==0.11.1",
        "markupsafe==1.1.1",
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
