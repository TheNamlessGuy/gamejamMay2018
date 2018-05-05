#encoding: utf-8

from Gspace import *

class NormalEnd(WorldInterface):
    def __init__(self):
        WorldInterface.__init__(self)

    def update(self, gs):
        print "NormalEnd"
        return gs['screen-levelselect']

    def reset(self, gs):
        pass
