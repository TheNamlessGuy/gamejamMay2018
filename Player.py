#encodng utf-8

from Gspace import WorldInterface, Sprite, load_image, collides_with, Vec2

VELSPEED = 1
GRAVITY = 0.6

class Player(WorldInterface):
    def __init__(self, start_pos):
        WorldInterface.__init__(self)
        
        #Player vars
        self.player = (Sprite(None, Vec2(start_pos.x, start_pos.y), Vec2(64, 64)))
        self.vel = Vec2(0,0)
        
        #Res
        self.res = {}
        self.res['player_right'] = [load_image("res/player/standing_right.png"), \
                                    load_image("res/player/running_right_1.png"), \
                                    load_image("res/player/running_right_2.png"), \
                                    load_image("res/player/running_right_3.png"), \
                                    load_image("res/player/running_right_4.png")]
        self.res['player_left'] = [load_image("res/player/standing_left.png"), \
                                    load_image("res/player/running_left_1.png"), \
                                    load_image("res/player/running_left_2.png"), \
                                    load_image("res/player/running_left_3.png"), \
                                    load_image("res/player/running_left_4.png")]
        
    def update(self, game_state):
        delta_vel = Vec2(0, -GRAVITY)
        
        if game_state['keyboard']['ctrl-up']:
            delta_vel.y += VELSPEED
        if game_state['keyboard']['ctrl-down']:
            delta_vel.y -= VELSPEED
        if game_state['keyboard']['ctrl-left']:
            delta_vel.x -= VELSPEED
        if game_state['keyboard']['ctrl-right']:
            delta_vel.x += VELSPEED
        
        self.vel.x += delta_vel.x
        self.vel.y += delta_vel.y
        
        self.player.pos.x += self.vel.x
        self.player.pos.y += self.vel.y
        
    def collision(self, world):
        #Check collision with each block
        
        #Check collision with each END
        pass
        
    def reset(self, game_state): 
        pass
        
        
