from setuptools import setup, find_packages

# Description of your package
DESCRIPTION = (
    '''A Python package to interact with the NetBox API.
        Version 0.5.0
       - Resources:
       * organizations
       * Devices
       * Connections
       * Ipam
       * Virtualization
       * Extras        
               ''')

setup(
    name='netboxCli',
    version='0.6.0',
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)
