from netboxCli.core import Core

from .config_contexts import ConfigContexts
from .config_templates import ConfigTemplates
from .custom_fields import CustomFields
from .custom_links import CustomLinks
from .export_templates import ExportTemplates
from .saved_filters import SavedFilters
from .tags import Tags


class Extras:
    def __init__(self, netbox):
        self.config_contexts = ConfigContexts(Core(netbox, '/api/extras/config-contexts/'))
        self.config_templates = ConfigTemplates(Core(netbox, '/api/extras/config-templates/'))
        self.custom_fields = CustomFields(Core(netbox, '/api/extras/custom-fields/'))
        self.custom_links = CustomLinks(Core(netbox, '/api/extras/custom-links/'))
        self.export_templates = ExportTemplates(Core(netbox, '/api/extras/export-templates/'))
        self.saved_filters = SavedFilters(Core(netbox, '/api/extras/saved-filters/'))
        self.tags = Tags(Core(netbox, '/api/extras/tags/'))


__all__ = ['Extras']
