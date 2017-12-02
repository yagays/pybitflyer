# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="pybitflyer",
    packages=['pybitflyer'],
    version="0.1.8",
    description="Python wrapper for bitFlyer's REST API.",
    author="yag_ays",
    author_email="yanagi.ayase@gmail.com",
    url="https://github.com/yagays/pybitflyer",
    install_requires=['requests'],
    keywords=["bitcoin", "bitflyer", "wrapper", "REST API"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
