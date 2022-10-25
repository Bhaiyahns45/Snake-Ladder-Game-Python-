import time
from Pointer import *
from Draw import *
from Snake import *
from Ladder import *

# from Gameover import *

theme = 1

from SnakeLadderGame import *

from main import *

# import main

name1 = 'jja'

name2 = 'lla'


class Movement:
    '''

    this class keep the track of score of player movement w.r.t their dice score

    '''

    def __init__(self, screen):
        self.Pointer = None
        self.screen = screen
        self.Pointer = Pointer(self.screen)
        self.Draw = Draw(self.screen)
        self.score1 = 0
        self.score2 = 0
        self.dice1_x = 7
        self.dice1_y = 577
        self.dice2_x = 610
        self.dice2_y = 577

    # function to keep track the movement of players regarding their score
    def move(self, dice_score, player1, player2):

        ladder = {}
        snake = {}

        if theme == 1:
            snake = Snake.snake1
            ladder = Ladder.ladder1
        elif theme == 2:
            snake = Snake.snake2
            ladder = Ladder.ladder2
        elif theme == 3:
            snake = Snake.snake3
            ladder = Ladder.ladder3

        if player1 is True:

            self.score1 += dice_score
            # self.score1 = 100
            if self.score1 < 100:

                if self.score1 in ladder:
                    self.score1 = ladder[self.score1]
                    # SnakeLadderGame.music("music/ladder.wav")

                if self.score1 in snake:
                    self.score1 = snake[self.score1]
                    # SnakeLadderGame.music("music/snake.wav")

                self.Pointer.pointer(self.score1, self.score2)

            elif self.score1 == 100:
                self.Pointer.pointer(self.score1, self.score2)
                # SnakeLadderGame.music("music/winning.mp3")
                time.sleep(4)
                GameOver.game_over(name1.upper())

            else:
                self.score1 -= dice_score

        if player2 is True:
            self.score2 += dice_score

            if self.score2 < 100:
                if self.score2 in ladder:
                    self.score2 = ladder[self.score2]
                    # SnakeLadderGame.music("music/ladder.wav")

                if self.score2 in snake:
                    self.score2 = snake[self.score2]
                    # SnakeLadderGame.music("music/snake.wav")

                self.Pointer.pointer(self.score1, self.score2)

            elif self.score2 == 100:
                self.Pointer.pointer(self.score1, self.score2)
                # SnakeLadderGame.music("music/winning.mp3")
                time.sleep(4)
                GameOver.game_over(name2.upper())
            else:
                self.score2 -= dice_score
