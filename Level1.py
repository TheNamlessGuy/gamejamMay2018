#encoding: utf-8

from Gspace import *
from Player import *

class Level1(Level):
    def __init__(self):
        self.level = (
            (1, 1, 1, 1, 1, 1, 1, 1),
            (1, 1, 1, 0, 0, 1, 1, 1),
            (1, 3, 0, 0, 0, 0, 2, 1),
            (1, 1, 1, 0, 0, 1, 1, 1),
            (1, 1, 1, 1, 1, 1, 1, 1)
        )
        Level.__init__(self)

    def update(self, gs):
        return self._update(gs, 'screen-normal-end')

    def reset(self, gs):
        self._reset(gs)
