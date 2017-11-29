# coding: utf-8

"""
:copyleft: (c) 2014 by Taehoon Kim.
:license: GNU GPL, see LICENSE for more details.
このライブラリはTaehoon Kim氏が開発し、Sh1maが改良したライブラリです。
"""

from distutils.core import setup

setup(
    name         = "line",
    version      = "0.9.3",
    author       = "Aiden",
    author_email = "rootmelo92118@gmail.com",
    packages     = ["LineApi", "LineThrift"],
    package_dir  = {"": "LineAlpha"},
    install_requires = [
    "thrift==0.9.3",
    "requests",
    "rsa",
    ]
)
