import os
import random

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
ROCK_AND_GEM = ["*", "o"]
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
YELLOW = Color(249, 215, 28)

#Add game level
DEFAULT_ARTIFACTS = None
GAME_LEVEL = input("Choose a dificculty (Normal / Hard): ").title()
if GAME_LEVEL.lower() == "normal":
    DEFAULT_ARTIFACTS = 40
else: DEFAULT_ARTIFACTS = 100

def main():
    
    # create the cast
    cast = Cast()
    
    # create the scoreboard banner
    scoreboard = Actor()
    scoreboard.set_font_size(FONT_SIZE)
    scoreboard.set_color(YELLOW)
    scoreboard.set_position(Point(CELL_SIZE, 30))
    cast.add_actor("banners", scoreboard)

    # create the game difficulty
    level_board = Actor()
    level_board.set_font_size(FONT_SIZE)
    level_board.set_text(f"Level: {GAME_LEVEL}")
    level_board.set_color(WHITE)
    level_board.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("level_board", level_board)
    
    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y / 2)
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    # create the artifacts
    with open(DATA_PATH) as file:
        data = file.read()
        messages = data.splitlines()

    for n in range(DEFAULT_ARTIFACTS):
        text = random.choice(ROCK_AND_GEM)
        # text = chr(random.randint(33, 126))
        # message = text

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        cast.add_actor("artifacts", artifact)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()