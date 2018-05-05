#encoding: utf-8

from Gspace import *
from LevelSelect import *

if __name__ == '__main__':
    game_state = {}
    game_state['screen-levelselect'] = LevelSelect()

    game_state['blur'] = False
    game_state['camera'] = Vec2( 0.0, 0.0 )
    run_game(game_state['screen-levelselect'], game_state, 24)
