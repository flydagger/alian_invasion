import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        # initialize alien and set its start position
        super(Alien, self).__init__()  # super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # each alien appears at the top left corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # save the accurate position of alien
        self.x = float(self.rect.x)

    def blitme(self):
        """draw the alien at the specific position"""
        self.screen.blit(self.image, self.rect)

