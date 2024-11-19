import arcade
import arcade.gui
import math
from settings import *

DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 20


class GameHome(arcade.View):

    def __init__(self):
        super().__init__()
        self.text_angle = 0
        self.time_elapsed = 0.0
        self.heading_text = arcade.Text(
            text="Catch the Coins",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT - 60,
            color=arcade.color.YELLOW,
            font_size=40,
            anchor_x="center",
            anchor_y="center",
            bold=True,
            italic=True,
            font_name="Kenney Future"
        )

        self.returning_users = arcade.Text(
            text="Returning  Users",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT - 215,
            color=arcade.color.YELLOW,
            font_size=50,
            anchor_x="center",
            anchor_y="center",
            bold=True,
            italic=True,
            font_name="Kenney High"
        )
        arcade.set_background_color(arcade.color.COOL_GREY)

        self.manager = arcade.gui.UIManager()
        self.text_box_manager = arcade.gui.UIManager()
        self.text_box_manager.enable()
        self.manager.enable()

        self.v_box = arcade.gui.UIBoxLayout(space_between=10, vertical=False)
        self.r_box = arcade.gui.UIBoxLayout(space_between=10, vertical=False)

        right_button_g = arcade.load_texture("textures/rightgreenarrow1.jpg", width=150, height=50)
        right_button_w = arcade.load_texture("textures/rightwhitearrow1.jpg", width=150, height=50)
        self.user_text_box = (arcade.gui.UIInputText
                              (width=250,
                               height=30,
                               font_size=15,
                               font_name="Arial",
                               anchor_x="center",
                               anchor_y="center",
                               multiline=False, text="Enter User Name", text_color=arcade.color.BLACK,
                               # Set text color to black
                               color=arcade.color.WHITE,
                               visible=True)
                              )

        user_text_box_border = arcade.gui.UIBorder(child=self.user_text_box, border_width=2)
        self.confirm_box_button = arcade.gui.UITextureButton(texture=right_button_g, texture_hovered=right_button_w,
                                                             width=150)
        self.new_profile_button = arcade.gui.UIFlatButton(text="Create Profile", width=200)
        # self.v_box.add(self.user_text_box)
        self.v_box.add(user_text_box_border)
        self.v_box.add(self.confirm_box_button)

        self.r_box.add(self.new_profile_button.with_space_around(top=340))
        self.user_text_box.on_key_press = self.on_key_press
        self.user_text_box.on_mouse_press = self.on_mouse_press
        self.confirm_box_button.on_click = self.on_click_open
        self.new_profile_button.on_click = self.new_user_open

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                align_x=3,
                child=self.v_box),
        )
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                align_x=2,
                child=self.r_box),
        )
        self.new_users = arcade.Text(
            text="New  Users",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT - 425,
            color=arcade.color.YELLOW,
            font_size=50,
            anchor_x="center",
            anchor_y="center",
            bold=True,
            italic=True,
            font_name="Kenney High"
        )

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT and self.user_text_box.text == "Enter User Name":
            self.user_text_box.text = ""

    def on_click_open(self, event):
        if self.user_text_box.text == "" or self.user_text_box.text == "Enter User Name":
            message_box = arcade.gui.UIMessageBox(
                message_text=(
                    "Enter a username and try once again."
                ),
                width=450,
                height=150,
                buttons=["Ok"]
            )
            self.text_box_manager.add(message_box)
        elif self.user_text_box.text == "Thomas":
            self.prior_game_open(None)
        else:
            message_box = arcade.gui.UIMessageBox(
                message_text=(
                    "The User information was found!.\n"
                ),
                width=450,
                height=150,
                buttons=["Ok"]
            )
            self.text_box_manager.add(message_box)

    def new_user_open(self, event):
        new_player_v = New_Player()
        new_player_v.setup()
        self.window.show_view(new_player_v)

    def prior_game_open(self, event):
        prior_game_v = Prior_Game()
        prior_game_v.setup()
        self.window.show_view(prior_game_v)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            self.on_click_open(None)
        if key == arcade.key.ESCAPE:
            self.user_text_box.text = "Enter User Name"

    def load_sounds(self):
        # self.background_music = arcade.load_sound("sounds/Apoxode_-_Electric_1.wav")
        self.background_music = arcade.load_sound("sounds/Collision.wav")
        # self.move_up_sound = arcade.load_sound("sounds/Rising_putter.wav")
        # self.move_down_sound = arcade.load_sound("sounds/Falling_putter.wav")

    def setup(self):
        self.load_sounds()
        self.background_music.play(loop=False)

    def on_update(self, delta_time):
        self.time_elapsed += delta_time
        self.heading_text.angle = 6 * math.sin(self.time_elapsed * 2)
        self.heading_text.color = (
            int(255 * (0.5 + 0.5 * math.sin(self.time_elapsed * 3))),
            int(255 * (0.5 + 0.5 * math.sin(self.time_elapsed * 2))),
            int(255 * (0.5 + 0.5 * math.sin(self.time_elapsed * 4))),
        )
        self.heading_text.font_size = 70 + 5 * math.sin(self.time_elapsed * 2)
        self.heading_text.start_y = SCREEN_HEIGHT - 60 + 10 * math.sin(self.time_elapsed * 2)

    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.heading_text.draw()
        self.returning_users.draw()
        self.manager.draw()
        self.text_box_manager.draw()
        self.new_users.draw()


