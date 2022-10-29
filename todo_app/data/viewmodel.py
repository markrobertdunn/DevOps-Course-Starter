import os

class Viewmodel:
    def __init__(self,items):
        self._items = items
    def todoitems(self):
        result = []
        for item in self._items:
            if item.status == "To-Do":
                result.append(item)
        return result
    def doingitems(self):
        result = []
        for item in self._items:
            if item.status == "Doing":
                result.append(item)
        return result
    def doneitems(self):
        result = []
        for item in self._items:
            if item.status == "Done":
                result.append(item)
        return result
