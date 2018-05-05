#encoding: utf-8

from Gspace import *
import math
import pygame

class MainMenu(WorldInterface):
    def __init__(self):
        WorldInterface.__init__(self)
        self.bg = Sprite(load_image('res/main_menu.png'), Vec2(320, 240), (640, 480))
        self.space = Sprite(load_image('res/spacebar.png'), Vec2(320, 420), (310, 54))

    def update(self, gs):
        if gs['keyboard']['ctrl-action']:
            gs['keyboard']['ctrl-action'] -= 1
            return gs['screen-levelselect']

        self.space.pos.x = 320 - math.cos(math.radians(pygame.time.get_ticks())) * 5
        self.space.pos.y = 420 + math.sin(math.radians(pygame.time.get_ticks())) * 5

    def reset(self, gs):
        self.sprites.append(self.bg)
        self.sprites.append(self.space)
