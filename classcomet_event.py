import pygame
from classcomet import Comet

class CometFallEvent :

    #compteur
    def __init__(self, game) :
        self.percent = 0
        self.percent_speed = 12
        self.all_comet = pygame.sprite.Group()
        self.game = game
        self.bool_comet = False

    def add_percent(self) :
        if self.game.score >= 6 :
            self.percent += self.percent_speed / 100


    def update_bar(self, surface) :

        self.add_percent()

        self.attempt_fall()

        pygame.draw.rect(surface, (0, 0, 0), [0, surface.get_height() - 20, surface.get_width(), 10])
        pygame.draw.rect(surface, (230, 131, 5), [0, surface.get_height() - 20, (surface.get_width() / 100) * self.percent, 10])

    # apparition des comets
    def meteor_fall(self) :

        for i in range (1) :
            self.all_comet.add(Comet(self))
        self.percent = 0

    # barre chargée à 100%
    def is_full_loaded(self) :

        return self.percent >= 100


    def attempt_fall(self) :

        if self.is_full_loaded() :
            self.meteor_fall()
