import requests
from .virtualization import Virtualization as vitualization
from .ipam import Ipam as ipam
from .extras import Extras as extras


class Client:
    def __init__(self, API_IP, API_TOKEN):
        self.virtualization = vitualization(self)
        self.ipam = ipam(self)
        self.extras = extras(self)

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
            print(f'Error {response.status_code}: {response.text}')
            return None

    def _get_id(self, name, endpoint):
        if name:
            data = self._request('GET', endpoint)["results"]
            filtered_data = filter(lambda d: d["name"] == str(name), data)
            ids = list(map(lambda d: d["id"], filtered_data))

            if ids:
                return ids[0]

        return None

