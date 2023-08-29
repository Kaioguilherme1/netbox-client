from setuptools import setup, find_packages

# Description of your package
DESCRIPTION = "A Python package to interact with the NetBox API."

setup(
    name='netboxCli',
    version='0.2.0',
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)
