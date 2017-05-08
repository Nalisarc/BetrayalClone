import unittest

class Deck(object):

    def __init__(self, _list):
        self._list = _list
        return None

    def __len__(self):
        return len(self._list)

    def __repr__(self):
        return "Deck({0})".format(self._list)

    def __getitem__(self, position):
        return self._list[position]

    def __setitem__(self, position, value):
        self._list[position] = value
        return None

    def append(self, value):
        self._list.append(value)
        return None

    def pop(self):
        return self._list.pop()

class DeckUnitTests(unittest.TestCase):

    def test_can_make_deck(self):
        test = Deck([])
        self.assertIsInstance(test,Deck)

    def test_decks_are_indexable(self):
        test = Deck([1,2,3])
        self.assertEqual(test[0], 1)

    def test_decks_can_be_appended(self):
        test = Deck([1,2,3])
        test.append(4)
        self.assertEqual(test[3],4)

    def test_decks_can_be_changed(self):
        test = Deck([1])
        test[0] = 'a'
        self.assertEqual(test[0], 'a')

    def test_decks_are_syntactically_symmetrical(self):
        test1 = Deck([1,2,3])
        r = repr(test1)
        test2 = eval(r)
        self.assertEqual(test1._list,test2._list)

    def test_decks_are_iterable(self):
        test = Deck([1,2,3])
        for i in test:
            self.assertEqual(i, test[i-1])

    def test_decks_can_be_popped(self):
        test = Deck([1,2,3])
        v = test.pop()
        self.assertEqual(v, 3)
        self.assertEqual(len(test),2)
