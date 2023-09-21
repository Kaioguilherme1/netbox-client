
class Core:
    def __init__(self, netbox: object, endpoint: str):
        self._netbox = netbox
        self._endpoint = endpoint

    def create(self, data):
        data['slug'] = self._netbox._slug(data['name'])
        return self._netbox._request('post',f'{self._endpoint}', data)

    def get(self, id: int = None, name: str = None, tags: list = None, search: str = None , limit: int = 1000):

        self._netbox._request('get', f'{self._endpoint}?q=200.129.143.16')['results']

        if not id and name:
            id = self._netbox._get_id(name,f'{self._endpoint}')

            if id is not None:
                return self._netbox._request('get', f'{self._endpoint}?id={id}')['results'][0]
            else:
                return None


        else:
            if search:
                response = self._netbox._request('get', f'{self._endpoint}?q={search}&?limit={limit}')['results']
            else:
                response = self._netbox._request('get', f'{self._endpoint}?limit={limit}')['results']

            if tags:
                filtered_resources = []
                slug_tags = [self._netbox._slug(tag) for tag in tags]
                for item in response:
                    if item['tags']:
                        for tag in item['tags']:
                            if tag['slug'] in slug_tags:
                                filtered_resources.append(item)

                return filtered_resources
            else:
                return response

    def update(self, data):
        return self._netbox._request('put',f'{self._endpoint}', data)

    def delete(self, id: int):
        response = self._netbox._request('delete', f'{self._endpoint}{id}/')
        if response[0] != 204:
            return [False, response[0], response[1]]
        else:
            return [True,response[0],response[1]]
