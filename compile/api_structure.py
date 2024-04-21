# Lista de dados de teste
api = [
    [
        'organization',
        [
            ['sites', 'Sites', ['GET', 'POST', 'PUT', 'DELETE']],
            ['regions', 'Regions', ['GET', 'POST', 'PUT', 'DELETE']],
            ['site_groups', 'SiteGroups', ['GET', 'POST', 'PUT', 'DELETE']],
            ['locations', 'Locations', ['GET', 'POST', 'PUT', 'DELETE']],
            ['racks', 'Racks', ['GET', 'POST', 'PUT', 'DELETE']],
            ['racks_roles', 'RacksRoles', ['GET', 'POST', 'PUT', 'DELETE']],
            ['reservations', 'Reservations', ['GET', 'POST', 'PUT', 'DELETE']],
            ['tenants', 'Tenants', ['GET', 'POST', 'PUT', 'DELETE']],
            [
                'tenant_groups',
                'TenantGroups',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
            ['contacts', 'Contacts', ['GET', 'POST', 'PUT', 'DELETE']],
            [
                'contact_groups',
                'ContactGroups',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
            [
                'contact_roles',
                'ContactRoles',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
            [
                'contact_assignment',
                'ContactAssignment',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
        ],
    ],
    [
        'devices',
        [
            ['devices', 'DevicesClass', ['GET', 'POST', 'PUT', 'DELETE']],
            ['modules', 'Modules', ['GET', 'POST', 'PUT', 'DELETE']],
            [
                'devices_roles',
                'DevicesRoles',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
            ['platforms', 'Platforms', ['GET', 'POST', 'PUT', 'DELETE']],
            [
                'virtual_chassis',
                'VirtualChassis',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
            [
                'virtual_chassis_contexts',
                'VirtualChassisContexts',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
            ['device_types', 'DeviceTypes', ['GET', 'POST', 'PUT', 'DELETE']],
            [
                'modules_types',
                'ModulesTypes',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
            [
                'manufacturers',
                'Manufacturers',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
            ['interfaces', 'Interfaces', ['GET', 'POST', 'PUT', 'DELETE']],
            ['front_ports', 'FrontPorts', ['GET', 'POST', 'PUT', 'DELETE']],
            ['rear_ports', 'RearPorts', ['GET', 'POST', 'PUT', 'DELETE']],
            [
                'console_ports',
                'ConsolePorts',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
            [
                'console_server_ports',
                'ConsoleServerPorts',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
            ['power_ports', 'PowerPorts', ['GET', 'POST', 'PUT', 'DELETE']],
            [
                'power_outlets',
                'PowerOutlets',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
            ['modules_bays', 'ModulesBays', ['GET', 'POST', 'PUT', 'DELETE']],
            [
                'inventory_items',
                'InventoryItems',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
            [
                'inventory_items_roles',
                'InventoryItemsRoles',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
        ],
    ],
    [
        'connections',
        [
            ['cables', 'Cables', ['GET', 'POST', 'PUT', 'DELETE']],
            [
                'wireless_links',
                'WirelessLinks',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
            [
                'interface_connections',
                'InterfaceConnections',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
        ],
    ],
    [
        'wireless',
        [
            [
                'wireless_lans',
                'WirelessLans',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
            [
                'wireless_lan_groups',
                'WirelessLanGroups',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
        ],
    ],
    [
        'ipam',
        [
            ['ip_addresses', 'IpAddresses', ['GET', 'POST', 'PUT', 'DELETE']],
            ['ip_ranges', 'IpRanges', ['GET', 'POST', 'PUT', 'DELETE']],
            ['prefixes', 'Prefixes', ['GET', 'POST', 'PUT', 'DELETE']],
            ['prefix_roles', 'PrefixRoles', ['GET', 'POST', 'PUT', 'DELETE']],
            ['asn_ranges', 'AsnRanges', ['GET', 'POST', 'PUT', 'DELETE']],
            ['asns', 'Asns', ['GET', 'POST', 'PUT', 'DELETE']],
            ['aggregates', 'Aggregates', ['GET', 'POST', 'PUT', 'DELETE']],
            ['rirs', 'Rirs', ['GET', 'POST', 'PUT', 'DELETE']],
            ['vrfs', 'Vrfs', ['GET', 'POST', 'PUT', 'DELETE']],
            [
                'router_targets',
                'RouterTargets',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
            ['vlans', 'Vlans', ['GET', 'POST', 'PUT', 'DELETE']],
            ['vlan_groups', 'VlanGroups', ['GET', 'POST', 'PUT', 'DELETE']],
            ['fhrp_groups', 'FhrpGroups', ['GET', 'POST', 'PUT', 'DELETE']],
            [
                'services_templates',
                'ServicesTemplates',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
            ['services', 'Services', ['GET', 'POST', 'PUT', 'DELETE']],
        ],
    ],
    [
        'vpn',
        [
            ['tunnels', 'Tunnels', ['GET', 'POST', 'PUT', 'DELETE']],
            [
                'tunnel_terminations',
                'TunnelTerminations',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
            ['tunnel_grups', 'TunnelGrups', ['GET', 'POST', 'PUT', 'DELETE']],
            ['l2vpns', 'L2vpns', ['GET', 'POST', 'PUT', 'DELETE']],
            ['terminations', 'Terminations', ['GET', 'POST', 'PUT', 'DELETE']],
            ['ike_policies', 'IkePolicies', ['GET', 'POST', 'PUT', 'DELETE']],
            [
                'ike_proposals',
                'IkeProposals',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
            [
                'ipsec_policies',
                'IpsecPolicies',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
            [
                'ipsec_profiles',
                'IpsecProfiles',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
            [
                'ipsec_proposals',
                'IpsecProposals',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
        ],
    ],
    [
        'virtualization',
        [
            [
                'cluster_groups',
                'ClusterGroups',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
            [
                'cluster_types',
                'ClusterTypes',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
            ['clusters', 'Clusters', ['GET', 'POST', 'PUT', 'DELETE']],
            [
                'virtual_machines',
                'VirtualMachines',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
            ['interfaces', 'Interfaces', ['GET', 'POST', 'PUT', 'DELETE']],
        ],
    ],
    [
        'Circuits',
        [
            ['circuits', 'CircuitsClass', ['GET', 'POST', 'PUT', 'DELETE']],
            [
                'circuit_types',
                'CircuitTypes',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
            ['providers', 'Providers', ['GET', 'POST', 'PUT', 'DELETE']],
            [
                'provider_accounts',
                'ProviderAccounts',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
            [
                'provider_networks',
                'ProviderNetworks',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
        ],
    ],
    [
        'power',
        [
            ['power_feeds', 'PowerFeeds', ['GET', 'POST', 'PUT', 'DELETE']],
            ['power_panels', 'PowerPanels', ['GET', 'POST', 'PUT', 'DELETE']],
        ],
    ],
    [
        'Provisioning',
        [
            [
                'config_contexts',
                'ConfigContexts',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
            [
                'config_templates',
                'ConfigTemplates',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
        ],
    ],
    [
        'Customization',
        [
            [
                'custom_fields',
                'CustomFields',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
            ['custom_links', 'CustomLinks', ['GET', 'POST', 'PUT', 'DELETE']],
            [
                'export_templates',
                'ExportTemplates',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
            [
                'saved_filters',
                'SavedFilters',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
            ['tags', 'Tags', ['GET', 'POST', 'PUT', 'DELETE']],
            [
                'image_attachments',
                'ImageAttachments',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
            ['reports', 'Reports', ['GET', 'POST', 'PUT', 'DELETE']],
            ['scripts', 'Scripts', ['GET', 'POST', 'PUT', 'DELETE']],
        ],
    ],
    [
        'Operations',
        [
            ['data_sources', 'DataSources', ['GET', 'POST', 'PUT', 'DELETE']],
            ['webhooks', 'Webhooks', ['GET', 'POST', 'PUT', 'DELETE']],
            ['jobs', 'Jobs', ['GET', 'POST', 'PUT', 'DELETE']],
            [
                'journal_entries',
                'JournalEntries',
                ['GET', 'POST', 'PUT', 'DELETE'],
            ],
        ],
    ],
]


class_header = '''
class {class_name}:
    """
    this class is used to create, retrieve, update, and delete resources of netbox api.

    Args:
        core (obj): Core object for create, retrieve, update, and delete actions.

    Attributes:
        core (obj): Core object for create, retrieve, update, and delete actions.
    """
    
    def __init__(self, core):
        self._core = core
'''

metods = {
    'POST': '''
    def create(self, data):
        """
        Create a new resource using the provided data.
    
        Args:
            data (dict): Data to create the resource. It should contain all the necessary information to create the resource.
    
        Returns:
            dict: Data of the created resource if successful.
                  If the creation fails or if the data is invalid, returns None.
        """
        return self._core.create(data)
    ''',
    'GET': '''
    def get(self, id: int = None, name: str = None, tags: list = None, search: str = None, limit: int = 1000):
        """
       Retrieve a resource from the NetBox API based on ID, name, tags, or search query.
    
       Args:
           id (int, optional): The ID of the resource to retrieve.
           name (str, optional): The name of the resource to retrieve.
           tags (list, optional): List of tags to filter resources.
           search (str, optional): Search query to filter resources.
           limit (int, optional): Maximum number of results to return. Defaults to 1000.
    
       Returns:
           dict or list: If a single resource is found, returns a dictionary containing the data of the retrieved resource.
                        If multiple resources are found, returns a list of dictionaries containing the data of the retrieved resources.
                        If no resources are found, returns an empty list.
       """
        return self._core.get(id, name, tags, search, limit)
    ''',
    'PUT': '''
    def update(self, data):
        """
        Update an existing resource with the provided data.
    
        Args:
            data (dict): Updated data for the resource. It should contain all the necessary information to update the resource.
    
        Returns:
            dict: Data of the resource after the update if successful.
                  If the update fails or if the data is invalid, returns None.
        """
        return self._core.update(data)
    ''',
    'DELETE': '''
    def delete(self, id: int):
        """
        Delete a resource based on its ID.
    
        Args:
            id (int): ID of the resource to delete.
    
        Returns:
            bool: True if deletion is successful, False otherwise.
        """
        return self._core.delete(id)
    ''',
}

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
        """
        Create a new resource using the provided data.
    
        Args:
            data (dict): Data to create the resource. It should contain all the necessary information to create the resource.
    
        Returns:
            dict: Data of the created resource if successful.
                  If the creation fails or if the data is invalid, returns None.
        """
        return self._core.create(data)

    def get(self, id: int = None, name: str = None, tags: list = None, search: str = None, limit: int = 1000):
        """
       Retrieve a resource from the NetBox API based on ID, name, tags, or search query.
    
       Args:
           id (int, optional): The ID of the resource to retrieve.
           name (str, optional): The name of the resource to retrieve.
           tags (list, optional): List of tags to filter resources.
           search (str, optional): Search query to filter resources.
           limit (int, optional): Maximum number of results to return. Defaults to 1000.
    
       Returns:
           dict or list: If a single resource is found, returns a dictionary containing the data of the retrieved resource.
                        If multiple resources are found, returns a list of dictionaries containing the data of the retrieved resources.
                        If no resources are found, returns an empty list.
       """
        return self._core.get(id, name, tags, search, limit)

    def update(self, data):
        """
        Update an existing resource with the provided data.
    
        Args:
            data (dict): Updated data for the resource. It should contain all the necessary information to update the resource.
    
        Returns:
            dict: Data of the resource after the update if successful.
                  If the update fails or if the data is invalid, returns None.
        """
        return self._core.update(data)

    def delete(self, id: int):
        """
        Delete a resource based on its ID.
    
        Args:
            id (int): ID of the resource to delete.
    
        Returns:
            bool: True if deletion is successful, False otherwise.
        """
        return self._core.delete(id)
'''
