from netboxCli.core import Core
from .power_feeds import PowerFeeds
from .power_panels import PowerPanels

class Power:
    def __init__(self, netbox):
        self.power_feeds = PowerFeeds(Core(netbox, '/api/dcim/power-feeds/'))
        self.power_panels = PowerPanels(Core(netbox, '/api/dcim/power-panels/'))

__all__ = ['Power']
