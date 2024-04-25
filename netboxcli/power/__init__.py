from netboxcli.core import Core

from .power_feeds import PowerFeeds
from .power_panels import PowerPanels


class Power:
    """
    Power module

    Args:
        netbox: (Core) The Netbox object generated by the Client class.

    Attributes:
        power_feeds (PowerFeeds): The power_feeds object.
        power_panels (PowerPanels): The power_panels object.
    """

    def __init__(self, netbox: Core):

        self.power_feeds = PowerFeeds(Core(netbox, '/api/dcim/power-feeds/'))
        self.power_panels = PowerPanels(
            Core(netbox, '/api/dcim/power-panels/')
        )


__all__ = ['Power']
