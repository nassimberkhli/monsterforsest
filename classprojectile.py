import pygame

class Projectile(pygame.sprite.Sprite) :

    def __init__(self, game) :
        super().__init__()

        self.game = game
        self.degat = 7
        self.vitesse = 6
        self.image = pygame.image.load("projectile.png")
        self.image = pygame.transform.scale(self.image, (250,133))
        self.rect = self.image.get_rect()
        self.rect.x = self.game.player.rect.x - 35
        self.rect.y = self.game.player.rect.y + 10


    def move(self) :
        self.rect.x = self.rect.x + self.vitesse


        for monstre in self.game.collision(self, self.game.all_monstre) :
            self.game.all_projectile.remove(self)
            monstre.damage(self.degat)



