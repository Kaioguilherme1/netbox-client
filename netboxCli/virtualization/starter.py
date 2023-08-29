# Lista de dados de teste
teste = [
    ['vms', 'Vms'],
    ['interfaces', 'Interfaces'],
    ['clusters', 'Clusters'],
    ['cluster_types', 'ClusterTypes'],
    ['cluster_groups', 'ClusterGroups'],
]

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

        get(id=None, name=None):
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

    def get(self, id: int = None, name: str = None):
        """Retrieve a resource based on ID or name."""
        return self._core.get(id, name)

    def update(self, data):
        """Update an existing resource."""
        return self._core.update(data)

    def delete(self, id: int):
        """Delete a resource based on its ID."""
        return self._core.delete(id)
'''

# Criar arquivos .py com classes
for item in teste:
    filename = f"{item[0]}.py"
    class_name = item[1]

    with open(filename, 'w') as file:
        file.write(class_content.format(class_name=class_name))

    print(f"Arquivo '{filename}' criado com a classe '{class_name}'.")

print("Processo concluído.")
