from netboxCli.core import Core

from .custom_fields import CustomFields
from .custom_links import CustomLinks
from .export_templates import ExportTemplates
from .saved_filters import SavedFilters
from .tags import Tags
from .image_attachments import ImageAttachments
from .reports import Reports
from .scripts import Scripts


class Customization:
    def __init__(self, netbox):
        # Customization
        self.custom_fields = CustomFields(Core(netbox, '/api/extras/custom-fields/'))
        self.custom_links = CustomLinks(Core(netbox, '/api/extras/custom-links/'))
        self.export_templates = ExportTemplates(Core(netbox, '/api/extras/export-templates/'))
        self.saved_filters = SavedFilters(Core(netbox, '/api/extras/saved-filters/'))
        self.tags = Tags(Core(netbox, '/api/extras/tags/'))
        self.image_attachments = ImageAttachments(Core(netbox, '/api/extras/image-attachments/'))
        # Reports & Scripts
        self.reports = Reports(Core(netbox, '/api/extras/reports/'))
        self.scripts = Scripts(Core(netbox, '/api/extras/scripts/'))


__all__ = ['Customization']
