import time
import random
from pygame.locals import *
from pygame import mixer
from Snake import *
from Ladder import *
from Pointer import *

# global variable
GameOver = False


class SnakeLadderGame:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake Ladder Game")
        self.screen = pygame.display.set_mode((670, 640))

        # coordinate of dice
        self.x1 = 7
        self.y1 = 577
        self.x2 = 610
        self.y2 = 577

        self.wait()
        self.screen = pygame.display.set_mode((670, 640))
        self.Pointer = Pointer(self.screen)
        self.Draw = Draw(self.screen)
        self.Movement = Movement(self.screen)
        self.ludo_interface()
        pygame.display.flip()

    # display background interface
    def ludo_interface(self):
        self.screen = pygame.display.set_mode((670, 640))
        font = pygame.font.SysFont('ariel', 20, bold=True)
        line1 = font.render(name1.split()[0].upper(), True, (255, 0, 0))
        self.screen.blit(line1, (5, 540))
        font = pygame.font.SysFont('ariel', 20, bold=True)
        line1 = font.render(name2.split()[0].upper(), True, (19, 163, 246))
        self.screen.blit(line1, (608, 540))
        self.Draw.display(SnakeLadderGame.choose_theme(theme), 540, 638, 62, 0)
        self.Draw.display('image/red.png', 22, 22, 68, 600)
        self.Draw.display('image/blue.png', 22, 22, 92, 600)
        self.Draw.dice(1, self.x1, self.y1)
        self.Draw.dice(1, self.x2, self.y2)

    # restart the game
    def restart(self):
        SnakeLadderGame.music("music/starting_music.mp3")
        self.Movement.score1 = 0
        self.Movement.score2 = 0
        print("\n----Game Restarted---------------------------------------------")
        print("\nPlayer1 Score:", 0)
        print("Player2 Score:", 0)
        self.ludo_interface()
        pygame.display.flip()

    # wait for few second at the starting of game to display the rule for game
    def wait(self):
        font = pygame.font.SysFont('ariel', 52, bold=True)
        line1 = font.render("Game Start With 1", True, (242, 12, 12), (255, 255, 255))
        back = pygame.image.load(SnakeLadderGame.choose_theme(theme))
        self.screen.blit(pygame.transform.scale(back, (540, 638)), (62, 0))
        self.screen.blit(line1, (155, 300))
        pygame.display.flip()
        SnakeLadderGame.music("music/starting_music.mp3")
        time.sleep(8)

    # to choose the different theme for game
    @staticmethod
    def choose_theme(x):

        d_theme = {1: 'image/theme1.jpeg', 2: 'image/theme2.jpeg', 3: 'image/theme3.jpeg',
                   4: 'image/theme4.jpeg', 5: 'image/theme5.jpeg', 6: 'image/theme6.jpeg'}

        return d_theme[x]

    # for playing the music
    @staticmethod
    def music(music):
        mixer.init()
        mixer.music.load(music)
        mixer.music.set_volume(0.5)
        mixer.music.play()

    # game over function
    @staticmethod
    def game_over(player):

        global GameOver
        font = pygame.font.SysFont('ariel', 52, bold=True)
        line1 = font.render(f"{player} Won!!!", True, (15, 137, 219))
        line2 = font.render("Press ESC to exit ", True, (173, 219, 15))
        line3 = font.render("Press Enter to Restart", True, (173, 219, 15))
        screen = pygame.display.set_mode((670, 640))
        back = pygame.image.load('image/game_over.png')
        screen.blit(pygame.transform.scale(back, (540, 638)), (62, 0))
        screen.blit(line1, (180, 130))
        screen.blit(line2, (180, 470))
        screen.blit(line3, (130, 530))
        pygame.display.flip()

        GameOver = True

    # to run the game
    def run(self):
        running = True
        global GameOver
        GameOver = False
        open1 = 0
        open2 = 0
        turn1 = False
        turn2 = False

        print("\nPlayer1 Score:", 0)
        print("Player2 Score:", 0)

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    # press escape to end the game
                    if event.key == K_ESCAPE:
                        running = False

                    # press enter to restart the game
                    if event.key == K_RETURN:
                        GameOver = False
                        open1 = 0
                        open2 = 0
                        turn1 = False
                        turn2 = False
                        self.restart()

                    if not GameOver:
                        # player1 rolling the dice
                        if event.key == K_1 and turn1 is not True:
                            turn1 = True
                            turn2 = False
                            self.music('music/rolling_music.mp3')
                            dice_score = random.randint(1, 6)
                            print("\nPlayer1 Dice:", dice_score)
                            self.Draw.dice(dice_score, self.x1, self.y1)

                            # Player1 open
                            if dice_score == 1 and open1 == 0:
                                self.music('music/open.wav')
                                print("\n->Player1 Open")
                                self.Movement.move(dice_score, True, False)
                                pygame.display.flip()
                                open1 = 1
                            elif open1 == 1:

                                self.Movement.move(dice_score, True, False)

                        # player1 rolling the dice
                        if event.key == K_2 and turn2 is not True:
                            turn2 = True
                            turn1 = False
                            self.music('music/rolling_music.mp3')
                            dice_score = random.randint(1, 6)
                            print("\nPlayer2 Dice:", dice_score)
                            self.Draw.dice(dice_score, self.x2, self.y2)

                            # Player2 open
                            if dice_score == 1 and open2 == 0:
                                self.music('music/open.wav')
                                print("\n->Player2 Open")
                                self.Movement.move(dice_score, False, True)
                                pygame.display.flip()
                                open2 = 1
                            elif open2 == 1:
                                self.Movement.move(dice_score, False, True)


