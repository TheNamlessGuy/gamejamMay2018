#encoding: utf-8

from WorldInterface import *
from Sprite import *
from Vec2 import *

class Level(WorldInterface):
    def __init__(self):
        WorldInterface.__init__(self)
        self.objects = []
        self.tiles = {
            'air': [],
            'wall': [],
            'goal': [],
            'start': [],
            'bpadu': [],
            'bpadd': [],
            'bpadr': [],
            'bpadl': [],
            'rose': []
        }

    def _get_name_of(self, i):
        return {
            0: 'air',
            1: 'wall',
            2: 'goal',
            3: 'start',
            4: 'bpadu',
            5: 'bpadd',
            6: 'bpadr',
            7: 'bpadl',
            8: 'rose'
        }[i]

    def _get_start_x(self, tilesize):
        return 320 - ((len(self.level[0]) / 2) * tilesize) - (tilesize / 2)

    def _load_tiles(self):
        tilesize = 40
        start_x = self._get_start_x(tilesize)
        x = start_x
        y = 0

        for row in self.level:
            for col in row:
                self.tiles[self._get_name_of(col)].append(Sprite(load_image('res/tiles/' + str(col) + '.png'), Vec2(x, y), (tilesize, tilesize)))
                x += tilesize
            y += tilesize
            x = start_x
