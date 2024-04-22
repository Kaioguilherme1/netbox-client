class Core:
    def __init__(self, netbox: object, endpoint: str):
        self._netbox = netbox
        self._endpoint = endpoint

    def create(self, data) -> dict:
        data['slug'] = self._netbox._slug(data['name'])
        response = self._netbox._request('post', f'{self._endpoint}', data)
        return response

    def get(
        self,
        id: int = None,
        name: str = None,
        tags: list = None,
        search: str = None,
        limit: int = 1000,
    ) -> dict:

        result = {'status': None, 'data': None}
        if id:
            response = self._netbox._request(
                'get', f'{self._endpoint}?id={id}'
            )
            return response

        if not id and name:
            id_name = self._netbox._get_id(name, f'{self._endpoint}')

            if id_name is not None:
                response = self._netbox._request(
                    'get', f'{self._endpoint}?id={id_name}'
                )
                return response
            else:
                result['status'] = 404
                return result

        else:
            if search:
                response = self._netbox._request(
                    'get', f'{self._endpoint}?q={search}&?limit={limit}'
                )
            else:
                response = self._netbox._request(
                    'get', f'{self._endpoint}?limit={limit}'
                )

            if tags:
                if response['status'] != 200:
                    return response

                filtered_resources = []
                slug_tags = [self._netbox._slug(tag) for tag in tags]
                for item in response['data']['results']:
                    if item['tags']:
                        for tag in item['tags']:
                            if tag['slug'] in slug_tags:
                                filtered_resources.append(item)

                return response
            else:
                return response

    def update(self, data) -> dict:
        return self._netbox._request('put', f'{self._endpoint}', data)

    def delete(self, id: int) -> dict:
        return self._netbox._request('delete', f'{self._endpoint}{id}/')
