import json
import os

from api_structure import class_header, metods


def read_specs() -> list:
    specs = []
    for folder in os.listdir('./specs'):
        with open(f'./specs/{folder}', 'r') as file:
            specs.append(json.load(file))

    return specs


def code():
    root_path = '../netboxcli'
    class_list = read_specs()
    for folder in class_list:
        folder_name = folder['Class_name']
        class_list = folder['sub_classes']
        class_content = class_header
        if not os.path.exists(f'{root_path}/{folder_name}'):
            os.makedirs(f'{root_path}/{folder_name}')

        for resource in class_list:
            metdos_list = resource['methods']
            for metod in metdos_list:
                class_content += metods[metod].rstrip()
            class_content += '\n'
            file_name = f"{root_path}/{folder_name}/{resource['name']}.py"

            folder_name = folder_name.lower()
            class_name = resource['class']
            if os.path.exists(file_name):
                print(f"Updating file '{file_name}'.")
            else:
                print(f"Creating file '{file_name}'.")
            with open(file_name, 'w') as file:
                file.write(
                    class_content.format(
                        class_name=class_name,
                        docstring=resource['docs'],
                        subclass=resource['name'],
                        class_main=folder_name,
                        result='Returns a list with a status code and the request data in JSON format: {{status: 200, data: '
                        '{{result: [list of {0}]}}}}'.format(resource['name']),
                    )
                )
            class_content = class_header


def docs():
    root_path = '../docs/api'
    api = read_specs()
    for folder in api:
        folder_name = folder['Class_name']
        class_list = folder['sub_classes']

        if not os.path.exists(f'{root_path}/{folder_name}'):
            os.makedirs(f'{root_path}/{folder_name}')

        with open(f'{root_path}/{folder_name}/index.md', 'w') as file:
            file.write(f'#{folder_name.lower()}\n::: {folder_name.lower()}')

        for resource in class_list:
            name = resource['name']
            file_name = f'{root_path}/{folder_name}/{name}.md'
            folder_name = folder_name.lower()
            content = f'::: {folder_name}.{name}'
            if os.path.exists(file_name):
                print(f"Updating file '{file_name}'.")
            else:
                print(f"Creating file '{file_name}'.")

            with open(file_name, 'w') as file:
                file.write(content)


def __main__():
    import sys

    if len(sys.argv) > 1:
        if sys.argv[1] == 'docs':
            docs()
        elif sys.argv[1] == 'code':
            code()
        else:
            print('Invalid argument.')
    else:
        print('No argument provided.')
