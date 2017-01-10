import unittest
import sys
from traitor import housemap

class MapUnitTests(unittest.TestCase):

    def setUp(self):
        self.MAP = housemap.setup()


    def test_if_rooms_exist(self):
        list_of_rooms = [[r, self.MAP[r]] for r in self.MAP]
        self.assertNotEqual(len(list_of_rooms),0)

    def test_if_rooms_connected(self):
        #Check if connections can be made

        self.assertTrue(
        self.MAP['000'].is_connected_at('north')
            )
        self.assertTrue(
        self.MAP['001'].is_connected_at('north')
            )
        self.assertTrue(
        self.MAP['002'].is_connected_at('up')
            )

        #Check reverse connections.
        self.assertTrue(
        self.MAP['001'].is_connected_at('south')
            )
        self.assertTrue(
        self.MAP['002'].is_connected_at('south')
            )
        self.assertTrue(
        self.MAP['100'].is_connected_at('down')
            )

    def test_can_move_between_rooms(self):
        pos = self.MAP['000']

        pos = pos.move('north')

        self.assertEqual(pos,self.MAP['001'],
                         "Position did not move!")
        pos = pos.move('south')

        self.assertEqual(pos,self.MAP['000'],
                         "Position failed in reverse")

    def test_cannot_move_invalid_direction(self):

        pos = self.MAP['000']
        pos = pos.move('up')
        self.assertEqual(pos,self.MAP['000'])
