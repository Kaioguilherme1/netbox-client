class ProviderNetworks:
    """
    Responsible for managing provider networks

    Args:
        core (obj): Core object for create, retrieve, update, and delete actions.

    """

    def __init__(self, core):
        self._core = core

    def get(
        self,
        id: int = None,
        name: str = None,
        tags: list = None,
        search: str = None,
        limit: int = 1000,
    ) -> dict:
        """
        Get a resource from the provider_networks on ID, name, tags, or search query.

        Args:
            id (int, optional): The ID of the resource to retrieve.
            name (str, optional): The name of the resource to retrieve.
            tags (list, optional): List of tags to filter resources.
            search (str, optional): Search query to filter resources.
            limit (int, optional): Maximum number of results to return. Defaults to 1000.

        Examples:
            Create a new client:
            >>> from netboxcli import Client
            >>> nb = Client('http://localhost:8000', 'token')

            Get a resource by ID:
            >>> result = nb.circuits.provider_networks.get(id=1)

            Get a resource by name:
            >>> result = nb.circuits.provider_networks.get(name="resource_name")

            Get resources by tags:
            >>> result = nb.circuits.provider_networks.get(tags=["tag1", "tag2"])

            Get resources by search query:
            >>> result = nb.circuits.provider_networks.get(search="query")

            Get all resources:
            >>> result = nb.circuits.provider_networks.get()

        Returns:
            Returns a list with a status code and the request data in JSON format: {status: 200, data: {result: [list of provider_networks]}}
        """
        return self._core.get(id, name, tags, search, limit)

    def create(self, data) -> dict:
        """
        Create a new resource in provider_networks using the provided data.

        Args:
            data (dict): Data to create the resource. It should contain all the necessary information to create the resource.

        Examples:
            Create a new client:
            >>> from netboxcli import Client
            >>> nb = Client('http://localhost:8000', 'token')

            Create a new resource:
            >>> data = {'name': 'resource_name'}
            >>> result = nb.circuits.provider_networks.create(data)

        Returns:
            dict: {'status': 200, 'data': {'result': provider_networks]}}
        """
        return self._core.create(data)

    def update(self, data) -> dict:
        """
        Update an existing resource in provider_networks with the provided data.

        Args:
            data (dict): Updated data for the resource. It should contain id and optional fields to update, to default fields find in https://demo.netbox.dev/api/ .

        Examples:
            Create a new client:
            >>> from netboxcli import Client
            >>> nb = Client('http://localhost:8000', 'token')

            Update a resource by ID:
            >>> data = {'id': 1, 'name': 'new_name'}
            >>> result = nb.circuits.provider_networks.update(data)
        """
        return self._core.update(data)

    def delete(self, id: int) -> dict:
        """
        Delete a resource based on its ID.

        Args:
            id (int): ID of the resource in provider_networks to delete.

        Examples:
            Create a new client:
            >>> from netboxcli import Client
            >>> nb = Client('http://localhost:8000', 'token')

            Delete a resource by ID:
            >>> result = nb.circuits.provider_networks.delete(id=1)

        Returns:
            [status_code, response]
        """
        return self._core.delete(id)
