from netboxcli.core import Core

from .wireless_lan_groups import WirelessLanGroups
from .wireless_lans import WirelessLans


class Wireless:
    def __init__(self, netbox):
        self.wireless_lans = WirelessLans(
            Core(netbox, '/api/wireless/wireless-lans/')
        )
        self.wireless_lan_groups = WirelessLanGroups(
            Core(netbox, '/api/wireless/wireless-lan-groups/')
        )


__all__ = ['Wireless']

list = [
    'wireless',
    [
        ['wireless_lans', 'WirelessLans'],
        ['wireless_lan_groups', 'WirelessLanGroups'],
    ],
]
