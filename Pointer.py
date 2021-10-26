from Draw import *

# coordinate of number form 1-100 in snake ladder board

coord = {1: (70, 580),   2: (92, 590),   3: (147, 590),  4: (202, 590),  5: (257, 590), 6: (312, 590),
         7: (367, 590),  8: (422, 590),  9: (470, 590),  10: (522, 590), 11: (522, 530), 12: (470, 530),
         13: (422, 530), 14: (367, 530), 15: (312, 530), 16: (257, 530), 17: (202, 530), 18: (147, 530),
         19: (92, 530),  20: (37, 530),  21: (37, 470),  22: (92, 470),  23: (147, 470), 24: (202, 470),
         25: (257, 470), 26: (312, 470), 27: (367, 470), 28: (422, 470), 29: (470, 470), 30: (522, 470),
         31: (522, 410), 32: (470, 410), 33: (422, 410), 34: (367, 410), 35: (312, 410), 36: (257, 410),
         37: (202, 410), 38: (147, 410), 39: (92, 410),  40: (37, 410),  41: (37, 340),  42: (92, 340),
         43: (147, 340), 44: (202, 340), 45: (257, 340), 46: (312, 340), 47: (367, 340), 48: (422, 340),
         49: (470, 340), 50: (522, 340), 51: (522, 278), 52: (470, 278), 53: (422, 278), 54: (367, 278),
         55: (312, 278), 56: (257, 278), 57: (202, 278), 58: (147, 278), 59: (92, 278),  60: (37, 278),
         61: (37, 215),  62: (92, 215),  63: (147, 215), 64: (202, 215), 65: (257, 215), 66: (312, 215),
         67: (367, 215), 68: (422, 215), 69: (470, 215), 70: (522, 215), 71: (522, 152), 72: (470, 152),
         73: (422, 152), 74: (367, 152), 75: (312, 152), 76: (257, 152), 77: (202, 152), 78: (147, 152),
         79: (92, 152),  80: (37, 152),  81: (37, 90),   82: (92, 90),   83: (147, 90),  84: (202, 90),
         85: (257, 90),  86: (312, 90),  87: (367, 90),  88: (422, 90),  89: (470, 90),  90: (522, 90),
         91: (522, 28),  92: (470, 28),  93: (422, 28),  94: (367, 28),  95: (312, 28),  96: (257, 28),
         97: (202, 28),  98: (147, 28),  99: (92, 28),   100: (37, 28)}


class Pointer:
    """ this class keep the track of pointer of players w.r.t to their score """

    def __init__(self, screen):
        self.SnakeLadderGame = None
        self.screen = screen
        self.Draw = Draw(self.screen)

    # when both pointer collide in main
    def home_collide(self):
        self.Draw.display('image/red.png', 25, 25, 66, 580)
        self.Draw.display('image/blue.png', 25, 25, 91, 580)

    # when both pointer collide outside the main
    def collide(self, p1):
        x, y = coord[p1]
        self.Draw.display('image/blue.png', 22, 22, x + 53, y + 10)
        self.Draw.display('image/red.png', 22, 22, x + 29, y + 10)

    # function to display the pointer regarding their score
    def pointer(self, score_p1, score_p2):

        print("\nPlayer1 Score:", score_p1)
        print("Player2 Score:", score_p2)

        # player1 just open but player2 not open
        if score_p1 == 1 and score_p2 == 0:
            self.Draw.display('image/red.png', 30, 30, 68, 580)
            self.Draw.display('image/blue.png', 22, 22, 92, 600)

        # player2 just open but player1 not open
        elif score_p1 == 0 and score_p2 == 1:
            self.Draw.display('image/red.png', 22, 22, 68, 600)
            self.Draw.display('image/blue.png', 30, 30, 85, 580)

        # player1 open but player2 not open
        elif score_p1 > 1 and score_p2 == 0:
            x1, y1 = coord[score_p1]
            self.Draw.display('image/red.png', 38, 38, x1 + 33, y1)
            self.Draw.display('image/blue.png', 22, 22, 92, 600)

        # both open just after another
        elif score_p1 == 1 and score_p2 == 1:
            self.home_collide()

        # player1 opened after player2 open
        elif score_p1 > 1 and score_p2 != 0:
            x1, y1 = coord[score_p1]
            x2, y2 = coord[score_p2]

            if score_p2 == 1:
                self.Draw.display('image/red.png', 38, 38, x1 + 33, y1)
                self.Draw.display('image/blue.png', 30, 30, 90, y2)
            elif score_p1 == score_p2:
                self.collide(score_p1)
            else:
                self.Draw.display('image/red.png', 38, 38, x1 + 33, y1)
                self.Draw.display('image/blue.png', 38, 38, x2 + 33, y2)

        # player 2 open but player1 not open
        elif score_p1 == 0 and score_p2 > 1:
            x1, y1 = coord[score_p2]
            self.Draw.display('image/blue.png', 38, 38, x1 + 33, y1)
            self.Draw.display('image/red.png', 22, 22, 68, 600)

        #  player2opened after player1 open
        elif score_p2 > 1 and score_p1 != 0:
            x1, y1 = coord[score_p2]
            x2, y2 = coord[score_p1]

            if score_p1 == 1:
                self.Draw.display('image/blue.png', 38, 38, x1 + 33, y1)
                self.Draw.display('image/red.png', 30, 30, 72, y2)
            elif score_p1 == score_p2:
                self.collide(score_p2)
            else:
                self.Draw.display('image/red.png', 38, 38, x1 + 33, y1)
                self.Draw.display('image/blue.png', 38, 38, x2 + 33, y2)

        pygame.display.flip()
