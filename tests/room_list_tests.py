roomlist=[["Wine Cellar", "(True,False,True,False)", "(-1,)"], ["Junk Room", "(True,True,True,True)", "(-1,0,1)"], ["Organ Room", "(False, False, True, True)", "(-1,0,1)"], ["Storeroom", "(True,False,False,False)", "(-1,1)"], ["Creeky Hallway", "(True,True,True,True)", "(-1,0,1)"], ["Dusty Hallway", "(True,True,True,True)", "(-1,0,1)"], ["Furnace Room", "(True,False,True,True)", "(-1,)"], ["Stairs from the Basement", "(False,False,True,False)", "(-1,)"], ["Operating Laboratory", "(False,True,True,False)", "(-1,1)"], ["Pentagram Chamber", "(False,True,False,False)", "(-1,)"], ["Attic", "(False,False,True,False)", "(1,)"], ["Chapel", "(True,False,False,False)", "(0,1)"], ["Research Laboratory", "(True,False,True,False)", "(-1,1)"], ["Mystic Elevator", "(True,False,False,False)", "(-1,0,1)"], ["Vault", "(True,False,False,False)", "(-1,1)"], ["Gardens", "(True,False,True,False)", "(0,)"], ["Graveyard", "(False,False,True,False)", "(0,)"], ["Patio", "(True,False,True,True)", "(0,)"], ["Servants' Quarters", "(True,True,True,True)", "(-1,1)"], ["Catacombs", "(True,False,True,False)", "(-1,)"], ["Ballroom", "(True,True,True,True)", "(0,)"], ["Gymnasium", "(False,True,True,False)", "(-1,1)"], ["Tower", "(False,True,False,True)", "(1,)"], ["Larder", "(True,False,True,False)", "(-1,)"], ["Bloody Room", "(True,True,True,True)", "(0,1)"], ["Dining Room", "(True,True,False,False)", "(0,)"], ["Master Bedroom", "(True,False,False,True)", "(1,)"], ["Conservatory", "(True,False,False,False)", "(0,1)"], ["Collapsed Room", "(True,True,True,True)", "(0,1)"], ["Bedroom", "(False,True,False,True)", "(1,)"], ["Coal Chute", "(True,False,False,False)", "(1,)"], ["Game Room", "(True,True,True,False)", "(-1,0,1)"], ["Library", "(False,False,True,True)", "(0,1)"], ["Charred Room", "(True,True,True,True)", "(0,1)"], ["Abandoned Room", "(True,True,True,True)", "(-1,0)"], ["Balcony", "(True,False,True,False)", "(1,)"], ["Statuary Corridor", "(True,False,True,False)", "(-1,0,1)"], ["Underground Lake", "(True,True,False,False)", "(-1,)"], ["Kitchen", "(True,True,False,False)", "(-1,0)"], ["Chasm", "(False,True,False,True)", "(-1,)"], ["Crypt", "(True,False,False,False)", "(-1,)"], ["Gallery", "(True,False,True,False)", "(1,)"]]
import unittest
import sys
from traitor import house


class RoomListTests(unittest.TestCase):
    def setUp(self):
        self.RoomList = house.RoomList(roomlist)

    def test_room_list_has_rooms(self):
        self.assertNotEqual(
            self.RoomList.LIST, [],
            "It seems that the roomlist was not properly filled :/"
        )
