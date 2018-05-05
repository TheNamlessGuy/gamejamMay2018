#encoding: utf-8

from Gspace import *

class FinalEnd(WorldInterface):
    def __init__(self):
        WorldInterface.__init__(self)

    def update(self, gs):
        print "FinalEnd"
        return gs['screen-levelselect']

    def reset(self, gs):
        pass
