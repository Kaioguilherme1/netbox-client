class ContactGroups:
    """
    this class is used to create, retrieve, update, and delete resources of netbox api.

    Args:
        core (obj): Core object for create, retrieve, update, and delete actions.

    Attributes:
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
    ):
        """
        Retrieve a resource from the NetBox API based on ID, name, tags, or search query.

        Args:
            id (int, optional): The ID of the resource to retrieve.
            name (str, optional): The name of the resource to retrieve.
            tags (list, optional): List of tags to filter resources.
            search (str, optional): Search query to filter resources.
            limit (int, optional): Maximum number of results to return. Defaults to 1000.

        Returns:
            dict or list: If a single resource is found, returns a dictionary containing the data of the retrieved resource.
                         If multiple resources are found, returns a list of dictionaries containing the data of the retrieved resources.
                         If no resources are found, returns an empty list.
        """
        return self._core.get(id, name, tags, search, limit)

    def create(self, data):
        """
        Create a new resource using the provided data.

        Args:
            data (dict): Data to create the resource. It should contain all the necessary information to create the resource.

        Returns:
            dict: Data of the created resource if successful.
                  If the creation fails or if the data is invalid, returns None.
        """
        return self._core.create(data)

    def update(self, data):
        """
        Update an existing resource with the provided data.

        Args:
            data (dict): Updated data for the resource. It should contain all the necessary information to update the resource.

        Returns:
            dict: Data of the resource after the update if successful.
                  If the update fails or if the data is invalid, returns None.
        """
        return self._core.update(data)

    def delete(self, id: int):
        """
        Delete a resource based on its ID.

        Args:
            id (int): ID of the resource to delete.

        Returns:
            bool: True if deletion is successful, False otherwise.
        """
        return self._core.delete(id)
