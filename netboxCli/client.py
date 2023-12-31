import requests
from .organization import Organization
from .devices import Devices
from .connections import Connections
from .wireless import Wireless
from .ipam import Ipam
from .overlay import Overlay
from .virtualization import Virtualization
from .circuits import Circuits
from .power import Power
from .provisioning import Provisioning
from .customization import Customization
from .operations import Operations


class Client:
    def __init__(self, API_IP, API_TOKEN):
        self.organization = Organization(self)
        self.devices = Devices(self)
        self.connections = Connections(self)
        self.wireless = Wireless(self)
        self.ipam = Ipam(self)
        self.overlay = Overlay(self)
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

    def _slug(self, text):
        return text.lower().replace(' ', '-')

    def _request(self, method, endpoint, data=None):
        url = f'{self._base_url}{endpoint}'
        response = requests.request(method, url, json=data, headers=self._headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f'Status {response.status_code}: {response.text}')
            return [response.status_code, response.text]

    def _get_id(self, name, endpoint):
        if name:
            data = self._request('GET', endpoint)["results"]
            filtered_data = filter(lambda d: d["name"] == str(name), data)
            ids = list(map(lambda d: d["id"], filtered_data))

            if ids:
                return ids[0]

        return None

