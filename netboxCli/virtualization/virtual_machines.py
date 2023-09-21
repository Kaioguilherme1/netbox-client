
class VirtualMachines:
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
        """Create a new resource using the provided data."""
        return self._core.create(data)

    def get(self, id: int = None, name: str = None, tags: list = None, search: str = None, limit: int = 1000):
        """Retrieve a resource based on ID or name."""
        return self._core.get(id, name, tags, search, limit)

    def update(self, data):
        """Update an existing resource."""
        return self._core.update(data)

    def delete(self, id: int):
        """Delete a resource based on its ID."""
        return self._core.delete(id)
