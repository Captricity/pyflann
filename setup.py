#!/usr/bin/python
from setuptools import setup, find_packages
setup(
	name = "pyflann",
	version = "1.6.11",
	packages = ['pyflann'],
	
	install_requires = [],
	include_package_data = True,
	package_data = {
		'': ['*.txt', '*.rst', '*.html', '*.frag'],
	},
)
