# converte api structure em arquivos json

import json
import os

from api_structure import api, class_header, metods


def printjson(data):
    print(json.dumps(data, indent=4))


# converte cada item da lista primatia api em um arquivo json
def convert():
    for folder in api:
        json_name = folder[0]
        # converte a lista em um dicionario para ser convertido em json
        json_data = {}
        json_data[json_name] = []
        for resource in folder[1]:
            json_data[json_name].append(
                {
                    'name': resource[0],
                    'class': resource[1],
                    'methods': resource[2],
                }
            )
        if not os.path.exists('./specs'):
            os.makedirs('./specs')

        with open(f'./specs/{json_name}.json', 'w') as file:
            file.write(json.dumps(json_data, indent=4))


convert()
