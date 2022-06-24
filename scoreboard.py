import pygame.font
from pygame.sprite import Group
from ship import Ship
class Scoreboard:
    def __init__(self,ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (200,0,0)
        self.font = pygame.font.SysFont(None,80)

        self.prep_score()
        self.prep_ships()
    
    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str,True,self.text_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.score_rect.right + 1200
        self.score_rect.top = 20
    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.ships.draw(self.screen)

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            #self.ships.add(ship)
