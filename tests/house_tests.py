import unittest
import sys
from traitor import house


class HouseFunctionalTests(unittest.TestCase):

    def test_can_not_put_room_on_wrong_floor(self):

        testroom = [house.Room(
            "Evil Room!",
            (False, False, False, False),
            (1, 2, 3))]
        with self.assertRaises(KeyError):
            house.discover((6,6,6),None,roomlist=testroom)
    def test_discovered_room_has_coordnate(self):
        testroom = [house.Room(
            "Test Room",
            (True, True, True, True),
            (-1, 0, 1))]
        house.discover((-1, 0, 0), None, roomlist=testroom)
        self.assertNotEqual(house.MAP[(-1, 0, 0)].x, None)

    def test_discovered_room_has_edges(self):
        testroom = [house.Room(
        "Test Room",
            (True, True, True, True),
            (-1, 0, 1))]
        house.discover((-2, 0, 0), None, roomlist=testroom)
        for edge in house.MAP[(-2, 0, 0)].edges:
            self.assertNotEqual(edge, None)


    def test_each_room_is_placeable(self):
        x = 1
        y = 0
        z = 0
        roomlist = list(house.ROOM_LIST)
        while roomlist != []:
            room = roomlist[0]
            z = room.allowed_floors[0]
            house.discover((x,y,z),None, roomlist)
            x += 1
        self.assertEqual(len(roomlist), 0, "ROOM_LIST did not empty")
