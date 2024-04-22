class FrontPorts:
    """
    Responsable for managing front ports of devices

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
        Get a resource from the front_ports on ID, name, tags, or search query.

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
            >>> result = nb.devices.front_ports.get(id=1)

            Get a resource by name:
            >>> result = nb.devices.front_ports.get(name="resource_name")

            Get resources by tags:
            >>> result = nb.devices.front_ports.get(tags=["tag1", "tag2"])

            Get resources by search query:
            >>> result = nb.devices.front_ports.get(search="query")

            Get all resources:
            >>> result = nb.devices.front_ports.get()

        Returns:
            Returns a list with a status code and the request data in JSON format: {status: 200, data: {result: [list of front_ports]}}
        """
        return self._core.get(id, name, tags, search, limit)

    def create(self, data) -> dict:
        """
        Create a new resource in front_ports using the provided data.

        Args:
            data (dict): Data to create the resource. It should contain all the necessary information to create the resource.

        Examples:
            Create a new client:
            >>> from netboxcli import Client
            >>> nb = Client('http://localhost:8000', 'token')

            Create a new resource:
            >>> data = {'name': 'resource_name'}
            >>> result = nb.devices.front_ports.create(data)

        Returns:
            dict: {'status': 200, 'data': {'result': front_ports]}}
        """
        return self._core.create(data)

    def update(self, data) -> dict:
        """
        Update an existing resource in front_ports with the provided data.

        Args:
            data (dict): Updated data for the resource. It should contain id and optional fields to update, to default fields find in https://demo.netbox.dev/api/ .

        Examples:
            Create a new client:
            >>> from netboxcli import Client
            >>> nb = Client('http://localhost:8000', 'token')

            Update a resource by ID:
            >>> data = {'id': 1, 'name': 'new_name'}
            >>> result = nb.devices.front_ports.update(data)
        """
        return self._core.update(data)

    def delete(self, id: int) -> dict:
        """
        Delete a resource based on its ID.

        Args:
            id (int): ID of the resource in front_ports to delete.

        Examples:
            Create a new client:
            >>> from netboxcli import Client
            >>> nb = Client('http://localhost:8000', 'token')

            Delete a resource by ID:
            >>> result = nb.devices.front_ports.delete(id=1)

        Returns:
            [status_code, response]
        """
        return self._core.delete(id)
