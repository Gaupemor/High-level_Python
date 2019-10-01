#!/usr/bin/env python
""" 4.6: setup file for the package 'blur_package'.
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='blur-package-selmafs',
    version='1.0',
    author="selmafs",
    author_email="selmafs@student.matnat.uio.no",
    description="IN3110-19 mandatory assignment 4 package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.uio.no/IN3110/IN3110-selmafs/tree/master/assignment4",
    install_requires=[
        'numpy',
        'numba',
        'opencv-python'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Development Status :: 5 - Production/Stable",
        "License :: Free For Educational Use"
    ],
    python_requires='>=3.6'
)
