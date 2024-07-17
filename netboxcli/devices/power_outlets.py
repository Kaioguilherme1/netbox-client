class PowerOutlets:
    """
    Responsable for managing power outlets

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
        filter: str = None,
        limit: int = 1000,
    ) -> dict:
        """
        Get a resource from the power_outlets on ID, name, tags, or search query.

        Args:
            id (int, optional): The ID of the resource to retrieve.
            name (str, optional): The name of the resource to retrieve.
            tags (list, optional): List of tags to filter resources.
            search (str, optional): Search query to filter resources.
            filter (str, optional): Filter query especified by the user in to filter resources.
            limit (int, optional): Maximum number of results to return. Defaults to 1000.

        Examples:
            Create a new client:
            >>> from netboxcli import Client
            >>> nb = Client('http://localhost:8000', 'token')

            Get a resource by ID:
            >>> result = nb.devices.power_outlets.get(id=1)

            Get a resource by name:
            >>> result = nb.devices.power_outlets.get(name="resource_name")

            Get resources by tags:
            >>> result = nb.devices.power_outlets.get(tags=["tag1", "tag2"])

            Get resources by search query:
            >>> result = nb.devices.power_outlets.get(search="query")

            Get resources by filter query:
               >>> result = nb.devices.power_outlets.get(filter="assigned_to_interface=True")

            Get all resources:
            >>> result = nb.devices.power_outlets.get()

        Returns:
            Returns a list with a status code and the request data in JSON format: {status: 200, data: {result: [list of power_outlets]}}
        """
        return self._core.get(id, name, tags, search, limit)

    def create(self, data) -> dict:
        """
        Create a new resource in power_outlets using the provided data.

        Args:
            data (list or dict): Data it can be a dictionary or a list of dictionaries containing the information to create the resource.

        Examples:
            Create a new client:
            >>> from netboxcli import Client
            >>> nb = Client('http://localhost:8000', 'token')

            Create a new resource:
            >>> data = {'name': 'resource_name'}
            >>> result = nb.devices.power_outlets.create(data)

        Returns:
            dict: {'status': 200, 'data': {'result': power_outlets]}}
        """
        return self._core.create(data)

    def update(self, data: list) -> dict:
        """
        Update an existing resource in power_outlets with the provided data.

        Args:
            data (list): List of dictionaries containing the updated data for the resources.

        Examples:
            Create a new client:
            >>> from netboxcli import Client
            >>> nb = Client('http://localhost:8000', 'token')

            Update a resource by ID:
            >>> data = [{'id': 1, 'name': 'new_name'}]
            >>> result = nb.devices.power_outlets.update(data)
        """
        return self._core.update(data)

    def delete(self, id: int) -> dict:
        """
        Delete a resource based on its ID.

        Args:
            id (int): ID of the resource in power_outlets to delete.

        Examples:
            Create a new client:
            >>> from netboxcli import Client
            >>> nb = Client('http://localhost:8000', 'token')

            Delete a resource by ID:
            >>> result = nb.devices.power_outlets.delete(id=1)

        Returns:
            [status_code, response]
        """
        return self._core.delete(id)
