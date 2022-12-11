from game.casting.color import Color

# --------------------------------------------------------------------------------------------------
# GENERAL GAME CONSTANTS
# --------------------------------------------------------------------------------------------------

# GAME
GAME_TITLE = "MST3K Pong"
FRAME_RATE = 48

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "pong/assets/fonts/retro.ttf"
FONT_SMALL = 21
FONT_LARGE = 40

# SOUND
HIT_SOUND = "pong/assets/sounds/hit.wav"
START_SOUND = "pong/assets/sounds/open_door.wav"
GAMEOVER_SOUND = "pong/assets/sounds/end_twang.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)

# KEYS
UP = "w","up"
DOWN = "s","down"
ENTER = "enter"


# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4



# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP1 = "stat1"
STATS_GROUP2 = "stat2"

# HUD
HUD_MARGIN = 15
SCORE_GROUP = "score1","score2"
SCORE_FORMAT = "Team Crow: {}","Team Servo: {}"

# BALL
BALL_GROUP = "balls"
BALL_IMAGE = "pong/assets/images/mst3k_logo_60.png"
BALL_WIDTH = 60
BALL_HEIGHT = 60
BALL_VELOCITY = 6

# SILHOUETTE
SILHOUETTE_GROUP = "silhouette"
SILHOUETTE_IMAGE = "pong/assets/images/silhouette.png"
SILHOUETTE_WIDTH = 200
SILHOUETTE_HEIGHT = 64
SILHOUETTE_VELOCITY = 1

# RACKET
RACKET_GROUP = "racket1","racket2",
RACKET_IMAGES = {
    "left": ["pong/assets/images/sol.png"],
    "right" : ["pong/assets/images/sol.png"]
}
RACKET_WIDTH =  28
RACKET_HEIGHT =  125
RACKET_RATE = 6
RACKET_VELOCITY = 7

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
MOVIE_SIGN_START = "WE'VE GOT MOVIE SIGN!!!"
WAS_GOOD_GAME = "GAME OVER!"