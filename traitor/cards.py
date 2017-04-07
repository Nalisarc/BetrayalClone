
class Deck(object):
    def __init__(self, _list):
        self._list = _list
        return None

    def __repr__(self):
        return "Deck({0})".format(self._list)

    def __getitem__(self,position):
        return self._list[position]

    def __setitem__(self,position,value):
        self._list[position] = value
        return None

    def append(self,value):
        self._list.append(value)
        return None
