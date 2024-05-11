import logging
import sys
import time

sys.path.append('..')
from netboxcli import Client

client = Client('http://localhost:8000', 'token')

log_debug = logging.getLogger('debug')
log_debug.setLevel(logging.DEBUG)
log_debug.addHandler(logging.FileHandler('test_passed.log'))

log_error = logging.getLogger('error')
log_error.setLevel(logging.ERROR)
log_error.addHandler(logging.FileHandler('test_failed.log'))


def get_modules(obj):
    modules = []
    for module in dir(obj):
        if not module.startswith('__') and not module.startswith('_'):
            attr = getattr(obj, module)
            for sub_module in dir(attr):
                if not sub_module.startswith(
                    '__'
                ) and not sub_module.startswith('_'):
                    modules.append(f'{module}.{sub_module}')

    return modules


def validation(module, result):
    if isinstance(result, list) and result and result[0] == 404:
        print(f'Module: {module} - failed - Page not found')
        log_error.error(f'Module: {module} pege not found- {result}')
        return False

    elif isinstance(result, list):
        print(f'Module: {module} - passed')
        log_debug.info(f'Module: {module} - Result: {result}')
        return [True, result]
    elif isinstance(result, dict):
        print(f'Module: {module} - passed')
        log_debug.info(f'Module: {module} - Result: {result}')

        return [True, result]

    else:
        print(f'Module: {module} - failed')
        log_error.error(f'Module: {module} - Error: {result}')
        return False


# test get method of all modules using the pytest
def test_get(obj, modules):
    for module in modules:
        try:
            module_list = module.split('.')
            module_obj1 = getattr(obj, module_list[0])
            module_obj2 = getattr(module_obj1, module_list[1])
        except Exception as e:
            log_error.error(f'Error: {e}')
            continue

        try:
            try:
                result = module_obj2.get()
                time.sleep(1)
            except Exception as e:
                print(f'Module: {module} - request failed')
                log_error.error(f'{e}')
                continue
            if isinstance(result, list) and result and result[0] == 111:
                print('Conenction Error')
                log_error.error(f'{result}')
                break

            assert validation(module, result)

        except Exception as e:
            print(f'Module: {module} - failed')
            log_error.error(f'Module: {module} execution - Error: {e}')


modules = get_modules(client)


def main():

    if len(sys.argv) > 1:
        if sys.argv[1] == 'get':
            test_get(client, modules)
        else:
            print('Invalid argument.')
    else:
        print('No argument provided.')


if __name__ == '__main__':
    main()
