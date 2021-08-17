from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in slnee_monitoring/__init__.py
from slnee_monitoring import __version__ as version

setup(
	name="slnee_monitoring",
	version=version,
	description="Custom App For Monitoring and Documentation",
	author="erpcloud.systems",
	author_email="info@erpcloud.systems",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
