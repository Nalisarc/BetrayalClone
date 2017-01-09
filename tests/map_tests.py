import unittest
import sys
from traitor import housemap

class MapUnitTests(unittest.TestCase):

    def setUp(self):
        self.MAP = housemap.setup()


    def test_if_rooms_exist(self):
        list_of_rooms = [[r.key(),r.value()] for r in self.MAP]
        self.assertNotEqual(len(list_of_rooms),0)

    def test_if_rooms_connected(self):

        self.assertTrue(
        self.MAP['000'].is_connected_at('north')
            )
        self.assertTrue(
        self.MAP['001'].is_connected_at('north')
            )
        self.assertTrue(
        self.MAP['002'].is_connected_at('up')
            )




if __name__ == '__main__':
    unittest.main()
    sys.exit()