class New_Player(arcade.View):

    def __init__(self):
        super().__init__()
        self.text_angle = 0
        self.time_elapsed = 0.0
        self.heading_text = arcade.Text(
            text="Catch the Coins",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT - 60,
            color=arcade.color.YELLOW,
            font_size=40,
            anchor_x="center",
            anchor_y="center",
            bold=True,
            italic=True,
            font_name="Kenney Future"
        )

        self.new_player = arcade.Text(
            text="New Player",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT - 170,
            color=arcade.color.YELLOW,
            font_size=50,
            anchor_x="center",
            anchor_y="center",
            bold=True,
            italic=True,
            font_name="Kenney High"
        )
        arcade.set_background_color(arcade.color.COOL_GREY)

        self.manager = arcade.gui.UIManager()
        self.text_box_manager = arcade.gui.UIManager()
        self.text_box_manager.enable()
        self.manager.enable()

        self.v_box = arcade.gui.UIBoxLayout(space_between=10, vertical=False)
        self.r_box = arcade.gui.UIBoxLayout(space_between=10, vertical=False)

        back_button_f = arcade.load_texture("textures/icons8-back-button-50.png", width=50, height=50)
        back_button_h = arcade.load_texture("textures/icons8-back-button-50 (1).png", width=50, height=50)
        self.user_text_box = (arcade.gui.UIInputText
                              (width=250,
                               height=30,
                               font_size=15,
                               font_name="Arial",
                               anchor_x="center",
                               anchor_y="center",
                               multiline=False, text="Enter New User Name")
                              )
        right_button_g = arcade.load_texture("textures/rightgreenarrow1.jpg", width=150, height=50)
        right_button_w = arcade.load_texture("textures/rightwhitearrow1.jpg", width=150, height=50)
        user_text_box_border = arcade.gui.UIBorder(child=self.user_text_box, border_width=2)
        self.confirm_box_button = arcade.gui.UITextureButton(texture=right_button_g, texture_hovered=right_button_w,
                                                             width=150)
        self.back_button = arcade.gui.UITextureButton(texture=back_button_h, texture_hovered=back_button_f, width=50,
                                                      height=50)
        # self.v_box.add(self.user_text_box)
        self.v_box.add(user_text_box_border)
        self.v_box.add(self.confirm_box_button)
        self.r_box.add(self.back_button.with_space_around(top=350, left=500))
        self.user_text_box.on_key_press = self.on_key_press
        self.user_text_box.on_mouse_press = self.on_mouse_press
        self.back_button.on_click = self.new_user_open
        self.confirm_box_button.on_click = self.change_status
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                align_x=0,
                child=self.v_box),
        )
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                align_x=1,
                child=self.r_box),
        )
        self.new_name_available = arcade.Text(
            text="Username Found!",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT - 450,
            color=arcade.color.COOL_GREY,
            font_size=35,
            anchor_x="center",
            anchor_y="center",
            bold=True,
            italic=True,
            font_name="Kenney High Square"
        )

        self.new_name_unavailable = arcade.Text(
            text="Username Not Found!",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT - 520,
            color=arcade.color.COOL_GREY,
            font_size=35,
            anchor_x="center",
            anchor_y="center",
            bold=True,
            italic=True,
            font_name="Kenney High Square"
        )

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT and self.user_text_box.text == "Enter New User Name":
            self.user_text_box.text = ""

    def change_status(self, event):
        available = True
        if available is True:
            self.new_name_available.color = arcade.color.GREEN
        elif available is False:
            self.new_name_unavailable.color = arcade.color.RED

    def new_user_open(self, event):
        view = GameHome()
        view.setup()
        self.window.show_view(view)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            self.on_click_open(None)
        if key == arcade.key.ESCAPE:
            self.user_text_box.text = "Enter User Name"

    def load_sounds(self):
        # self.background_music = arcade.load_sound("sounds/Apoxode_-_Electric_1.wav")
        self.background_music = arcade.load_sound("sounds/Collision.wav")
        # self.move_up_sound = arcade.load_sound("sounds/Rising_putter.wav")
        # self.move_down_sound = arcade.load_sound("sounds/Falling_putter.wav")

    def setup(self):
        self.load_sounds()
        self.background_music.play(loop=False)

    def on_update(self, delta_time):
        self.time_elapsed += delta_time
        # self.text_angle = 10 * math.sin(self.time_elapsed * 2)

    def on_draw(self):
        self.clear()
        self.heading_text.rotation = self.text_angle
        self.heading_text.draw()
        self.new_player.draw()
        self.manager.draw()
        self.text_box_manager.draw()
        self.new_name_available.draw()
        self.new_name_unavailable.draw()


