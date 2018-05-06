#encoding: utf-8

from Gspace import *
from random import randint

class NormalEnd(WorldInterface):
    def __init__(self):
        WorldInterface.__init__(self)

        self.fridge_position = Vec2(130, 225)
        self.background = Sprite(load_image('res/smack_boom_bang.png'), Vec2(320, 240), (640, 480))
        self.fridge_open = load_image('res/fridge2_fullsize.png')
        self.fridge_closed = load_image('res/fridge1_fullsize.png')
        self.coyote_left = load_image('res/coyote_fullsize_left.png')
        self.coyote_right = load_image('res/coyote_fullsize_right.png')
        self.coyote_size = 0.7
        self.time_to_swap_da_images = 14
        self.no_smack_plz = 16
        self.coyote_rotations = [
            [-15.0, 5],
            [15.0, 5],
            [-15.0, 5],
            [15.0, 5],
            [-15.0, 5],
            
            [22, 10],
            
            [randint(0, 365), 1],
            [randint(0, 365), 1],
            [randint(0, 365), 1],
            [randint(0, 365), 1],
            [randint(0, 365), 1],
            [randint(0, 365), 1],
            [randint(0, 365), 1],
            
            [-15, 15],

            [randint(0, 365), 1],

            [15, 18],
            [15, 3],

            [randint(110, 190), 5],
            [randint(1, 366), 5],
            [randint(2, 366), 5],
            [randint(3, 366), 5],
            [randint(4, 366), 5],
        ]
        self.coyote_positions = [
            Vec2(730, 240),
            Vec2(700, 240),
            Vec2(660, 240),
            Vec2(570, 240),
            Vec2(480, 240),
            
            Vec2(420, 260),
            
            Vec2(420, 260),
            Vec2(420, 260),
            Vec2(420, 260),
            Vec2(420, 260),
            Vec2(420, 260),
            Vec2(420, 260),
            Vec2(420, 260),

            Vec2(420, 260),

            Vec2(420, 260),
            
            Vec2(420, 260),
            Vec2(420, 260),

            Vec2(480, 260),
            Vec2(520, 260),
            Vec2(590, 260),
            Vec2(640, 260),
            Vec2(780, 260),
        ]

        if len(self.coyote_rotations) != len(self.coyote_positions):
            raise "FUCK YOU THESE LISTS SHOULD HAVE THE SAME LENGTH"
        
        self.reset_animation()


    def update(self, gs):
        self.coyote_sprite.angle = self.coyote_rotations[self.animation_frame][0]
        self.coyote_sprite.pos = self.coyote_positions[self.animation_frame]

        self.real_frame += 1
        if self.real_frame >= self.coyote_rotations[self.animation_frame][1]:
            self.animation_frame += 1
            self.real_frame = 0

        if self.animation_frame == self.no_smack_plz:
            self.sprites = [x for x in self.sprites if x != self.background]
            
        if self.animation_frame == self.time_to_swap_da_images:
            self.sprites.insert(0, self.background)
            self.fridge_sprite.image = self.fridge_closed
            self.coyote_sprite.image = self.coyote_right
            
        if self.animation_frame >= len(self.coyote_positions):
            return gs['screen-levelselect']

        
    def reset(self, gs):
        self.reset_animation()

        self.sprites = []
        self.sprites.append(self.coyote_sprite)
        self.sprites.append(self.fridge_sprite)


    def reset_animation(self):
        self.real_frame = 0
        self.animation_frame = 0
        
        self.fridge_sprite = Sprite(
            self.fridge_open,
            self.fridge_position,
            (640, 480)
        )
        self.coyote_sprite = Sprite(
            self.coyote_left,
            self.coyote_positions[0],
            (int(414 * self.coyote_size), int(480 * self.coyote_size)),
            self.coyote_rotations[0]
        )
