import os

class Viewmodel:
    def __init__(self,items):
        self._items = items
    def todoitems(self):
        result = []
        for item in self._items:
            if item.idList == os.environ.get('TO_DO'):
                result.append(item)
        return result
    def doingitems(self):
        result = []
        for item in self._items:
            if item.idList == os.environ.get('DOING'):
                result.append(item)
        return result
    def doneitems(self):
        result = []
        for item in self._items:
            if item.idList == os.environ.get('DONE'):
                result.append(item)
        return result
