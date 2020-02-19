# Copyright (C) 2020 Arrai Innovations Inc. - All Rights Reserved
from setuptools import setup

from genpw import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as req:
    install_requires = [x for x in req.read().split("\n") if x]

setup(
    name="genpw",
    url="https://github.com/arrai-innovations/genpw/",
    version=__version__,
    description="Generate pronounceable passwords in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Arrai Innovations",
    author_email="support@arrai.com",
    packages=["genpw"],
    install_requires=install_requires,
    license="LICENSE",
    test_suite="tests",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: BSD License",
        "Environment :: Console",
        "Intended Audience :: Developers",
    ],
)
