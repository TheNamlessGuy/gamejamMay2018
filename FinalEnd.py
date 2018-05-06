#encoding: utf-8

from Gspace import *
from random import randint

class FinalEnd(WorldInterface):
    def __init__(self):
        WorldInterface.__init__(self)

        self.fridge_position = Vec2(130, 225)
        self.background = Sprite(load_image('res/smack_boom_bang.png'), Vec2(320, 240), (640, 480))
        self.fridge_open = load_image('res/fridge2_fullsize.png')
        self.fridge_closed = load_image('res/fridge1_fullsize.png')
        self.coyote_left = load_image('res/coyote_fullsize_left.png')
        self.coyote_right = load_image('res/coyote_fullsize_right.png')
        self.back1 = load_image('res/powerup1.png')
        self.back2 = load_image('res/powerup2.png')
        self.spacebar = load_image('res/spacebar.png')
        self.it_ended_back = load_image('res/it_ended.png')
        self.coyote_size = 0.7
        self.powerup_frame = 6
        self.background_animation_time = 2
        self.coyote_rotations = [
            [-15.0, 5],
            [15.0, 5],
            [-15.0, 5],
            [15.0, 5],
            [-15.0, 5],
            
            [22, 10],

            [22, 10],

            [15, 48],
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
        ]

        self.fridge_positions = [
            Vec2(130, 225),
            Vec2(20, 180),
            Vec2(-130, 120),
            Vec2(-500, 90),
        ]
        self.fridge_rotations = [
            randint(0, 365),
            randint(0, 365),
            randint(0, 365),
            randint(0, 365),
        ]

        if len(self.coyote_rotations) != len(self.coyote_positions):
            raise "FUCK YOU THESE LISTS SHOULD HAVE THE SAME LENGTH"
        if len(self.fridge_rotations) != len(self.fridge_positions):
            raise "FFS DONT DO THIS TO MEEEEEEE"
        
        self.reset_animation()


    def update(self, gs):
        if self.it_ended:
            self.coyote_sprite.angle += 0.04
            self.coyote_sprite.pos.x += 0.05
            self.coyote_sprite.pos.y -= 0.2
            if gs['keyboard']['ctrl-action']:
                gs['keyboard']['ctrl-action'] -= 1
                return gs['screen-levelselect']
            return
        
        if not self.powering_up:
            self.coyote_sprite.angle = self.coyote_rotations[self.animation_frame][0]
        self.coyote_sprite.pos = self.coyote_positions[self.animation_frame]

        if self.animation_frame == self.powerup_frame and not self.powering_up:
            self.sprites.insert(0, self.background_sprite)
            self.sprites.append(self.spacebar_sprite)
            self.powering_up = True
        
        self.real_frame += 1
        if not self.powering_up:
            if self.real_frame >= self.coyote_rotations[self.animation_frame][1]:
                self.animation_frame += 1
                self.real_frame = 0
        else:
            if self.real_frame % self.background_animation_time == 0:
                self.background_sprite.image = self.back2 if self.background_sprite.image == self.back1 else self.back1
            if gs['keyboard']['ctrl-action']:
                gs['keyboard']['ctrl-action'] -= 1;
                self.rotation_speed -= 1
                if self.rotation_speed == 0:
                    self.powering_up = False
                    self.animation_frame += 1
                    self.sprites = [x for x in self.sprites if x != self.background_sprite and x != self.spacebar_sprite]
                    self.fridge_sprite.image = self.fridge_closed
                    self.coyote_sprite.image = self.coyote_right
                    self.commence_animating_the_fridge = True
            if self.real_frame >= self.rotation_speed:
                self.coyote_sprite.angle = randint(0, 360)
                self.real_frame = 0

        if self.commence_animating_the_fridge:
            self.fridge_sprite.angle = self.fridge_rotations[self.fridge_animation_frame]
            self.fridge_sprite.pos = self.fridge_positions[self.fridge_animation_frame]
            self.fridge_animation_frame += 1
            if self.fridge_animation_frame >= len(self.fridge_positions):
                self.fridge_animation_frame = len(self.fridge_positions) - 1
                    
        if self.animation_frame >= len(self.coyote_positions):
            self.it_ended = True
            self.sprites.insert(0, self.it_ended_sprite)

        
    def reset(self, gs):
        self.reset_animation()

        self.sprites = []
        self.sprites.append(self.coyote_sprite)
        self.sprites.append(self.fridge_sprite)


    def reset_animation(self):
        self.real_frame = 0
        self.animation_frame = 0
        self.powering_up = False
        self.rotation_speed = 10
        self.commence_animating_the_fridge = False
        self.fridge_animation_frame = 0
        self.it_ended = False
        
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
        self.background_sprite = Sprite(
            self.back1,
            Vec2(320, 240),
            (640, 480)
        )
        self.spacebar_sprite = Sprite(
            self.spacebar,
            Vec2(320, 400),
            (310, 54)
        )
        self.it_ended_sprite = Sprite(
            self.it_ended_back,
            Vec2(320, 240),
            (640, 480)
        )
