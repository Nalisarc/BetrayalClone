import unittest
import sys
from traitor import house



class Discover_Tests(unittest.TestCase):
    def setUp(self):
        self.MAP = house.Map()
        self.ROOM_LIST = house.RoomList(house.room_list)

    def test_can_discover_room(self):
        discover((1,0,0), 'east',MAP=self.MAP,ROOM_LIST=ROOM_LIST)
        self.MAP.MAP(1,0,0)
