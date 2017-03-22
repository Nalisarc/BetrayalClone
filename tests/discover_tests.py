import unittest
import sys
from traitor import house



class Discover_Tests(unittest.TestCase):

    def test_placeable_room_exists(self):
        ROOM_LIST = house.RoomList([]) #Empty
        self.assertFalse(house.placeable_room_exists((0,0,0),ROOM_LIST))
        ROOM_LIST.add_room(house.Room("Test",(False,False,False,False),(0)))
        self.assertTrue(house.placeable_room_exists((0,0,0),ROOM_LIST))

    def test_can_place_room(self):
        #Test for False:
        self.assertFalse(
        house.can_place_room((0,0,0),house.Room("Test1",(False,False,False,False),(-1,)))
        )
        #Test for True:
        self.assertTrue(
        house.can_place_room((0,0,0),house.Room("Test1",(False,False,False,False),(0,)))
        )

    def test_search_fails_on_no_placeable_room(self):
        ROOM_LIST = house.RoomList([])
        with self.assertRaises(IndexError) as cm:
            house.search_for_room((0,0,0),ROOM_LIST)
