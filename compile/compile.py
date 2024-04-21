import json
import os

from api_structure import api, class_header, metods


def read_specs() -> list:
    specs = []
    for folder in os.listdir('./specs'):
        with open(f'./specs/{folder}', 'r') as file:
            specs.append(json.load(file))

    return specs


def code():
    root_path = '../netboxcli'

    for folder in api:
        folder_name = folder[0]
        class_list = folder[1]
        metdos_list = folder[1][0][2]
        class_content = class_header
        for metod in metdos_list:
            class_content += metods[metod]

        if not os.path.exists(f'{root_path}/{folder_name}'):
            os.makedirs(f'{root_path}/{folder_name}')

        for resource in class_list:
            file_name = f'{root_path}/{folder_name}/{resource[0]}.py'
            class_name = resource[1]

            if os.path.exists(file_name):
                print(f"Updating file '{file_name}'.")
            else:
                print(f"Creating file '{file_name}'.")

            with open(file_name, 'w') as file:
                file.write(class_content.format(class_name=class_name))


def docs():
    root_path = '../docs/api'
    specs = read_specs()
    for folder in api:
        folder_name = folder[0]
        class_list = folder[1]

        if not os.path.exists(f'{root_path}/{folder_name}'):
            os.makedirs(f'{root_path}/{folder_name}')

        for resource in class_list:
            file_name = f'{root_path}/{folder_name}/{resource[0]}.md'
            class_name = resource[0]
            # deixa a primeira letra em minusculo
            folder_name = folder_name.lower()
            content = f'::: {folder_name}.{class_name}'
            print(content)
            if os.path.exists(file_name):
                print(f"Updating file '{file_name}'.")
            else:
                print(f"Creating file '{file_name}'.")

            with open(file_name, 'w') as file:
                file.write(content)


code()
docs()
print('Process completed.')
