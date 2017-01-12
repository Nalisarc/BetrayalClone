class Room(object):

    def __init__(self,
                 name,
                 coordnate,
                 allowed_edges):

        self.name = name
        self.coordnate = coordnate
        self.edges = {}
        for edge in allowed_edges:
            self.edges[edge] = None
        return None

    def connect(self, direction, room):
        #Bidirectional right now
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
        opposite_direction = None
        for d in edge_table:
            if d[0] == direction:
                opposite_direction = d[1]
                break
            else:
                continue
        if opposite_direction == None:
            return "Error: Missing Opposite Edge!"
    
        self.edges[direction] = room
        room.edges[opposite_direction] = self
        return None
    
    
    def is_connected_at(self, direction):
        if self.edges[direction] != None:
            return True
        else:
            return False
    
    def is_connected_to(self,room):
        if room in self.edges.values():
            return True
        else:
            return False
    
    def is_connected_to_at(self, room, direction):
        condition1 = self.is_connected_at(direction)
        condition2 = self.is_connected_to(room)
        if condition1 and condition2:
            return True
        else:
            return False
    
    def move(self, direction):
        try:
            if direction != None:
                return self.edges[direction]
            else:
                pass
        except KeyError:
            return self
        except:
            return "Unexpected Error!"
    





def setup():
    MAP = {}

    MAP[(0,0,0)]= Room(
        "Entrance Hall",
        (0,0,0),
        ("north","east","west"))

    MAP[(0,0,1)] = Room(
        "Foyer",
        '001',
        ("north","south","east","west"))


    MAP[(0,0,2)] =  Room(
        "Grand Staircase",
        '002',
        ("south","east","west"))

    MAP[(1,0,0)] = Room(
        "Upper Landing",
        (1,0,0),
        ("north","south","east","west"))

    MAP[(-1,0,0)] = Room(
        "Basement Landing",
        (-1,0,0),
        ("north","south","east","west"))

    MAP[(0,0,0)].connect("north", MAP[(0,0,1)])
    MAP[(0,0,1)].connect("north", MAP[(0,0,2)])
    MAP[(0,0,2)].connect("up", MAP[(1,0,0)])

    return MAP
