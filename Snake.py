""" position of snake in the available theme[1-6] """


class Snake:

    snake1 = {27: 5, 38: 17, 52: 33, 62: 60, 66: 46, 90: 70, 93: 67, 95: 75, 97: 58, 99: 81}
    snake2 = {11: 9, 36: 14, 43: 22, 57: 19, 66: 47, 81: 63, 90: 49, 94: 48, 96: 65, 99: 78}
    snake3 = {18: 2, 36: 5, 54: 7, 93: 73, 95: 55, 97: 37, 99: 2}
    snake4 = {22: 2, 36: 7, 42: 40, 68: 49, 77: 28, 81: 62, 86: 74, 94: 71, 96: 84, 98: 63}
    snake5 = {13: 9, 15: 7, 17: 5, 42: 38, 44: 36, 46: 34, 73: 69, 75: 67, 77: 65, 91: 50, 95: 87, 97: 85, 99: 83}
    snake6 = {25: 4, 29: 10, 33: 27, 42: 22, 63: 59, 64: 37, 70: 49, 94: 73, 96: 47, 99: 78}

    @staticmethod
    def snake(theme):
        if theme == 1:
            return Snake.snake1
        elif theme == 2:
            return Snake.snake2
        elif theme == 3:
            return Snake.snake3
        elif theme == 4:
            return Snake.snake4
        elif theme == 5:
            return Snake.snake5
        elif theme == 6:
            return Snake.snake6
