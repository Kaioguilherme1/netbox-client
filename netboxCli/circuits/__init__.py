from netboxcli.core import Core

from .circuit_types import CircuitTypes
from .circuits import CircuitsClass
from .provider_accounts import ProviderAccounts
from .provider_networks import ProviderNetworks
from .providers import Providers


class Circuits:
    """
    Circuits module
    """

    def __init__(self, netbox: Core):
        """
        Initialize the Circuits module.

        Args:
            netbox: (Core) The Netbox object generated by the Client class.
        """

        # circuits
        self.circuits = CircuitsClass(Core(netbox, '/api/circuits/circuits/'))
        self.circuit_types = CircuitTypes(
            Core(netbox, '/api/circuits/circuit-types/')
        )
        # providers
        self.providers = Providers(Core(netbox, '/api/circuits/providers/'))
        self.provider_accounts = ProviderAccounts(
            Core(netbox, '/api/circuits/provider-accounts/')
        )
        self.provider_networks = ProviderNetworks(
            Core(netbox, '/api/circuits/provider-networks/')
        )


__all__ = ['Circuits']
