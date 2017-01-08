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
    
    






def setup():
    MAP = {}

    MAP['000']= Room(
        "Entrance Hall",
        '000',
        ("north","east","west"))

    MAP['001'] = Room(
        "Foyer",
        '001',
        ("north","south","east","west"))


    MAP['002'] =  Room(
        "Grand Staircase",
        '002',
        ("south","east","west"))

    MAP['100'] = Room(
        "Upper Landing"
        '100',
        ("north","south","east","west"))

    MAP['-100'] = Room(
        "Basement Landing",
        '-100',
        ("north","south","east","west"))


    MAP['000'].connect("north", MAP['001'])
    MAP['001'].connect("north", MAP['002'])
    MAP['002'].connect("up", MAP['100'])

    return MAP
