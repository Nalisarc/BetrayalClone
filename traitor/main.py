from traitor import housemap
class Character(object):

    def __init__(self):

        self.name = name
        self.birthday = birthday

        #Stat lists

        self.might = might
        self.speed = speed
        self.knowledge = knowledge
        self.sanity = sanity

        #Inventory
        self.inventory = []

        #Position
        self.position = (0,0,0)

    def change_stat(self, stat, value):
        """To raise the stat use a positive integer, 
        to lower the stat use a negative integer"""
        self.stat['current'] += value
        #Performs 0 check
        if self.stat['current'] < 0:
            self.stat['current'] = 0
        #Performs 8 check    
        if self.stat['current'] > 8:
            self.stat['current'] = 8
        #Change sucessful
        return None

house = housemap.Map()
me = Character(
    "Zeeter",
    "01/17",
    ['dead',9,9,9,9,9,9,9,9,9],
    ['dead',9,9,9,9,9,9,9,9,9],
    ['dead',9,9,9,9,9,9,9,9,9],
    ['dead',9,9,9,9,9,9,9,9,9],
)

me.pos = house.MAP[(0,0,0)]
