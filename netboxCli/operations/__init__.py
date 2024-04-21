from netboxcli.core import Core

from .data_sources import DataSources
from .jobs import Jobs
from .journal_entries import JournalEntries
from .webhooks import Webhooks


class Operations:
    def __init__(self, netbox):
        # Integrations
        self.data_sources = DataSources(
            Core(netbox, '/api/core/data-sources/')
        )
        self.webhooks = Webhooks(Core(netbox, '/api/extras/webhooks/'))
        # Jobs
        self.jobs = Jobs(Core(netbox, '/api/core/jobs/'))
        # logging
        self.journal_entries = JournalEntries(
            Core(netbox, '/api/extras/journal-entries/')
        )


__all__ = ['Operations']
