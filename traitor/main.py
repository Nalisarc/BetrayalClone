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
            self.pos = house.MAP[self.pos.move(direction)]
            print(self.pos.name, self.pos.get_coordnate())
            return None
        except AssertionError:
            print("You can't go that way")
        except KeyError:
            house.spawn_room(
                (self.pos.move(direction)),
                 house.ROOM_LIST.pop())
            house.MAP[self.pos.move(direction)].set_coordnate(
            self.pos.move(direction))
            house.MAP[self.pos.move(direction)].set_connections()
            self.pos = house.MAP[self.pos.move(direction)]
            print(self.pos.name)
    def quit(self):
        sys.exit()

    def look(self):
        print("You are in the {}".format(self.pos.name))
        print("You can go: ")
        for edge in self.pos.edges:
            if edge["enabled"] == True:
                print(edge['direction'])
        return None


if __name__ == '__main__':
    me = player()
    me.repl()
