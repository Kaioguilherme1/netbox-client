from netboxCli.core import Core

from .l2vpns import L2vpns
from .terminations import Terminations

class Overlay:
    def __init__(self, netbox):
        self.l2vpns = L2vpns(Core(netbox, '/api/ipam/l2vpns/'))
        self.terminations = Terminations(Core(netbox, '/api/ipam/l2vpn-terminations/'))

__all__ = ['Overlay']
