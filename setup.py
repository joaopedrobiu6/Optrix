"""Setup/build/install script for nldesa."""

import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open(os.path.join(here, "requirements.txt"), encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="Optrix",
    version="0.0.1",
    description=("A package with tools to compute ray tracing using Matrix Optics."),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joaopedrobiu6/Optrix/",
    author="João Pedro Ferreira Biu",
    author_email="joaopedrofbiu@tecnico.ulisboa.pt",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    keywords="optics, ray tracing, matrix optics",
    packages=find_packages(exclude=["docs", "tests", "local", "report"]),
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.8",
    project_urls={
        "Issues Tracker": "https://github.com/joaopedrobiu6/Optrix/issues/",
        "Source Code": "https://github.com/joaopedrobiu6/Optrix/",
    },
)