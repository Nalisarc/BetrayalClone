#!/usr/bin/env python3
import sys
import house
class player(object):

    def __init__(self):

        self.pos = house.MAP[(0,0,0)]
        return None

    def repl(self):
        print("Traitor pre-alpha demo")
        print("Made by Daniel A Smith")
        prompt = '==> '

        while True:
            command = input(prompt)
            command_parsed = command.split()
            if len(command_parsed) == 0:
                pass
            elif command_parsed[0] == 'go':
                try:
                    self.go(command_parsed[1])
                except IndexError:
                    d = input("Which direction do you want to go?: ")
                    self.go(d)
                except:
                    print("Something went wrong")
            elif command_parsed[0] == 'look':
                self.look()
            elif command_parsed[0] == 'quit':
                self.quit()
            else:
                print("Invaild command, sorry")


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

                self.house.spawn_room((x,y,z),
				      house.List_of_Rooms.pop())
                self.house.MAP[(x,y,z)].set_coordnate((x,y,z))
                self.house.MAP[(x,y,z)].set_edges()
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

    def look(self):
        print("You are in the {}".format(self.pos.name))
        print("You can go: ")
        for edge in self.pos.edges:
            print(edge['direction'])
        return None


if __name__ == '__main__':
    me = player(house)
    me.repl()
