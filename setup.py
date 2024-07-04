from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in qr/__init__.py
from qr import __version__ as version

setup(
	name="qr",
	version=version,
	description="QR Code Generator for Frappe, based on Segno",
	author="itsdave GmbH",
	author_email="dev@itsdave.de",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
