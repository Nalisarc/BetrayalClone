import unittest
import sys
from traitor import house



class Discover_Tests(unittest.TestCase):

    def test_placeable_room_exists_will_fail_if_none(self):
        coordnate = (0,0,1)
        roomlist = house.RoomList([])
        self.assertFalse(house.placeable_room_exists(coordnate,roomlist))

    def test_placeable_room_exists_will_pass(self):
        testroom = house.Room(
            "test room",
            (-1,0,1),
            )
        coordnate = (0,0,1)
        roomlist = house.RoomList([testroom])

        self.assertTrue(house.placeable_room_exists(coordnate,roomlist))
