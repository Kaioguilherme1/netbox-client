
class Core:
    def __init__(self, netbox: object, endpoint: str):
        self._netbox = netbox
        self._endpoint = endpoint

    def create(self, data):
        data['slug'] = self._netbox._slug(data['name'])
        return self._netbox._request('post',f'{self._endpoint}', data)

    def get(self, id: int = None, name: str = None):
        if not id and name:
            id = self._netbox._get_id(name,f'{self._endpoint}')

            if id is not None:
                return self._netbox._request('get', f'{self._endpoint}?id={id}')['results'][0]
            else:
                return None
        else:
            return self._netbox._request('get', f'{self._endpoint}')['results']

    def update(self, data):
        return self._netbox._request('put',f'{self._endpoint}', data)

    def delete(self, id: int):
        return self._netbox._request('delete', f'{self._endpoint}{id}/')
