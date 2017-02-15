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


class Stat(object):

    def __init__(self, range_, current):
        self.range_ = ('dead') + range_
        self.current = current
        return None
