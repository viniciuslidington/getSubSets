# SubSet question - Encora - Estagio

class MySet:
    def __init__(self):
        self.data = []  # lista interna para armazenar elementos sem repetição

    def add(self, element):
        if element not in self.data:
            self.data.append(element)
            return True
        return False

    def addAll(self, other_set):
        changed = False
        for element in other_set.data:
            if self.add(element):
                changed = True
        return changed

    def contains(self, element):
        return element in self.data

    def equals(self, other_set):
        if self.size() != other_set.size():
            return False
        for e in self.data:
            if not other_set.contains(e):
                return False
        return True

    def iterator(self):
        return iter(self.data)

    def remove(self, element):
        if element in self.data:
            self.data.remove(element)
            return True
        return False

    def size(self):
        return len(self.data)

    def toArray(self):
        return list(self.data)

    def __repr__(self):
        if self.size() == 0:
            return "{}"
        return "{" + ", ".join(str(e) for e in self.data) + "}"