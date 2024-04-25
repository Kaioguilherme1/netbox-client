class_header = '''
class {class_name}:
    """
    {docstring}

    Args:
        core (obj): Core object for create, retrieve, update, and delete actions.

    """
    def __init__(self, core):
        self._core = core
'''

metods = {
    'POST': '''
    def create(self, data) -> dict:
        """
        Create a new resource in {subclass} using the provided data.
        
        Args:
            data (list or dict): Data it can be a dictionary or a list of dictionaries containing the information to create the resource.
            
        Examples:
            Create a new client:
            >>> from netboxcli import Client
            >>> nb = Client('http://localhost:8000', 'token')
            
            Create a new resource:
            >>> data = {{'name': 'resource_name'}}
            >>> result = nb.{class_main}.{subclass}.create(data)
        
        Returns:
            dict: {{'status': 200, 'data': {{'result': {subclass}]}}}}
        """
        return self._core.create(data)
    ''',
    'GET': '''
    def get(
        self,
        id: int = None,
        name: str = None,
        tags: list = None,
        search: str = None,
        limit: int = 1000,
    ) -> dict:
        """
       Get a resource from the {subclass} on ID, name, tags, or search query.
       
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
           >>> result = nb.{class_main}.{subclass}.get(id=1)
           
           Get a resource by name:
           >>> result = nb.{class_main}.{subclass}.get(name="resource_name")
           
           Get resources by tags:
           >>> result = nb.{class_main}.{subclass}.get(tags=["tag1", "tag2"])
           
           Get resources by search query:
           >>> result = nb.{class_main}.{subclass}.get(search="query")
           
           Get all resources:
           >>> result = nb.{class_main}.{subclass}.get()
           
       Returns:
           {result}
       """
        return self._core.get(id, name, tags, search, limit)
    ''',
    'PUT': '''
    def update(self, data: list) -> dict:
        """
        Update an existing resource in {subclass} with the provided data.
        
        Args:
            data (list): List of dictionaries containing the updated data for the resources.
            
        Examples:
            Create a new client:
            >>> from netboxcli import Client
            >>> nb = Client('http://localhost:8000', 'token')
            
            Update a resource by ID:
            >>> data = [{{'id': 1, 'name': 'new_name'}}]
            >>> result = nb.{class_main}.{subclass}.update(data)
        """
        return self._core.update(data)
    ''',
    'DELETE': '''
    def delete(self, id: int) -> dict:
        """
        Delete a resource based on its ID.
        
        Args:
            id (int): ID of the resource in {subclass} to delete.
        
        Examples:
            Create a new client:
            >>> from netboxcli import Client
            >>> nb = Client('http://localhost:8000', 'token')
            
            Delete a resource by ID:
            >>> result = nb.{class_main}.{subclass}.delete(id=1)
        
        Returns:
            [status_code, response]
        """
        return self._core.delete(id)
    ''',
}

# Conteúdo da classe base
class_content = '''
class {class_name}:
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
        """
        Create a new resource using the provided data.
    
        Args:
            data (dict): Data to create the resource. It should contain all the necessary information to create the resource.
    
        Returns:
            dict: Data of the created resource if successful.
                  If the creation fails or if the data is invalid, returns None.
        """
        return self._core.create(data)

    def get(self, id: int = None, name: str = None, tags: list = None, search: str = None, limit: int = 1000):
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
'''