class Prior_Game(arcade.View):

    def __init__(self):
        super().__init__()
        self.text_angle = 0
        self.time_elapsed = 0.0
        self.heading_text = arcade.Text(
            text="atontalapur",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT - 20,
            color=arcade.color.YELLOW,
            font_size=15,
            anchor_x="center",
            anchor_y="center",
            font_name="Kenney Future"
        )
        #
        # self.new_player = arcade.Text(
        #     text="Level 1",
        #     start_x=SCREEN_WIDTH // 2,
        #     start_y=SCREEN_HEIGHT - 260,
        #     color=arcade.color.YELLOW,
        #     font_size=80,
        #     anchor_x="center",
        #     anchor_y="center",
        #     bold=True,
        #     italic=True,
        #     font_name="Kenney High"
        # )
        #
        # self.difficulty = arcade.Text(
        #     text="Difficulty: Easy",
        #     start_x=SCREEN_WIDTH // 2,
        #     start_y=SCREEN_HEIGHT - 360,
        #     color=arcade.color.YELLOW,
        #     font_size=30,
        #     anchor_x="center",
        #     anchor_y="center",
        #     bold=True,
        #     italic=True,
        #     font_name="Kenney High"
        # )
        arcade.set_background_color(arcade.color.COOL_GREY)

        self.manager = arcade.gui.UIManager()
        self.text_box_manager = arcade.gui.UIManager()
        self.text_box_manager.enable()
        self.manager.enable()

        self.level_1_box = arcade.gui.UIBoxLayout(space_between=10, vertical=False)
        self.level_2_box = arcade.gui.UIBoxLayout(space_between=10, vertical=False)
        self.level_3_box = arcade.gui.UIBoxLayout(space_between=10, vertical=False)
        self.level_4_box = arcade.gui.UIBoxLayout(space_between=10, vertical=False)
        self.level_5_box = arcade.gui.UIBoxLayout(space_between=10, vertical=False)

        one_white = arcade.load_texture("textures/levelOneWhite132.jpg")
        one_black = arcade.load_texture("textures/levelOneBlack150.jpg")
        self.level_one = arcade.gui.UITextureButton(texture=one_black, texture_hovered=one_white, width=300, height=114)


        self.level_1_box.add(self.level_one)
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                align_x=-400,
                align_y=200,
                child=self.level_1_box),
        )

        two_white = arcade.load_texture("textures/Level2_White.png")
        two_black = arcade.load_texture("textures/Level2_Black.png")
        self.level_two = arcade.gui.UITextureButton(texture=two_black, texture_hovered=two_white, width=300, height=114)

        self.level_2_box.add(self.level_two)
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                align_x=0,
                align_y=200,
                child=self.level_2_box),
        )

        three_white = arcade.load_texture("textures/Level3_White.png")
        three_black = arcade.load_texture("textures/Level3_Black.png")
        self.level_three = arcade.gui.UITextureButton(texture=three_black, texture_hovered=three_white, width=300, height=114)

        self.level_3_box.add(self.level_three)
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                align_x=400,
                align_y=200,
                child=self.level_3_box),
        )

        four_white = arcade.load_texture("textures/Level4_White.png")
        four_black = arcade.load_texture("textures/Level4_Black.png")
        self.level_four = arcade.gui.UITextureButton(texture=four_black, texture_hovered=four_white, width=300, height=114)

        self.level_4_box.add(self.level_four)
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                align_x=-200,
                align_y=-100,
                child=self.level_4_box),
        )

        five_white = arcade.load_texture("textures/Level5_White.png")
        five_black = arcade.load_texture("textures/Level5_Black.png")
        self.level_five = arcade.gui.UITextureButton(texture=five_black, texture_hovered=five_white, width=300,
                                                     height=114)

        self.level_5_box.add(self.level_five)
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                align_x=200,
                align_y=-100,
                child=self.level_5_box),
        )

        self.high_score = arcade.Text(
            text="high score: 0",
            start_x=SCREEN_WIDTH - 1140,
            start_y=SCREEN_HEIGHT - 170,
            color=arcade.color.GOLD,
            font_size=20,
            anchor_x="center",
            anchor_y="center",
            bold=True,
            italic=True,
            font_name="Kenney High Square"
        )

        self.trophy = arcade.load_texture("textures/trophy.jpeg")


    def load_sounds(self):
        # self.background_music = arcade.load_sound("sounds/Apoxode_-_Electric_1.wav")
        self.background_music = arcade.load_sound("sounds/Collision.wav")
        # self.move_up_sound = arcade.load_sound("sounds/Rising_putter.wav")
        # self.move_down_sound = arcade.load_sound("sounds/Falling_putter.wav")


    def setup(self):
        self.load_sounds()
        self.background_music.play(loop=False)


    def rules_open(self, event):
        rules = Rule_Page()
        rules.setup()
        self.window.show_view(rules)


    def on_update(self, delta_time):
        self.time_elapsed += delta_time


    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.heading_text.draw()
        # self.new_player.draw()
        self.manager.draw()
        #self.trophy.draw_scaled(55, 550, 0.2, 0.2)
        #self.high_score.draw()
        # self.difficulty.draw()


