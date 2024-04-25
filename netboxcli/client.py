import requests

from .circuits import Circuits
from .connections import Connections
from .customization import Customization
from .devices import Devices
from .ipam import Ipam
from .operations import Operations
from .organization import Organization
from .power import Power
from .provisioning import Provisioning
from .virtualization import Virtualization
from .vpn import Vpn
from .wireless import Wireless


class Client:
    """
    Netbox API client to interact with the Netbox API, main class to interact other classes,
    this class is responsible for the authentication and the base URL to interact with the API.

    Args:
        API_IP (str): The IP address of the Netbox API.
        API_TOKEN (str): The token to authenticate with the Netbox API.

    Examples:
        >>> from netboxcli import Client
        >>> client = Client('http://localhost:8000','9437417491269694621969126946')

    Attributes:
        organization (Organization): The organization object.
        devices (Devices): The devices object.
        connections (Connections): The connections object.
        wireless (Wireless): The wireless object.
        ipam (Ipam): The ipam object.
        vpn (Vpn): The vpn object.
        virtualization (Virtualization): The virtualization object.
        circuits (Circuits): The circuits object.
        power (Power): The power object.
        provisioning (Provisioning): The provisioning object.
        customization (Customization): The customization object.
        operations (Operations): The operations object.
    """

    def __init__(self, API_IP: str, API_TOKEN: str):
        self.organization = Organization(self)
        self.devices = Devices(self)
        self.connections = Connections(self)
        self.wireless = Wireless(self)
        self.ipam = Ipam(self)
        self.vpn = Vpn(self)
        self.virtualization = Virtualization(self)
        self.circuits = Circuits(self)
        self.power = Power(self)
        self.provisioning = Provisioning(self)
        self.customization = Customization(self)
        self.operations = Operations(self)

        self._base_url = API_IP
        self._token = API_TOKEN
        self._headers = {
            'Authorization': f'Token {self._token}',
            'Content-Type': 'application/json',
        }

    def _slug(self, text) -> str:
        """
        Convert a text to a slug format.

        Args:
            text (str): The text to be converted to a slug format.

        Returns:
            str: The text in a slug format.
        """
        return text.lower().replace(' ', '-')

    def _request(self, method, endpoint, data=None) -> dict:
        """
        Make a request to the Netbox API.

        Args:
            method (str): The HTTP method to be used in the request.
            endpoint (str): The endpoint to interact with in Netbox.
            data (dict): The data to be sent in the request.

        Returns:
            dict: Returns a dictionary with the status code and the request data in JSON format: {status: 200, data: {respondse}}
        """
        url = f'{self._base_url}{endpoint}'
        result = {
            'status': None,
            'data': None,
        }
        try:
            response = requests.request(
                method, url, json=data, headers=self._headers
            )
        except requests.exceptions.RequestException as e:
            result['status'] = 0
            result['data'] = e
            return result

        result['status'] = response.status_code
        if response.status_code == 200:

            result['data'] = response.json()
        else:
            result['data'] = response.text

        return result

    def _get_id(self, name: str, endpoint: str) -> int:
        """
        Get the ID of an object in Netbox by its name.

        Args:
            name (str): The name of the object to get the ID.
            endpoint (str): The endpoint to interact with in Netbox.

        Returns:
            int: The ID of the object in Netbox.
        """
        if name:
            result = self._request('GET', endpoint)
            status = result['status']
            data = result['data']

            if status != 200:
                # Trate o erro de forma adequada
                return None

            results = data.get('results', [])
            filtered_data = filter(lambda d: d['name'] == name, results)
            ids = [d['id'] for d in filtered_data]
            if ids:
                return ids[0]

        return None
