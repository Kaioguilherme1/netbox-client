from netboxCli.core import Core

from .config_contexts import ConfigContexts
from .config_templates import ConfigTemplates


class Provisioning:
    def __init__(self, netbox):
        self.config_contexts = ConfigContexts(Core(netbox, '/api/extras/config-contexts/'))
        self.config_templates = ConfigTemplates(Core(netbox, '/api/extras/config-templates/'))


__all__ = ['Provisioning']
