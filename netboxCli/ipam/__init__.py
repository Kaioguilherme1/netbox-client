from netboxCli.core import Core

from .ip_addresses import IpAddresses
from .ip_ranges import IpRanges
from .prefixes import Prefixes
from .prefix_roles import PrefixRoles
from .asn_ranges import AsnRanges
from .asns import Asns
from .aggregates import Aggregates
from .rirs import Rirs
from .vrfs import Vrfs
from .router_targets import RouterTargets
from .vlans import Vlans
from .vlan_groups import VlanGroups
from .fhrp_groups import FhrpGroups
from .services_templates import ServicesTemplates
from .services import Services

class Ipam:
    def __init__(self, netbox):
        self.ip_addresses = IpAddresses(Core(netbox, '/api/ipam/ip-addresses/'))
        self.ip_ranges = IpRanges(Core(netbox, '/api/ipam/ip-ranges/'))

        self.prefixes = Prefixes(Core(netbox, '/api/ipam/prefixes/'))
        self.prefix_roles = PrefixRoles(Core(netbox, '/api/ipam/roles/'))

        self.asn_ranges = AsnRanges(Core(netbox, '/api/ipam/asn-ranges/'))
        self.asns = Asns(Core(netbox, '/api/ipam/asns/'))

        self.aggregates = Aggregates(Core(netbox, '/api/ipam/aggregates/'))
        self.rirs = Rirs(Core(netbox, '/api/ipam/rirs/'))

        self.vrfs = Vrfs(Core(netbox, '/api/ipam/vrfs/'))
        self.router_targets = RouterTargets(Core(netbox, '/api/ipam/router-targets/'))

        self.vlans = Vlans(Core(netbox, '/api/ipam/vlans/'))
        self.vlan_groups = VlanGroups(Core(netbox, '/api/ipam/vlan-groups/'))

        self.fhrp_groups = FhrpGroups(Core(netbox, '/api/ipam/fhrp-groups/'))
        self.services_templates = ServicesTemplates(Core(netbox, '/api/ipam/services-templates/'))
        self.services = Services(Core(netbox, '/api/ipam/services/'))


__all__ = ['Ipam']


