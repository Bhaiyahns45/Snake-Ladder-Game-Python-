import pygame


class Draw:
    """ this class draw and display all the image which is required in the Snake Ladder Game """

    def __init__(self, screen):
        self.screen = screen

    # to display/draw the image on screen
    def display(self, image, width, height, x, y):
        blue = pygame.image.load(image)
        self.screen.blit(pygame.transform.scale(blue, (width, height)), (x, y))

    # for displaying the different dice regarding dice score of players
    def dice(self, p1, x, y):
        img = {1: 'image/dice1.jpeg', 2: 'image/dice2.jpeg', 3: 'image/dice3.jpeg', 4: 'image/dice4.jpeg',
               5: 'image/dice5.jpeg', 6: 'image/dice6.jpeg'}
        self.display(img[p1], 50, 50, x, y)
        pygame.display.flip()
