class Character(object):

    def __init__(self,
                 name,
                 birthday,
                 might,
                 speed,
                 knowledge,
                 sanity):

        self.name = name
        self.birthday = birthday

        #Stat lists

        self.might = might
        self.speed = speed
        self.knowledge = knowledge
        self.sanity = sanity

        #Inventory
        self.inventory = []

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
