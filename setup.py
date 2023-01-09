# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in programing_app/__init__.py
from programing_app import __version__ as version

setup(
	name="programing_app",
	version=version,
	description="js and python programing",
	author="Naqeeb khan",
	author_email="naqeebkhan8262@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
