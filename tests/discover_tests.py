import unittest
import sys
from traitor import house



class Discover_Tests(unittest.TestCase):

    def test_placeable_room_exists(self):
        ROOM_LIST = house.RoomList([]) #Empty
        self.assertFalse(house.placeable_room_exists((0,0,0),ROOM_LIST))
        ROOM_LIST.add_room(house.Room("Test",(False,False,False,False),(0,)))
        self.assertTrue(house.placeable_room_exists((0,0,0),ROOM_LIST))

    def test_can_place_room(self):
        #Test for False:
        self.assertFalse(
        house.can_place_room((0,0,0),house.Room("Test 1",(False,False,False,False),(-1,)))
        )
        #Test for True:
        self.assertTrue(
        house.can_place_room((0,0,0),house.Room("Test 2",(False,False,False,False),(0,)))
        )

    def test_search_fails_on_no_placeable_room(self):
        ROOM_LIST = house.RoomList([])
        with self.assertRaises(IndexError) as cm:
            house.search_for_room((0,0,0),ROOM_LIST)
        return None


    def test_rotate_room(self):
        # Test Rooms
        FOUR_TRUE_ROOM = house.Room("Test Room 4",(True,True,True,True),(-1,0,1))
        THREE_TRUE_ROOM = house.Room("Test Room 3",(False,True,True,True),(-1,0,1))
        TWO_TRUE_ROOM = house.Room("Test Room 2",(False,False,True,True),(-1,0,1))
        ONE_TRUE_ROOM = house.Room("Test Room 1",(False,False,False,True),(-1,0,1))
        ZERO_TRUE_ROOM = house.Room("Test Room 0",(False,False,False,False),(-1,0,1))
        # Expected Rotations
        FOUR_ROTATIONS = [0,1,2,3]
        THREE_ROTATIONS = [0,1,3]
        TWO_ROTATIONS = [0,3]
        ONE_ROTATIONS = [3]
        ZERO_ROTATIONS = []

        # Tests if output matches expected
        self.assertEqual(house.rotate_room(FOUR_TRUE_ROOM,"north"),FOUR_ROTATIONS)
        self.assertEqual(house.rotate_room(THREE_TRUE_ROOM, "north"),THREE_ROTATIONS)
        self.assertEqual(house.rotate_room(TWO_TRUE_ROOM, "north"), TWO_ROTATIONS)
        self.assertEqual(house.rotate_room(ONE_TRUE_ROOM, "north"), ONE_ROTATIONS)
        self.assertEqual(house.rotate_room(ZERO_TRUE_ROOM, "north"), ZERO_ROTATIONS)


    def test_discover_room(self):
        DISCOVERED_ROOM = house.Room("Discoved Room",(True,True,True,True),(-1,0,1))        
        MAP = house.Map()
        ROOM_LIST = house.RoomList([DISCOVERED_ROOM])
        house.discover_room(MAP,ROOM_LIST,(1,0,0),"east")

        self.assertEqual(MAP.MAP[(1,0,0)].name, "Discoved Room")

        self.assertTrue(MAP.MAP[(0,0,0)].is_connected_at('east'))
        self.assertTrue(MAP.MAP[(1,0,0)].is_connected_at('west'))
