
#encoding: utf-8

from Gspace import *
from Player import *

class Level1(Level):
    def __init__(self):
        Level.__init__(self)
        self.level = [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 1, 1, 1],
            [1, 3, 0, 0, 0, 0, 2, 1],
            [1, 1, 1, 0, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1]
        ]
        self._load_tiles()
        self.player = Player(Vec2(320, 240))

    def update(self, gs):
        self.player.update(gs)

    def reset(self, gs):
        self.sprites = []

        for tiletype in self.tiles:
            for tile in self.tiles[tiletype]:
                self.sprites.append(tile)

        self.sprites.append(self.player.player)
