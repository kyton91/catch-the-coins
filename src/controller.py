import arcade

from settings import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
from game_home import GameHome
from new_player import New_Player
from level_screen import Level_Screen
from rule_page import Rule_Page
from pause_view import PauseView
from game import Game
from win_game import WinGame
from loose_game import LooseGame

import controller_manager

class Controller(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.set_location(0, 30)

        controller_manager.controller = self

        self.to_game_home()
        arcade.run()
    
    def to_game_home(self):
        view = GameHome()
        view.setup()
        self.show_view(view)
    
    def to_new_player(self):
        view = New_Player()
        view.setup()
        self.show_view(view)

    def to_level_screen(self):
        view = Level_Screen()
        view.setup()
        self.show_view(view)
    
    def to_rule_page(self, level):
        view = Rule_Page(level)
        view.setup()
        self.show_view(view)
    
    def to_game(self, level):
        view = Game(level)
        view.setup()
        self.show_view(view)
    
    def to_pause_menu(self, game_view):
        view = PauseView(game_view)
        self.show_view(view)

    def to_win(self, time_taken):
        view = WinGame(time_taken)
        view.setup()
        self.show_view(view)

    def to_loose(self, num_coins):
        view = LooseGame(num_coins)
        view.setup()
        self.show_view(view)

if __name__ == "__main__":
    controller = Controller()