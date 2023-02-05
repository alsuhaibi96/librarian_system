from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in librarian_system/__init__.py
from librarian_system import __version__ as version

setup(
	name="librarian_system",
	version=version,
	description="librarian",
	author="librarian",
	author_email="librarian@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
