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
        self.player.update(gs, self)

    def reset(self, gs):
        self.player = Player(self.tiles['start'][0].pos)
        
        self.sprites = []

        for tiletype in self.tiles:
            for tile in self.tiles[tiletype]:
                self.sprites.append(tile)

        self.sprites.append(self.player.player)
