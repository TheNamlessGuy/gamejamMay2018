#encoding: utf-8

from WorldInterface import *
from Sprite import *
from Vec2 import *
from Player import *

class Level(WorldInterface):
    def __init__(self):
        WorldInterface.__init__(self)
        self.objects = []

        self._tile_translator = {
            0: 'air',
            1: 'wall',
            2: 'goal',
            3: 'start',
            4: 'bpadu',
            5: 'bpadd',
            6: 'bpadr',
            7: 'bpadl',
            8: 'rose'
        }

        self.tiles = {}
        for key in self._tile_translator:
            self.tiles[self._tile_translator[key]] = []

        self._load_tiles()

    def _get_name_of(self, i):
        return self._tile_translator[i]

    def _get_startvalue(self, tilesize, levelsize, initial):
        return initial - ((levelsize / 2.0) * tilesize) + (tilesize / 2)

    def _load_tiles(self):
        tilesize = 40
        start_x = self._get_startvalue(tilesize, len(self.level[0]), 320)
        x = start_x
        y = self._get_startvalue(tilesize, len(self.level), 240)

        for row in self.level:
            for col in row:
                self.tiles[self._get_name_of(col)].append(Sprite(load_image('res/tiles/' + str(col) + '.png'), Vec2(x, y), (tilesize, tilesize)))
                x += tilesize
            y += tilesize
            x = start_x

    def _update(self, gs, winscreen):
        win = self.player.update(gs, self.tiles)
        if win:
            return gs[winscreen]

        if gs['keyboard']['ctrl-reset']:
            gs['keyboard']['ctrl-reset'] -= 1
            self.reset(gs)
            return

    def _reset(self, gs):
        self.player = Player(self.tiles['start'][0].pos)

        self.sprites = []

        for tiletype in self.tiles:
            for tile in self.tiles[tiletype]:
                self.sprites.append(tile)

        self.sprites.append(self.player.player)
