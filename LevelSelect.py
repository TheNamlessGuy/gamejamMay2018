#encoding: utf-8

from Gspace import *

class LevelSelect(WorldInterface):
    def __init__(self):
        WorldInterface.__init__(self)

    def update(self, gs):
        pass

    def reset(self, gs):
        self.sprites = []

        self.levels = [
            ('level-1', Sprite(text_to_sprite('Lvl 1'), Vec2(320, 240), (500, 500)))
            #('level-2', Sprite(text_to_sprite('Lvl 1'), Vec2(320, 240), (500, 500)))
        ]

        self.current_level = 0
        self.arrow = text_to_sprite('>')

        for level in self.levels:
            self.sprites.append(level[1])
