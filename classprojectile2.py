import pygame

class Projectile2(pygame.sprite.Sprite) :

    def __init__(self, game) :
        super().__init__()

        self.vitesse = 6
        self.game = game
        self.degat = 10
        self.image = pygame.image.load("projectile.png")
        self.image = pygame.transform.scale(self.image, (250,133))
        self.rect = self.image.get_rect()
        self.rect.x = self.game.player.rect.x - 90
        self.rect.y = self.game.player.rect.y + 10


    def move(self) :
        self.rect.x = self.rect.x - self.vitesse

        for monstre in self.game.collision(self, self.game.all_monstre) :
            self.game.all_projectile2.remove(self)
            monstre.damage(self.game.player.attaque)








