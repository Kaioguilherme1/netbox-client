from netboxcli.core import Core

from .contact_assignments import ContactAssignments
from .contact_groups import ContactGroups
from .contact_roles import ContactRoles
from .contacts import Contacts
from .locations import Locations
from .racks import Racks
from .racks_roles import RacksRoles
from .regions import Regions
from .reservations import Reservations
from .site_groups import SiteGroups
from .sites import Sites
from .tenant_groups import TenantGroups
from .tenants import Tenants


class Organization:
    def __init__(self, netbox):
        # sites
        self.sites = Sites(Core(netbox, '/api/dcim/sites/'))
        self.regions = Regions(Core(netbox, '/api/dcim/regions/'))
        self.site_groups = SiteGroups(Core(netbox, '/api/dcim/site-groups/'))
        self.locations = Locations(Core(netbox, '/api/dcim/locations/'))
        # racks
        self.racks = Racks(Core(netbox, '/api/dcim/racks/'))
        self.racks_roles = RacksRoles(Core(netbox, '/api/dcim/rack-roles/'))
        self.reservations = Reservations(
            Core(netbox, '/api/dcim/rack-reservations/')
        )
        # Tenancy
        self.tenants = Tenants(Core(netbox, '/api/tenancy/tenants/'))
        self.tenant_groups = TenantGroups(
            Core(netbox, '/api/tenancy/tenant-groups/')
        )
        # contacts
        self.contacts = Contacts(Core(netbox, '/api/tenancy/contacts/'))
        self.contact_groups = ContactGroups(
            Core(netbox, '/api/tenancy/contact-groups/')
        )
        self.contact_roles = ContactRoles(
            Core(netbox, '/api/tenancy/contact-roles/')
        )
        self.contact_assignments = ContactAssignments(
            Core(netbox, '/api/tenancy/contact-assignments/')
        )


__all__ = ['Organization']
