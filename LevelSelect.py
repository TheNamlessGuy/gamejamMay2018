#encoding: utf-8

from Gspace import *

class LevelSelect(WorldInterface):
    def __init__(self):
        WorldInterface.__init__(self)

    def update(self, gs):
        if gs['keyboard']['ctrl-up']:
            self.current_level -= 1
            if self.current_level < 0: self.current_level = len(self.levels) - 1
            gs['keyboard']['ctrl-up'] -= 1
        elif gs['keyboard']['ctrl-down']:
            self.current_level += 1
            if self.current_level >= len(self.levels): self.current_level = 0
            gs['keyboard']['ctrl-down'] -= 1
        elif gs['keyboard']['ctrl-action']:
            return gs[self.levels[self.current_level][0]]

        self.arrow.pos.y = self.levels[self.current_level][1].pos.y

    def reset(self, gs):
        self.sprites = []

        # Y offset between levels: 70 (height + 20)
        self.levels = [
            ('level-1', Sprite(load_image('res/text/Lvl1.png'), Vec2(75,  20), (75, 50))),
            ('level-2', Sprite(load_image('res/text/Lvl2.png'), Vec2(75,  90), (75, 50))),
            ('level-3', Sprite(load_image('res/text/Lvl3.png'), Vec2(75, 160), (75, 50)))
        ]
        for level in self.levels:
            self.sprites.append(level[1])

        self.current_level = 0
        self.arrow = Sprite(load_image('res/text/arrow.png'), Vec2(20, self.levels[self.current_level][1].pos.y), (35, 50))
        self.sprites.append(self.arrow)
