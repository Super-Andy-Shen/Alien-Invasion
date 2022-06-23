import pygame

class Ship:
    def __init__(self, ai_game):

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/spaceship.png')
        self.image= pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 5
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.x -= 5
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.y -= 5
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 5

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
    def blitme(self):
        self.screen.blit(self.image,self.rect)
