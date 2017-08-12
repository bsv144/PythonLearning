'''
reloadall.py: Транзитивная перезагрузка вложенных модулей
'''

import types
from importlib import reload

def status(module):
    print('reloading: ' + module.__name__)

def transitive_reload(module, visited):
    if not module in visited:
        status(module)
        reload(module)
        visited[module] = None
        for attobj in module.__dict__.values():
            if type(attobj) == types.ModuleType:
                transitive_reload(attobj,visited)

def reload_all(*args):
    visited = {}
    for arg in args:
        if type(arg) == types.ModuleType:
            transitive_reload(arg, visited)

if __name__ == '__main__':
    import reloadall
    reload_all(reloadall)