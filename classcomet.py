import pygame
import random

class Comet(pygame.sprite.Sprite) :

    def __init__(self, comet_event) :
        super().__init__()

        self.image = pygame.image.load("comet.png")
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (120, 90))
        self.comet_event = comet_event
        self.rect.x = self.comet_event.game.player.rect.x
        self.vitesse = random.randint(3, 6)

    def fall(self) :
        self.rect.y += self.vitesse

        if self.rect.y >= 600 :
            self.comet_event.all_comet.remove(self)

        if self.comet_event.game.collision(self, self.comet_event.game.all_player) :

            self.comet_event.all_comet.remove(self)
            self.comet_event.game.player.damage(20)


