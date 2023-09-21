from setuptools import setup, find_packages

# Description of your package
DESCRIPTION = (
    '''A Python package to interact with the NetBox API.
        Version 1.0.0
       - Resources:
       * organizations
       * devices
       * connections
       * wireless
       * ipam
       * overlay
       * virtualization
       * circuits
       * power
       * provisioning
       * customization
       * operations      
               ''')

setup(
    name='netboxCli',
    version='1.0.0',
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)
