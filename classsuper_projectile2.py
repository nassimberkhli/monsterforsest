import pygame

class Super_projectile2(pygame.sprite.Sprite) :

    def __init__(self, game) :
        super().__init__()

        self.game = game
        self.degat = 1000
        self.vitesse = 20
        self.image = pygame.image.load("super_projectile.png")
        self.image = pygame.transform.scale(self.image, (150,3))
        self.rect = self.image.get_rect()
        self.rect.x = self.game.player.rect.x + 10
        self.rect.y = self.game.player.rect.y + 25


    def move(self) :
        self.rect.x = self.rect.x + self.vitesse


        for monstre in self.game.collision(self, self.game.all_monstre) :
            self.game.all_super_projectile2.remove(self)
            monstre.damage(self.degat)