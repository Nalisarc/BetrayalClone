import unittest
import sys
from traitor import house


class MapUnitTests(unittest.TestCase):

    def setUp(self):
        self.MAP = house.MAP

    def test_if_rooms_exist(self):
        list_of_rooms = [[r, self.MAP[r]] for r in self.MAP]
        self.assertNotEqual(len(list_of_rooms), 0)

    def test_if_rooms_connected(self):
        # Check if connections can be made

        self.assertTrue(
            self.MAP[(0, 0, 0)].is_connected_at('north'),
            self.MAP[(0, 0, 0)].edges
        )
        self.assertTrue(
            self.MAP[(0, 1, 0)].is_connected_at('north')
        )
        self.assertTrue(
            self.MAP[(0, 2, 0)].is_connected_at('up')
        )

        # Check reverse connections.
        self.assertTrue(
            self.MAP[(0, 1, 0)].is_connected_at('south')
        )
        self.assertTrue(
            self.MAP[(0, 2, 0)].is_connected_at('south')
        )
        self.assertTrue(
            self.MAP[(0, 0, 1)].is_connected_at('down')
        )

    def test_can_move_between_rooms(self):
        pos = self.MAP[(0, 0, 0)]

        pos = self.MAP[pos.move('north')]

        self.assertEqual(pos, self.MAP[(0, 1, 0)],
                         "Position did not move!")
        pos = self.MAP[pos.move('south')]

        self.assertEqual(pos, self.MAP[(0, 0, 0)],
                         "Position failed in reverse")

    def test_cannot_move_invalid_direction(self):

        pos = self.MAP[(0, 0, 0)]
        try:
            pos = self.MAP[pos.move('up')]
        except KeyError:
            self.assertEqual(pos, self.MAP[(0, 0, 0)])

    def test_does_not_move_if_room_is_undiscovered(self):

        pos = self.MAP[(0, 0, 0)]
        try:
            pos.move("east")
        except AssertionError:
            self.assertEqual(pos, self.MAP[(0, 0, 0)])

    def test_can_spawn_new_rooms(self):
        discovered_room = house.Room(
            "Test Room",

        )

        pos = self.MAP[(0, 0, 0)]
        house.spawn_room(
            (1, 0, 0),
            discovered_room
        )
        self.MAP[(1, 0, 0)].set_coordnate((1, 0, 0))
        self.MAP[(1, 0, 0)].set_edges()

        pos.bi_connect('east', self.MAP[(1, 0, 0)])

        pos = self.MAP[pos.move('east')]

        self.assertEqual(pos, self.MAP[(1, 0, 0)],
                         "Wrong room?!? {0}".format(pos.name)
                         )

        # From Room experiment

    def test_rooms_have_no_direction_by_default(self):
        test_room = house.Room(
            "test_room"
        )
        for edge in test_room.edges:
            self.assertEqual(edge['direction'], None)

    def test_rooms_default_rotation(self):
        test_room = house.Room(
            "test_room")
        test_room.set_edges()
        edges = test_room.edges
        directions = test_room.cardinal_directions
        zipped = zip(edges, directions)
        for edge, direction in zipped:
            self.assertEqual(edge["direction"], direction)

    def test_rooms_rotation(self):
        test_room = house.Room(
            "test_room")
        test_room.set_edges(1)
        edges = test_room.edges
        self.assertEqual(
            edges[0]['direction'], 'east')
        self.assertEqual(
            edges[1]['direction'], 'south')
        self.assertEqual(
            edges[2]['direction'], 'west')
        self.assertEqual(
            edges[3]['direction'], 'north')

    def test_room_list_has_rooms(self):
        self.assertNotEqual(house.ROOM_LIST, [],
                            "ROOM_LIST is empty!!")

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
