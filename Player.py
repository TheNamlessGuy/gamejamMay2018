#encodng utf-8

from Gspace import WorldInterface, Sprite, load_image, collides_with, Vec2

VELSPEED = 1
GRAVITY = 0.6

class Player(WorldInterface):
    def __init__(self, start_pos):
        WorldInterface.__init__(self)

        #Player vars
        self.player = (Sprite(None, Vec2(start_pos.x, start_pos.y), (35, 35)))
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

        self.current_sprite = 0
        self.switch_frame_timer = 3
        self.current_res = 'player_right'
        self.player.image = self.res[self.current_res][self.current_sprite]

        self.rotation_speed = 0
        self.player.rotation = self.rotation_speed

    def update(self, game_state, tiles):

        #Movement
        delta_vel = Vec2(0, 0)

        self.switch_frame_timer -= 1
        if self.switch_frame_timer == 0:
            self.current_sprite = (self.current_sprite + 1) % 5
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

        self.player.pos.x += self.vel.x
        self.player.pos.y += self.vel.y

        #Solid collision
        for wall in tiles['wall']:
            if collides_with(self.player.pos, (28,35), wall.pos, (40,40)):
                if self.rotation_speed < 90:
                    self.rotation_speed += 5
                self.vel.x = 0
                self.vel.y = 0

        #Win collision
        for goal in tiles['goal']:
            if collides_with(self.player.pos, (28,35), goal.pos, (40,40)):
                return True

        return False
