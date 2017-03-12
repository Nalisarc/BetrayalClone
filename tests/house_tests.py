import unittest
import sys
from traitor import house



class Discover_Tests(unittest.TestCase):

    def test_placeable_room_exists(self):
        coordnate = (0,0,1)
        roomlist = house.ROOM_LIST([])
        self.assertNotTrue(house.placeable_room_exists(coordnate,roomlist))
