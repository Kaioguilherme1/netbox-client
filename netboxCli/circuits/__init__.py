from netboxCli.core import Core
from .circuits import CircuitsClass
from .circuit_types import CircuitTypes
from .providers import Providers
from .provider_accounts import ProviderAccounts
from .provider_networks import ProviderNetworks

class Circuits:
    def __init__(self, netbox):
        #circuits
        self.circuits = CircuitsClass(Core(netbox, '/api/circuits/circuits/'))
        self.circuit_types = CircuitTypes(Core(netbox, '/api/circuits/circuit-types/'))
        #providers
        self.providers = Providers(Core(netbox, '/api/circuits/providers/'))
        self.provider_accounts = ProviderAccounts(Core(netbox, '/api/circuits/provider-accounts/'))
        self.provider_networks = ProviderNetworks(Core(netbox, '/api/circuits/provider-networks/'))

__all__ = ['Circuits']
