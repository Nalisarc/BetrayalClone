class Room(object):


    edge_table = [
        ["north","south"],
        ["south","north"],
        ["east","west"],
        ["west","east"],
        ["in","out"],
        ["out","in"],
        ["up","down"],
        ["down","up"]
    ]

    special_directions = ['up','down','in','out']


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
        pass

    
    def connect(self, direction, room):
    
        if direction in self.special_directions:
            self.edges.append(
                {"direction": direction,
                 "connection": room.get_coordnate()
                }
                )
            return None
    
        for edge in self.edges:
            if edge["direction"] == None:
                edge["direction"] = direction
                edge["connection"] = room.get_coordnate()
                break
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


        MAP[(0,0,0)].bi_connect("north", MAP[(0,1,0)])
        MAP[(0,1,0)].bi_connect("north", MAP[(0,2,0)])
        MAP[(0,2,0)].bi_connect("up", MAP[(0,0,1)])




        self.MAP = MAP

    
    def discover(self,coordnate, room):
    
        self.MAP[coordnate] = room
