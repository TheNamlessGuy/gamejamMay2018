#encoding: utf-8

import pygame

__sprite_db = {}
font = None

def font_init():
    global font
    font = pygame.font.Font('res/font.ttf', 30)

def load_image( path ):
    global sprite_db

    if not path in __sprite_db.keys():
        # crashes if the path is invalid
        sprite = pygame.image.load( path )
        # otherwise, it will be inserted to db here
        __sprite_db[ path ] = sprite
        return sprite
    else:
        return __sprite_db[ path ]

def text_to_sprite(text, antialias=True, color=(255, 255, 255), background=None):
    global __sprite_db
    global font

    name = 'text/' + text + '/' + str(antialias) + \
           ('/' + str(color[0]) + ',' + str(color[1]) + ',' + str(color[2]) + '/') if color is not None else '' + \
           ('/' + str(background[0]) + ',' + str(background[1]) + ',' + str(background[2])) if background is not None else ''
    
    if name not in __sprite_db.keys():
        sprite = font.render(text, antialias, color, background)
        __sprite_db['text/' + text] = sprite
        return sprite
    else:
        return __sprite_db[name]
    
# override this class to add features
class Sprite:
    def __init__( self, image, pos, size, angle=0.0, z=0, flip=False ):
        self.image          = image
        self.pos            = pos
        self.size           = size
        self.angle          = angle
        self.z              = z
        self.special_fx_id  = 0 # ugly hack that works <3
        self.flip           = flip