class Rule_Page(arcade.View):

    def __init__(self):
        super().__init__()
        self.text_angle = 0
        self.time_elapsed = 0.0
        self.heading_text = arcade.Text(
            text="atontalapur",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT - 20,
            color=arcade.color.YELLOW,
            font_size=15,
            anchor_x="center",
            anchor_y="center",
            font_name="Kenney Future"
        )

        self.new_player = arcade.Text(
            text="How to Play?",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT - 100,
            color=arcade.color.YELLOW,
            font_size=80,
            anchor_x="center",
            anchor_y="center",
            bold=True,
            italic=True,
            font_name="Kenney High"
        )
        arcade.set_background_color(arcade.color.COOL_GREY)

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.v_box = arcade.gui.UIBoxLayout(space_between=10, vertical=False)
        self.new_profile_button = arcade.gui.UIFlatButton(text="Play", width=200)

        self.v_box.add(self.new_profile_button.with_space_around(top=200))
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                align_x=0,
                child=self.v_box),
        )

    def load_sounds(self):
        # self.background_music = arcade.load_sound("sounds/Apoxode_-_Electric_1.wav")
        self.background_music = arcade.load_sound("sounds/Collision.wav")
        # self.move_up_sound = arcade.load_sound("sounds/Rising_putter.wav")
        # self.move_down_sound = arcade.load_sound("sounds/Falling_putter.wav")

    def setup(self):
        self.load_sounds()
        self.background_music.play(loop=False)

    def on_update(self, delta_time):
        self.time_elapsed += delta_time

    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.heading_text.rotation = self.text_angle
        self.heading_text.draw()
        self.new_player.draw()
        self.manager.draw()


if __name__ == "__main__":
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=False)
    home_view = GameHome()
    home_view.setup()
    window.show_view(home_view)
    arcade.run()
