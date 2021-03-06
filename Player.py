#encodng utf-8

from Gspace import WorldInterface, Sprite, load_image, collides_with, Vec2

MAX_VEL = 15
VELSPEED = 1
GRAVITY = 0.2
BOUNCE_MUL = 1.1

class Player(WorldInterface):
    def __init__(self, start_pos):
        WorldInterface.__init__(self)

        #Player vars
        self.player = (Sprite(None, Vec2(start_pos.x, start_pos.y), (35, 35)))
        self.vel = Vec2(0,0)
        self.last_pos = Vec2(0,0)

        #Res
        self.res = {}
        self.res['player_right'] = [load_image("res/player/standing_right.png"), \
                                    load_image("res/player/running_right_1.png"), \
                                    load_image("res/player/standing_right.png"), \
                                    load_image("res/player/running_right_3.png")]
        self.res['player_left'] = [load_image("res/player/standing_left.png"), \
                                    load_image("res/player/running_left_1.png"), \
                                    load_image("res/player/standing_left.png"), \
                                    load_image("res/player/running_left_3.png")]

        self.current_sprite = 0
        self.switch_frame_timer = 3
        self.current_res = 'player_right'
        self.player.image = self.res[self.current_res][self.current_sprite]

        self.rotation_speed = 0
        self.player.rotation = self.rotation_speed

    def update(self, game_state, tiles):

        hit_wall = False

        #Movement
        gravity_x = -GRAVITY if self.vel.x > 0 else GRAVITY
        
        
        delta_vel = Vec2(gravity_x, GRAVITY)

        self.switch_frame_timer -= 1
        if self.switch_frame_timer == 0:
            self.current_sprite = (self.current_sprite + 1) % 4
            self.switch_frame_timer = 3

        if game_state['keyboard']['ctrl-up']:
            delta_vel.y -= VELSPEED
        if game_state['keyboard']['ctrl-down']:
            delta_vel.y += VELSPEED
        if game_state['keyboard']['ctrl-left']:
            if self.current_res != 'player_left':
                self.current_sprite = 0
                self.current_res = 'player_left'
            delta_vel.x -= VELSPEED
        if game_state['keyboard']['ctrl-right']:
            if self.current_res != 'player_right':
                self.current_sprite = 0
                self.current_res = 'player_right'
            delta_vel.x += VELSPEED

        self.player.image = self.res[self.current_res][self.current_sprite]

        if (self.rotation_speed > 0): self.rotation_speed -= 0.5
        self.player.rotation = (self.player.rotation + self.rotation_speed) % 360

        self.vel.x += delta_vel.x
        self.vel.y += delta_vel.y
        
        self.vel.x = min(self.vel.x, MAX_VEL)
        self.vel.y = min(self.vel.y, MAX_VEL)

        self.player.pos.x += self.vel.x
        self.player.pos.y += self.vel.y

        #Solid collision
        for wall in tiles['wall']:
            if collides_with(self.player.pos, (26,32), wall.pos, (40,40)):
                if self.rotation_speed < 90:
                    self.rotation_speed += 5
                self.collision(wall)
                hit_wall = True

        for bpadl in tiles['bpadl']:
            if collides_with(self.player.pos, (26,32), bpadl.pos, (40,40)):
                self.vel.x = -MAX_VEL

        #Win collision
        for goal in tiles['goal']:
            if collides_with(self.player.pos, (26,32), goal.pos, (40,40)):
                return True
        
        if hit_wall is False:        
            self.last_pos.x = self.player.pos.x
            self.last_pos.y = self.player.pos.y
        
        return False
       
    def collision(self, wall):
        diff_x = self.player.pos.x - wall.pos.x
        diff_y = self.player.pos.y - wall.pos.y

        if self.player.pos.x == self.last_pos.x and self.player.pos.y == self.last_pos.y:
            return
        
        self.player.pos.x = self.last_pos.x
        self.player.pos.y = self.last_pos.y
        
        #Collision on x
        if abs(diff_x) > abs(diff_y):
            self.vel.x = -self.vel.x * BOUNCE_MUL
            if diff_x > 0:
                pass
            else:
                pass
        #Collision on y
        else:
            self.vel.y = -self.vel.y * BOUNCE_MUL
            if diff_y > 0:
                pass
            else:
                pass
        
        #print("diff_x:", diff_x, " diff_y:", diff_y)

