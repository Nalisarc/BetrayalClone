room_table=[["Wine Cellar", "(True,False,True,False)", "(-1)"], ["Junk Room", "(True,True,True,True)", "(-1,0,1)"], ["Organ Room", "(False, False, True, True)", "(-1,0,1)"], ["Storeroom", "(True,False,False,False)", "(-1,1)"], ["Creeky Hallway", "(True,True,True,True)", "(-1,0,1)"], ["Dusty Hallway", "(True,True,True,True)", "(-1,0,1)"], ["Furnace Room", "(True,False,True,True)", "(-1)"], ["Stairs from the Basement", "(False,False,True,False)", "(-1)"], ["Operating Laboratory", "(False,True,True,False)", "(-1,1)"], ["Pentagram Chamber", "(False,True,False,False)", "(-1)"], ["Attic", "(False,False,True,False)", "(1)"], ["Chapel", "(True,False,False,False)", "(0,1)"], ["Research Laboratory", "(True,False,True,False)", "(-1,1)"], ["Mystic Elevator", "(True,False,False,False)", "(-1,0,1)"], ["Vault", "(True,False,False,False)", "(-1,1)"], ["Gardens", "(True,False,True,False)", "(0)"], ["Graveyard", "(False,False,True,False)", "(0)"], ["Patio", "(True,False,True,True)", "(0)"], ["Servants' Quarters", "(True,True,True,True)", "(-1,1)"], ["Catacombs", "(True,False,True,False)", "(-1)"], ["Ballroom", "(True,True,True,True)", "(0)"], ["Gymnasium", "(False,True,True,False)", "(-1,1)"], ["Tower", "(False,True,False,True)", "(1)"], ["Larder", "(True,False,True,False)", "(-1)"], ["Bloody Room", "(True,True,True,True)", "(0,1)"], ["Dining Room", "(True,True,False,False)", "(0)"], ["Master Bedroom", "(True,False,False,True)", "(1)"], ["Conservatory", "(True,False,False,False)", "(0,1)"], ["Collapsed Room", "(True,True,True,True)", "(0,1)"], ["Bedroom", "(False,True,False,True)", "(1)"], ["Coal Chute", "(True,False,False,False)", "(1)"], ["Game Room", "(True,True,True,False)", "(-1,0,1)"], ["Library", "(False,False,True,True)", "(0,1)"], ["Charred Room", "(True,True,True,True)", "(0,1)"], ["Abandoned Room", "(True,True,True,True)", "(-1,0)"], ["Balcony", "(True,False,True,False)", "(1)"], ["Statuary Corridor", "(True,False,True,False)", "(-1,0,1)"], ["Underground Lake", "(True,True,False,False)", "(-1)"], ["Kitchen", "(True,True,False,False)", "(-1,0)"], ["Chasm", "(False,True,False,True)", "(-1)"], ["Crypt", "(True,False,False,False)", "(-1)"], ["Gallery", "(True,False,True,False)", "(1)"]]
import itertools
import random
class Room(object):


    cardinal_directions = ('north','east','south','west')
    special_directions = ('up','down','in','out')
    edge_table = (
        ('north','south'),
        ('south','north'),
        ('east','west'),
        ('west','east'),
        ('up','down'),
        ('down','up'),
        ('in','out'),
        ('out','in'))





    def __init__(self,
                 name,
                 shape=(True, True, True, True),
                 allowed_floors=(-1,0,1)):
        self.name = name
        self.shape = shape
        self.allowed_floors = allowed_floors

        self.edges = []
        for edge in shape:
            self.edges.append(
                {"direction": None,
                 "connection": None,
                 "enabled": edge
                 })

    def set_edges(self, rotation=0):
        """
        Rotation is an integer between 0-3.
        Anything higher is redundant and any < 0 will cause trouble.
        """
        if rotation < 0:
            raise ValueError

        direction_wheel = itertools.cycle(self.cardinal_directions)

        for n in range(int(rotation)):
            direction_wheel.__next__()
            continue

        for edge in self.edges:
            edge['direction'] = direction_wheel.__next__()
            continue

        return None

    def set_coordnate(self,coordnate):
        self.x,self.y,self.z = coordnate
        return None

    def get_coordnate(self):
        return (self.x,self.y,self.z)

    
    def connect(self, direction, room):
    
        if direction in self.special_directions:
            self.edges.append(
                {"direction": direction,
                 "connection": room.get_coordnate()
                }
                )
            return None
        for edge in self.edges:
            if direction in edge['direction']:
                edge['direction'] = direction
                edge['connection'] = room.get_coordnate()
                return None
            else:
                pass
    
    
    
    def bi_connect(self, direction, room):
    
        opposite_direction = None
        for d in self.edge_table:
            if d[0] == direction:
                opposite_direction = d[1]
                break
            else:
                continue
        if opposite_direction == None:
            return "Error: Missing Opposite Edge!"
    
        self.connect(direction, room)
        room.connect(opposite_direction, self)
    
    
    
    def is_connected_at(self, direction):
        for edge in self.edges:
            if edge["direction"] == direction:
                return True
    
        return False
    
    def is_connected_to(self,room):
        for edge in self.edges:
            if edge["connection"] == room:
                return True
        return False
    
    def is_connected_to_at(self,direction,room):
        for edge in self.edges:
            con_1 = edge["direction"] == direction
            con_2 = edge["connection"] == room
            if con_1 and con_2:
                return True
    
        return False
    def move(self, direction):
    
        for edge in self.edges:
            if edge["direction"] == direction:
                assert edge["enabled"] != False
                return edge["connection"]
    
    
    
    




ROOM_LIST = []

for room in room_table:
    ROOM_LIST.append(Room(
        room[0],
        eval(room[1]),
        eval(room[2]),)
    )



def spawn_room(coordnate, room):
    MAP[coordnate] = room
    return None




MAP = {}

MAP[(0,0,0)]= Room(
    "Entrance Hall",
    (True,True,False,True)
)

MAP[(0,1,0)] = Room(
    "Foyer",
    #Blank means all doors enabled
)


MAP[(0,2,0)] =  Room(
    "Grand Staircase",
    (False,False,True,False)
)

MAP[(0,0,1)] = Room(
    "Upper Landing",

)

MAP[(0,0,-1)] = Room(
    "Basement Landing",

)


for room in MAP:
    MAP[room].set_coordnate(room)
    MAP[room].set_edges()


MAP[(0,0,0)].bi_connect("north", MAP[(0,1,0)])
MAP[(0,1,0)].bi_connect("north", MAP[(0,2,0)])
MAP[(0,2,0)].bi_connect("up", MAP[(0,0,1)])
