#encoding: utf-8

from Gspace import *

class Level3(Level):
    def __init__(self):
        self.level = (
            (1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            (1, 0, 0, 0, 0, 0, 7, 2, 0, 1),
            (1, 0, 0, 0, 0, 0, 7, 0, 0, 1),
            (1, 0, 0, 1, 0, 0, 1, 0, 0, 1),
            (1, 0, 0, 7, 0, 0, 7, 0, 0, 1),
            (1, 0, 0, 7, 0, 0, 7, 0, 0, 1),
            (1, 0, 0, 1, 0, 0, 1, 0, 0, 1),
            (1, 0, 0, 7, 0, 0, 0, 0, 0, 1),
            (1, 0, 3, 7, 0, 0, 0, 0, 0, 1),
            (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
        )
        Level.__init__(self)

    def update(self, gs):
        return self._update(gs, 'screen-final-end')

    def reset(self, gs):
        self._reset(gs)
