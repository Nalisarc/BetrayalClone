import random

## My Dice Class I use for everything
class Dice(object):

    def __init__(self,_min,_max):
        self._min = _min
        self._max = _max
        return None

    def __repr__(self):
        return "Dice({0},{1})".format(self._min, self._max)

    def roll(self):
        return random.randint(self._min, self._max)
