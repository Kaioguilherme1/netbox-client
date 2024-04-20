from netboxCli.core import Core
from .ike_policies import IkePolicies
from .ike_proposals import IkeProposals
from .ipsec_policies import IpsecPolicies
from .ipsec_profiles import IpsecProfiles
from .ipsec_proposals import IpsecProposals
from .tunnel_grups import TunnelGrups
from .tunnel_terminations import TunnelTerminations
from .tunnels import Tunnels
from .l2vpns import L2vpns
from .terminations import Terminations

class Vpn:
    def __init__(self, netbox):
        self.ike_policies = Core(netbox, '/api/vpn/ike-policies/')
        self.ike_proposals = Core(netbox, '/api/vpn/ike-proposals/')
        self.ipsec_policies = Core(netbox, '/api/vpn/ipsec-policies/')
        self.ipsec_profiles = Core(netbox, '/api/vpn/ipsec-profiles/')
        self.ipsec_proposals = Core(netbox, '/api/vpn/ipsec-proposals/')
        self.tunnel_groups = Core(netbox, '/api/vpn/tunnel-groups/')
        self.tunnel_terminations = Core(netbox, '/api/vpn/tunnel-terminations/')
        self.tunnels = Core(netbox, '/api/vpn/tunnels/')
        self.l2vpns = L2vpns(Core(netbox, '/api/vpn/l2vpns/'))
        self.terminations = Terminations(Core(netbox, '/api/vpn/l2vpn-terminations/'))

__all__ = ['Vpn']
