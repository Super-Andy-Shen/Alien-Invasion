import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/alien.bmp')
        #self.image= pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.screen_rect = ai_game.screen.get_rect()
    def update(self):
       self.rect.x += (self.settings.alien_speed * self.settings.fleet_direction)
       
    def check_edges(self):
        if (self.rect.right >= self.screen_rect.right) or (self.rect.left <= self.screen_rect.left):
            return True
    

       