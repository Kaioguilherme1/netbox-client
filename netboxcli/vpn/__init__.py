from netboxcli.core import Core

from .ike_policies import IkePolicies
from .ike_proposals import IkeProposals
from .ipsec_policies import IpsecPolicies
from .ipsec_profiles import IpsecProfiles
from .ipsec_proposals import IpsecProposals
from .l2vpns import L2vpns
from .terminations import Terminations
from .tunnel_groups import TunnelGroups
from .tunnel_terminations import TunnelTerminations
from .tunnels import Tunnels


class Vpn:
    """
    Vpn module

    Args:
        netbox: (Core) The Netbox object generated by the Client class.

    Attributes:
        ike_policies (IkePolicies): The ike_policies object.
        ike_proposals (IkeProposals): The ike_proposals object.
        ipsec_policies (IpsecPolicies): The ipsec_policies object.
        ipsec_profiles (IpsecProfiles): The ipsec_profiles object.
        ipsec_proposals (IpsecProposals): The ipsec_proposals object.
        l2vpns (L2vpns): The l2vpns object.
        terminations (Terminations): The terminations object.
        tunnel_groups (TunnelGroups): The tunnel_groups object.
        tunnel_terminations (TunnelTerminations): The tunnel_terminations object.
        tunnels (Tunnels): The tunnels object.
    """

    def __init__(self, netbox: Core):
        self.ike_policies = IkePolicies(Core(netbox, '/api/vpn/ike-policies/'))
        self.ike_proposals = IkeProposals(
            Core(netbox, '/api/vpn/ike-proposals/')
        )
        self.ipsec_policies = IpsecPolicies(
            Core(netbox, '/api/vpn/ipsec-policies/')
        )
        self.ipsec_profiles = IpsecProfiles(
            Core(netbox, '/api/vpn/ipsec-profiles/')
        )
        self.ipsec_proposals = IpsecProposals(
            Core(netbox, '/api/vpn/ipsec-proposals/')
        )
        self.tunnel_groups = TunnelGroups(
            Core(netbox, '/api/vpn/tunnel-groups/')
        )
        self.tunnel_terminations = Terminations(
            Core(netbox, '/api/vpn/tunnel-terminations/')
        )
        self.tunnels = Tunnels(Core(netbox, '/api/vpn/tunnels/'))
        self.l2vpns = L2vpns(Core(netbox, '/api/vpn/l2vpns/'))
        self.terminations = Terminations(
            Core(netbox, '/api/vpn/l2vpn-terminations/')
        )


__all__ = ['Vpn']
