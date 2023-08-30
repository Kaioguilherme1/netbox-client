from netboxCli.core import Core

from .virtual_machines import VirtualMachines
from .interfaces import Interfaces
from .clusters import Clusters
from .cluster_types import ClusterTypes
from .cluster_groups import ClusterGroups



class Virtualization:
    """
    Class for managing virtualization-related resources.

    Args:
        netbox (obj): Netbox API instance.

    Attributes:
        vms (Vms): Instance of the Vms class for managing virtual machines.
        interfaces (Interfaces): Instance of the Interfaces class for managing interfaces.
        clusters (Clusters): Instance of the Clusters class for managing clusters.
        cluster_types (ClusterTypes): Instance of the ClusterTypes class for managing cluster types.
        cluster_groups (ClusterGroups): Instance of the ClusterGroups class for managing cluster groups.
    """
    def __init__(self, netbox):
        """
        Initialize Virtualization class with Netbox API instance.

        Args:
            netbox (obj): Netbox API instance.
        """
        self.virtual_machines = VirtualMachines(Core(netbox, '/api/virtualization/virtual-machines/'))
        self.interfaces = Interfaces(Core(netbox, '/api/virtualization/interfaces/'))
        self.clusters = Clusters(Core(netbox, '/api/virtualization/clusters/'))
        self.cluster_types = ClusterTypes(Core(netbox, '/api/virtualization/cluster-types/'))
        self.cluster_groups = ClusterGroups(Core(netbox, '/api/virtualization/cluster-groups/'))


__all__ = ['Virtualization']
