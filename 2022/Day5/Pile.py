import sys


class Pile:
    def __init__(self, maxSize=None):
        self.items = []
        self.MAX_SIZE = sys.maxsize if maxSize is None else maxSize

    def add(self, item):
        if type(item) is list:
            for it in item:
                if len(self.items) < self.MAX_SIZE:
                    self.items.append(it)
                else:
                    break
        else:
            if len(self.items) < self.MAX_SIZE:
                self.items.append(item)
            else:
                raise IndexError("Full stack")

    def nextItemPop(self):
        return self.items[-1]

    def pop(self):
        if len(self.items) <= 0:
            raise IndexError('pile vide')
        self.items.pop(-1)

    def isEmpty(self):
        return len(self.items) == 0

    def length(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)
