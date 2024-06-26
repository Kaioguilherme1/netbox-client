from netboxcli.core import Core

from .cables import Cables
from .wireless_links import WirelessLinks

# from .interface_connections import InterfaceConnections
# from .console_connections import ConsoleConnections
# from .power_connections import PowerConnections


class Connections:
    """
    Connections module

    Args:
        netbox: (Core) The Netbox object generated by the Client class.

    Attributes:
        cables (Cables): The cables object.
        wireless_links (WirelessLinks): The wireless_links object.
    """

    def __init__(self, netbox: Core):
        self.cables = Cables(Core(netbox, '/api/dcim/cables/'))
        self.wireless_links = WirelessLinks(
            Core(netbox, '/api/wireless/wireless-links/')
        )
        # self.interface_connections = InterfaceConnections(Core(netbox, '/api/dcim/interfaces/'))
        # self.console_connections = ConsoleConnections(Core(netbox, '/api/dcim/console-connections/'))
        # self.power_connections = PowerConnections(Core(netbox, '/api/dcim/power-connections/'))


__all__ = ['Connections']
