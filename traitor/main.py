#!/usr/bin/env python3
import sys
import housemap
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

class player(object):

    def __init__(self, house):

        self.house = house
        self.pos = self.house.MAP[(0,0,0)]
        return None

    def repl(self):
        prompt = '==>'
        while True:

            i = input(prompt)
            if i == "go":
                direction = input("Which direction: ")
                self.go(direction)
            elif i == "quit":
                self.quit()

            elif i == "":
                pass
            else:
                print("Im sorry Dave, I'm afraid I can't do that")



    def go(self,direction):
        try:
            self.pos = self.house.MAP[self.pos.move(direction)]
            print(self.pos.name, self.pos.get_coordnate())
            return None
        except AssertionError:
            x,y,z = self.pos.get_coordnate()

            if direction == "north":
                y += 1
            if direction == "south":
                y -= 1
            if direction == "east":
                x += 1
            if direction == "west":
                x -= 1

            try:
                self.pos.bi_connect(direction, self.house.MAP[(x,y,z)])
                self.pos = self.house.MAP[self.pos.move(direction)]
                print(self.pos.name, self.pos.get_coordnate())
            except KeyError:

                self.house.discover((x,y,z),housemap.Room(
                    "test room",
                    ['north','south','east','west'])
                )
                self.house.MAP[(x,y,z)].set_coordnate((x,y,z))
                self.pos.bi_connect(direction, self.house.MAP[(x,y,z)])
                self.pos = self.house.MAP[self.pos.move(direction)]
                print(self.pos.name, self.pos.get_coordnate())
                return None
        except KeyError:
            print("Invaild direction!")
            print(self.pos.name, self.pos.get_coordnate())
            return None

    def quit(self):
        sys.exit()


if __name__ == '__main__':
    me = player(house)
    me.repl()
