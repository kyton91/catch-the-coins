from arcade import color

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 640
SCREEN_TITLE = "Sprite Bouncing Coins and Player"

LEVEL_SETTINGS = {
    "level_1": {
        "BACKGROUND_COLOR" : color.SHAMROCK_GREEN,
        "BACKGROUND_MUSIC" : "crates.wav",
        "OBSTACLE_IMAGE" : ":resources:images/tiles/boxCrate_double.png",
        "OBSTACLE_PIXELS_X" : 128,
        "OBSTACLE_PIXELS_Y" : 128,
        "OBSTACLE_SCALING" : 0.5,

        "COIN_IMAGE" : ":resources:images/items/coinGold.png",
        "COIN_SCALING" : 0.375,
        "NUM_COINS": 40,
        "COIN_OFFSET": 50,
        "COIN_FROM_BORDER" : 100,
        "COIN_MIN_SPEED": 2,
        "COIN_MAX_SPEED": 4,

        "PLAYER_IMAGE" : ":resources:images/animated_characters/male_adventurer/maleAdventurer_walk1.png",
        "PLAYER_SPAWN_X": SCREEN_WIDTH // 2,
        "PLAYER_SPAWN_Y": SCREEN_HEIGHT // 2,
        "PLAYER_SCALING" : 0.55,
        "PLAYER_SPEED": 6,
    },
    "level_2": {
        "BACKGROUND_COLOR" : color.WARM_BLACK,
        "BACKGROUND_MUSIC" : "castle.wav",
        "OBSTACLE_IMAGE" : ":resources:images/tiles/stone.png",
        "OBSTACLE_IMAGE_2" : ":resources:images/tiles/stoneMid.png",
        "OBSTACLE_IMAGE_3" : ":resources:images/tiles/stoneRight.png",
        "OBSTACLE_IMAGE_4" : ":resources:images/tiles/stoneLeft.png",
        "OBSTACLE_PIXELS_X" : 128,
        "OBSTACLE_PIXELS_Y" : 128,
        "OBSTACLE_SCALING" : 0.5,

        "COIN_IMAGE" : ":resources:images/items/coinBronze.png",
        "COIN_SCALING" : 0.375,
        "NUM_COINS": 10,
        "COIN_OFFSET": 50,
        "COIN_FROM_BORDER" : 100,
        "COIN_MIN_SPEED": 5,
        "COIN_MAX_SPEED": 6,

        "PLAYER_IMAGE" : ":resources:images/animated_characters/male_adventurer/maleAdventurer_walk1.png",
        "PLAYER_SPAWN_X": 64 * 10,
        "PLAYER_SPAWN_Y": 64 * 6 + 32,
        "PLAYER_SCALING" : 0.5,
        "PLAYER_SPEED": 7,
    },
    "level_3": {
        "BACKGROUND_COLOR" : color.ICEBERG,
        "BACKGROUND_MUSIC" : "winter.wav",
        "OBSTACLE_IMAGE" : ":resources:images/tiles/snow.png",
        "OBSTACLE_IMAGE_2" : ":resources:images/tiles/snowMid.png",
        "OBSTACLE_IMAGE_3" : ":resources:images/tiles/snowRight.png",
        "OBSTACLE_IMAGE_4" : ":resources:images/tiles/snowLeft.png",
        "OBSTACLE_PIXELS_X" : 128,
        "OBSTACLE_PIXELS_Y" : 128,
        "OBSTACLE_SCALING" : 0.5,

        "COIN_IMAGE" : ":resources:images/items/coinSilver.png",
        "COIN_SCALING" : 0.375,
        "NUM_COINS": 20,
        "COIN_OFFSET": 50,
        "COIN_FROM_BORDER" : 100,
        "COIN_MIN_SPEED": 3,
        "COIN_MAX_SPEED": 5,

        "PLAYER_IMAGE" : ":resources:images/animated_characters/male_adventurer/maleAdventurer_walk1.png",
        "PLAYER_SPAWN_X": SCREEN_WIDTH // 2,
        "PLAYER_SPAWN_Y": SCREEN_HEIGHT // 2 - 64,
        "PLAYER_SCALING" : 0.55,
        "PLAYER_SPEED": 10,
    },
    "level_4": {
        "BACKGROUND_COLOR" : color.DESERT_SAND,
        "BACKGROUND_MUSIC" : "beach.wav",
        "OBSTACLE_IMAGE" : "resources/water_rounded.png",
        "OBSTACLE_IMAGE_2" : ":resources:images/tiles/water.png",
        "OBSTACLE_IMAGE_3" : ":resources:images/tiles/waterTop_low.png",
        "OBSTACLE_IMAGE_4" : "resources/waterTop_low_flipped.png",
        "OBSTACLE_PIXELS_X" : 128,
        "OBSTACLE_PIXELS_Y" : 128,
        "OBSTACLE_SCALING" : 0.5,

        "COIN_IMAGE" : ":resources:images/items/gemYellow.png",
        "COIN_SCALING" : 0.25,
        "NUM_COINS": 50,
        "COIN_OFFSET": 50,
        "COIN_FROM_BORDER" : 100,
        "COIN_MIN_SPEED": 1,
        "COIN_MAX_SPEED": 2,

        "PLAYER_IMAGE" : ":resources:images/animated_characters/male_adventurer/maleAdventurer_walk1.png",
        "PLAYER_SPAWN_X": 64 * 10 + 32,
        "PLAYER_SPAWN_Y": 64 * 8,
        "PLAYER_SCALING" : 0.4,
        "PLAYER_SPEED": 5,
    },
    "level_5": {
        "BACKGROUND_COLOR" : color.DARK_RED,
        "BACKGROUND_MUSIC" : "lava.mp3",
        "OBSTACLE_IMAGE" : "resources/lava_rounded.png",
        "OBSTACLE_IMAGE_2" : ":resources:images/tiles/lava.png",
        "OBSTACLE_IMAGE_3" : ":resources:images/tiles/lavaTop_low.png",
        "OBSTACLE_IMAGE_4" : "resources/lavaTop_low_flipped.png",
        "OBSTACLE_PIXELS_X" : 128,
        "OBSTACLE_PIXELS_Y" : 128,
        "OBSTACLE_SCALING" : 0.5,

        "COIN_IMAGE" : ":resources:images/items/gemBlue.png",
        "COIN_SCALING" : 0.375,
        "NUM_COINS": 1,
        "COIN_OFFSET": 50,
        "COIN_FROM_BORDER" : 100,
        "COIN_MIN_SPEED": 1.5,
        "COIN_MAX_SPEED": 3.5,

        "PLAYER_IMAGE" : ":resources:images/animated_characters/male_adventurer/maleAdventurer_walk1.png",
        "PLAYER_SPAWN_X": 64 * 11,
        "PLAYER_SPAWN_Y": 64 * 4,
        "PLAYER_SCALING" : 0.55,
        "PLAYER_SPEED": 5,
    },
}