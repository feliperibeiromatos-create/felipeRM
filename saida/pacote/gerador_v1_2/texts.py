import json
def walk(o, path=''):
    if isinstance(o, str):
        yield path, o
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from walk(v, f'{path}[{i}]')
    elif isinstance(o, dict):
        for k, v in o.items():
            yield from walk(v, f'{path}.{k}')
def load(p='out/pacote.json'):
    return json.load(open(p))
