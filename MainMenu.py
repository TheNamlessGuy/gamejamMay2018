#encoding: utf-8

from Gspace import *
import math
import pygame

class MainMenu(WorldInterface):
    def __init__(self):
        WorldInterface.__init__(self)
        self.bg = Sprite(load_image('res/main_menu.png'), Vec2(320, 240), (640, 480))
        self.space = Sprite(load_image('res/spacebar.png'), Vec2(320, 420), (310, 54))
        self.tear = Sprite(load_image('res/tear.png'), Vec2(388, 247), (8, 8))

    def update(self, gs):
        if gs['keyboard']['ctrl-action']:
            gs['keyboard']['ctrl-action'] -= 1
            return gs['screen-levelselect']

        self.space.pos.x = 320 - math.cos(math.radians(pygame.time.get_ticks())) * 5
        self.space.pos.y = 420 + math.sin(math.radians(pygame.time.get_ticks())) * 5

        self.tear.pos.y += (self.tear.pos.y / self.tear_offset)
        self.tear_offset -= 4
        if (self.tear.pos.y > 480):
            self.tear.pos.y = 247
            self.tear_offset = 100

    def reset(self, gs):
        self.tear_offset = 100
        
        self.sprites.append(self.bg)
        self.sprites.append(self.tear)
        self.sprites.append(self.space)
