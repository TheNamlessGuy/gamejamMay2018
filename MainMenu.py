#encoding: utf-8

from Gspace import *

class MainMenu(WorldInterface):
    def __init__(self):
        WorldInterface.__init__(self)
        self.bg = Sprite(load_image('res/main_menu.png'), Vec2(320, 240), (640, 480))

    def update(self, gs):
        if gs['keyboard']['ctrl-action']:
            gs['keyboard']['ctrl-action'] -= 1
            return gs['screen-levelselect']

    def reset(self, gs):
        self.sprites.append(self.bg)
