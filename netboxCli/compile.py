import os

# Lista de dados de teste
api = [
    ['organization',[
        ['sites', 'Sites'],
        ['regions', 'Regions'],
        ['site_groups', 'SiteGroups'],
        ['locations', 'Locations'],
        ['racks', 'Racks'],
        ['racks_roles', 'RacksRoles'],
        ['reservations', 'Reservations'],
        ['tenants', 'Tenants'],
        ['tenant_groups', 'TenantGroups'],
        ['contacts', 'Contacts'],
        ['contact_groups', 'ContactGroups'],
        ['contact_roles', 'ContactRoles'],
        ['contact_associations', 'ContactAssociations'],
    ]],

    ['devices',[
        ['devices', 'DevicesClass'],
        ['modules', 'Modules'],
        ['devices_roles', 'DevicesRoles'],
        ['platforms', 'Platforms'],
        ['virtual_chassis', 'VirtualChassis'],
        ['virtual_chassis_contexts', 'VirtualChassisContexts'],
        ['device_types', 'DeviceTypes'],
        ['modules_types', 'ModulesTypes'],
        ['manufacturers', 'Manufacturers'],
        ['interfaces', 'Interfaces'],
        ['front_ports', 'FrontPorts'],
        ['rear_ports', 'RearPorts'],
        ['console_ports', 'ConsolePorts'],
        ['console_server_ports', 'ConsoleServerPorts'],
        ['power_ports', 'PowerPorts'],
        ['power_outlets', 'PowerOutlets'],
        ['modules_bays', 'ModulesBays'],
        ['inventory_items', 'InventoryItems'],
        ['inventory_items_roles', 'InventoryItemsRoles'],
    ]],

    ['connections',[
        ['cables', 'Cables'],
        ['wireless_links', 'WirelessLinks'],
        ['interface_connections', 'InterfaceConnections'],
        ['console_connections', 'ConsoleConnections'],
        ['power_connections', 'PowerConnections'],
    ]],

    ['wireless',[
        ['wireless_lans', 'WirelessLans'],
        ['wireless_lan_groups', 'WirelessLanGroups']
    ]],

    ['extras',[
        ['config_contexts', 'ConfigContexts'],
        ['config_templates', 'ConfigTemplates'],
        ['custom_fields', 'CustomFields'],
        ['custom_links', 'CustomLinks'],
        ['export_templates', 'ExportTemplates'],
        ['saved_filters', 'SavedFilters'],
        ['tags', 'Tags']
    ]],

    ['ipam',[
        ['ip_addresses', 'IpAddresses'],
        ['ip_ranges', 'IpRanges'],
        ['prefixes', 'Prefixes'],
        ['prefix_roles', 'PrefixRoles'],
        ['asn_ranges', 'AsnRanges'],
        ['asns', 'Asns'],
        ['aggregates', 'Aggregates'],
        ['rirs', 'Rirs'],
        ['vrfs', 'Vrfs'],
        ['router_targets', 'RouterTargets'],
        ['vlans', 'Vlans'],
        ['vlan_groups', 'VlanGroups'],
        ['fhrp_groups', 'FhrpGroups'],
        ['services_templates', 'ServicesTemplates'],
        ['services', 'Services']
    ]],

    ['virtualization',[
        ['cluster_groups', 'ClusterGroups'],
        ['cluster_types', 'ClusterTypes'],
        ['clusters', 'Clusters'],
        ['virtual_machines', 'VirtualMachines'],
        ['interfaces', 'Interfaces']
    ]],

]

# Conteúdo da classe base
class_content = '''
class {class_name}:
    """
    this class is used to create, retrieve, update, and delete resources of netbox api.

    Args:
        core (obj): Core object for create, retrieve, update, and delete actions.

    Attributes:
        core (obj): Core object for create, retrieve, update, and delete actions.

    Methods:
        create(data):
            Create a new resource using the provided data.

            Args:
                data (dict): Data to create the resource.

            Returns:
                dict: Data of the created resource.

        get(id=None, name=None, tags=None):
            Retrieve a resource based on ID or name.

            Args:
                id (int, optional): ID of the resource to retrieve.
                name (str, optional): Name of the resource to retrieve.

            Returns:
                dict: Data of the retrieved resource.

        update(data):
            Update an existing resource.

            Args:
                data (dict): Updated data for the resource.

            Returns:
                dict: Data of the resource after the update.

        delete(id):
            Delete a resource based on its ID.

            Args:
                id (int): ID of the resource to delete.

            Returns:
                bool: True if deletion is successful, False otherwise.
    """

    def __init__(self, core):
        self._core = core

    def create(self, data):
        """Create a new resource using the provided data."""
        return self._core.create(data)

    def get(self, id: int = None, name: str = None, tags: list = None, search: str = None, limit: int = 1000):
        """Retrieve a resource based on ID or name."""
        return self._core.get(id, name, tags, search, limit)

    def update(self, data):
        """Update an existing resource."""
        return self._core.update(data)

    def delete(self, id: int):
        """Delete a resource based on its ID."""
        return self._core.delete(id)
'''

for folder in api:
    folder_name = folder[0]
    class_list = folder[1]

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    for resource in class_list:
        file_name = f"{folder_name}/{resource[0]}.py"
        class_name = resource[1]

        if os.path.exists(file_name):
            print(f"Updating file '{file_name}'.")
        else:
            print(f"Creating file '{file_name}'.")

        with open(file_name, 'w') as file:
            file.write(class_content.format(class_name=class_name))

print("Process completed.")