class Movement:
    """ this class keep the track of score of player movement w.r.t their dice score """

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

        ladder = Ladder.ladder(theme)
        snake = Snake.snake(theme)

        if player1 is True:

            self.score1 += dice_score
            # self.score1=100
            if self.score1 < 100:

                if self.score1 in ladder:
                    print("\n++ Player1 Ladder ++")
                    self.score1 = ladder[self.score1]
                    SnakeLadderGame.music("music/ladder.wav")

                if self.score1 in snake:
                    print("\n-- Player1 Snake --")
                    self.score1 = snake[self.score1]
                    SnakeLadderGame.music("music/snake.wav")
                self.Draw.display(SnakeLadderGame.choose_theme(theme), 540, 638, 62, 0)
                self.Pointer.pointer(self.score1, self.score2)

            elif self.score1 == 100:
                self.Draw.display(SnakeLadderGame.choose_theme(theme), 540, 638, 62, 0)
                self.Pointer.pointer(self.score1, self.score2)
                SnakeLadderGame.music("music/winning.mp3")
                print("\nPlayer1 Won!!")
                time.sleep(4)
                SnakeLadderGame.game_over(name1.upper())
            else:
                self.score1 -= dice_score

        if player2 is True:
            self.score2 += dice_score

            if self.score2 < 100:
                if self.score2 in ladder:
                    print("\n++ Player2 Ladder ++")
                    self.score2 = ladder[self.score2]
                    SnakeLadderGame.music("music/ladder.wav")

                if self.score2 in snake:
                    print("\n-- Player2 Snake --")
                    self.score2 = snake[self.score2]
                    SnakeLadderGame.music("music/snake.wav")
                self.Draw.display(SnakeLadderGame.choose_theme(theme), 540, 638, 62, 0)
                self.Pointer.pointer(self.score1, self.score2)

            elif self.score2 == 100:
                self.Draw.display(SnakeLadderGame.choose_theme(theme), 540, 638, 62, 0)
                self.Pointer.pointer(self.score1, self.score2)
                SnakeLadderGame.music("music/winning.mp3")
                print("\nPlayer2 won!!")
                time.sleep(4)
                SnakeLadderGame.game_over(name2.upper())
            else:
                self.score2 -= dice_score


""" main function """

if __name__ == "__main__":
    print("\n-------------------------------Snake Ladder Game Started---------------------------------")
    print("=> Game Rule:-")
    print("-> 2 Player game")
    print("-> Starting position of both player is 1")
    print("-> Press 1 for player1 turn and Press 2 for player2 turn")
    print("-> Reach 100 to win the game")
    print("-> Game Start with 1")
    print("-> Ladder refers to climbing up w.r.t position of ladder[score increase]")
    print("-> Snake refers to falling down w.r.t position of snake[score decrease]")

    print("-> Press ENTER key to restart the game]")
    print("-> Press ESCAPE key to exit the game")

    name1 = input("\nEnter Player1 Name: ")

    name2 = input("\nEnter Player1 Name: ")

    theme = int(input("\nChoose the theme [1,2,3,4,5,6]: "))

    try:
        game = SnakeLadderGame()
        game.run()
    except:
        print("\nWarning!! Choose From Available Theme")
    finally:
        print("\nExit!")
