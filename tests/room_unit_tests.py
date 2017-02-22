import unittest
import sys
from traitor import house


class RoomUnitTests(unittest.TestCase):
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
