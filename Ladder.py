
""" position of ladder in the available theme[1-6] """


class Ladder:

    ladder1 = {2: 18, 9: 28, 25: 47, 30: 50, 39: 41, 45: 57, 51: 73, 65: 85, 79: 98, 89: 91}
    ladder2 = {4: 26, 8: 51, 28: 46, 39: 60, 44: 80, 52: 68, 64: 85, 69: 93, 71: 92, 84: 98}
    ladder3 = {4: 24, 6: 46, 8: 68, 9: 92, 23: 98, 45: 96, 67: 94}
    ladder4 = {6: 16, 10: 61, 18: 43, 21: 39, 30: 51, 48: 67, 57: 65, 69: 87, 76: 95, 90: 92}
    ladder5 = {14: 28, 16: 26, 18: 24, 40: 81, 43: 57, 45: 55, 47: 53, 74: 88, 76: 86, 78: 84}
    ladder6 = {2: 23, 8: 14, 26: 35, 31: 86, 38: 44, 41: 60, 56: 77, 69: 90, 79: 81, 88: 92}

    @staticmethod
    def ladder(theme):

        if theme == 1:
            return Ladder.ladder1
        elif theme == 2:
            return Ladder.ladder2
        elif theme == 3:
            return Ladder.ladder3
        elif theme == 4:
            return Ladder.ladder4
        elif theme == 5:
            return Ladder.ladder5
        elif theme == 6:
            return Ladder.ladder6
