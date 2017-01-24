class Room(object):


    cardinal_directions = ['north','south','east','west']
    special_directions = ['up','down','in','out']
    edge_table = [
        ['north','south'],
        ['south','north'],
        ['east','west'],
        ['west','east'],
        ['up','down'],
        ['down','up'],
        ['in','out'],
        ['out','in']]



    def __init__(self,
                 name,
                 number_of_doors):

        self.name = name
        self.edges = []

        for d in range(number_of_doors):
            self.edges.append({
                "direction": None,
                "connection": None
            })


    def set_coordnate(self,coordnate):
        self.x,self.y,self.z = coordnate
        return None

    def get_coordnate(self):
        return (self.x,self.y,self.z)

    def set_edges(self):
        for r, d in zip(self.edges, self.cardinal_directions):
            r['direction'] = d
        return None


    
    def connect(self, direction, room):
    
        if direction in self.special_directions:
            self.edges.append(
                {"direction": direction,
                 "connection": room.get_coordnate()
                }
                )
            return None
    
        for edge in self.edges:
            if edge["direction"] == direction:
                edge["connection"] = room.get_coordnate()
                return None
            else:
                pass
    
        for edge in self.edges:
            if edge["direction"] == None:
                edge["direction"] = direction
                edge["connection"] = room.get_coordnate()
                return None
            else:
                pass
    
        return None
    
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
                assert edge["connection"] != None
                return edge["connection"]
        raise KeyError
    
    
    



List_of_Rooms = [
    Room("Chasm",2),
    Room("Crypt",1),
    Room("Gallery",2),
    Room("Pentagram Chamber",1),
    Room("Attic", 1),
    Room("Chapel", 1),
    Room("Collapsed Room",4),
    Room("Balcony",2),
    Room("Stairs from Basement",1),
    Room("Graveyard",1),
    Room("Gardens",2),
    Room("Kitchen",2),
    Room("Vault",1),
    Room("Mystic Elevator",1),
    Room("Statuary Corridor",2),
    Room("Research Laboratory",2),
    Room("Underground Lake",2),
    Room("Furnace Room",3),
    Room("Catacombs",2),
    Room("Ballroom",4),
    Room("Game Room",3),
    Room("Library",2),
    Room("Charred Room", 4),
    Room("Abandoned Room", 4),
    Room("Dining Room", 2),
    Room("Conservatory",1),
    Room("Master Bedroom",2),
    Room("Bloody Room",4),
    Room("Tower",2),
    Room("Gymnasium", 2),
    Room("Operating Laboritory", 2),
    Room("Coal Chute",1),
    Room("Bedroom", 2),
    Room("Balcony",2),
    Room("Junk Room",2),
    Room("Creaky Hallway",4)
    ]

class Map(object):
    def __init__(self):
        MAP = {}

        MAP[(0,0,0)]= Room(
            "Entrance Hall",
            3
        )

        MAP[(0,1,0)] = Room(
            "Foyer",
            4
        )


        MAP[(0,2,0)] =  Room(
            "Grand Staircase",
            4
        )

        MAP[(0,0,1)] = Room(
            "Upper Landing",
            4
        )

        MAP[(0,0,-1)] = Room(
            "Basement Landing",
            4
        )


        for room in MAP:
            MAP[room].set_coordnate(room)
            MAP[room].set_edges()


        MAP[(0,0,0)].bi_connect("north", MAP[(0,1,0)])
        MAP[(0,1,0)].bi_connect("north", MAP[(0,2,0)])
        MAP[(0,2,0)].bi_connect("up", MAP[(0,0,1)])




        self.MAP = MAP

    
    def spawn_room(self, coordnate, room):
        self.MAP[coordnate] = room
        return None
