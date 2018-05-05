#encoding: utf-8

from Gspace import *
from LevelSelect import *
from Level1 import *
from Level2 import *
from MainMenu import *

GAME_TITLE = "Coyote King of the Bouncing Palace Realm"

if __name__ == '__main__':
    pygame.display.set_caption("lul")
    game_state = {}
    game_state['screen-mainmenu'] = MainMenu()
    game_state['screen-levelselect'] = LevelSelect()

    game_state['level-1'] = Level1()
    game_state['level-2'] = Level2()

    game_state['blur'] = False
    game_state['camera'] = Vec2( 0.0, 0.0 )
    run_game(game_state['screen-mainmenu'], game_state, 24, GAME_TITLE)
