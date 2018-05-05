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
            ('level-1', Sprite(text_to_sprite('Lvl 1'), Vec2(50, 20), (35, 50))),
            ('level-2', Sprite(text_to_sprite('Lvl 2'), Vec2(50, 90), (35, 50))),
            ('level-3', Sprite(text_to_sprite('Lvl 3'), Vec2(50, 160), (35, 50)))
        ]
        for level in self.levels:
            self.sprites.append(level[1])

        self.current_level = 0
        self.arrow = Sprite(text_to_sprite('>'), Vec2(20, self.levels[self.current_level][1].pos.y), (25, 25))
        self.sprites.append(self.arrow)
