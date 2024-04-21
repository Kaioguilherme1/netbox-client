from setuptools import find_packages, setup

# Description of your package
DESCRIPTION = """A Python package to interact with the NetBox API.
        Version 1.0.2
       - Resources:
       * organizations
       * devices
       * connections
       * wireless
       * ipam
       * vpn
       * virtualization
       * circuits
       * power
       * provisioning
       * customization
       * operations      
               """

setup(
    name='netboxcli',
    version='1.0.2',
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)
