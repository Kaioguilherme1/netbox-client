from netboxCli.core import Core
from .devices import DevicesClass
from .modules import Modules
from .devices_roles import DevicesRoles
from .platforms import Platforms
from .virtual_chassis import VirtualChassis
from .virtual_chassis_contexts import VirtualChassisContexts
from .device_types import DeviceTypes
from .modules_types import ModulesTypes
from .manufacturers import Manufacturers
from .interfaces import Interfaces
from .front_ports import FrontPorts
from .rear_ports import RearPorts
from .console_ports import ConsolePorts
from .console_server_ports import ConsoleServerPorts
from .power_ports import PowerPorts
from .power_outlets import PowerOutlets
from .modules_bays import ModulesBays
from .inventory_items import InventoryItems
from .inventory_items_roles import InventoryItemsRoles

class Devices:

    def __init__(self, netbox):
        #Devices
        self.devices = DevicesClass(Core(netbox, '/api/dcim/devices/'))
        self.modules = Modules(Core(netbox, '/api/dcim/modules/'))
        self.devices_roles = DevicesRoles(Core(netbox, '/api/dcim/device-roles/'))
        self.platforms = Platforms(Core(netbox, '/api/dcim/platforms/'))
        self.virtual_chassis = VirtualChassis(Core(netbox, '/api/dcim/virtual-chassis/'))
        self.virtual_chassis_contexts = VirtualChassisContexts(Core(netbox, '/api/dcim/virtual-chassis-contexts/'))
        #Devices types
        self.device_types = DeviceTypes(Core(netbox, '/api/dcim/device-types/'))
        self.modules_types = ModulesTypes(Core(netbox, '/api/dcim/module-types/'))
        self.manufacturers = Manufacturers(Core(netbox, '/api/dcim/manufacturers/'))
        #Devices Components
        self.interfaces = Interfaces(Core(netbox, '/api/dcim/interfaces/'))
        self.front_ports = FrontPorts(Core(netbox, '/api/dcim/front-ports/'))
        self.rear_ports = RearPorts(Core(netbox, '/api/dcim/rear-ports/'))
        self.console_ports = ConsolePorts(Core(netbox, '/api/dcim/console-ports/'))
        self.console_server_ports = ConsoleServerPorts(Core(netbox, '/api/dcim/console-server-ports/'))
        self.power_ports = PowerPorts(Core(netbox, '/api/dcim/power-ports/'))
        self.power_outlets = PowerOutlets(Core(netbox, '/api/dcim/power-outlets/'))
        self.modules_bays = ModulesBays(Core(netbox, '/api/dcim/device-bays/'))
        self.inventory_items = InventoryItems(Core(netbox, '/api/dcim/inventory-items/'))
        self.inventory_items_roles = InventoryItemsRoles(Core(netbox, '/api/dcim/inventory-items-roles/'))

__all__ = ['Devices']

