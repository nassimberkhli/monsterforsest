import pygame
from classplayer import Player
from classprojectile import Projectile
from classprojectile2 import Projectile2
from classmonstre import Monstre
from classcomet_event import CometFallEvent
from classsuper_projectile import Super_projectile
from classsuper_projectile2 import Super_projectile2

class Game :

    def __init__(self) :
        # si notre jeu a commencé
        self.is_playing = False
        self.first_game = True

        # générer le personnage
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)

        # génère l'évènement de comet
        self.comet_event = CometFallEvent(self)

        # groupe de monstre
        self.all_monstre = pygame.sprite.Group()
        self.all_monstre2 = pygame.sprite.Group()
        self.pressed = {}

        # méthode qui permet de ranger le projecile dans le groupe all_projectile
        self.all_projectile = pygame.sprite.Group()
        self.all_projectile2 = pygame.sprite.Group()

        self.all_super_projectile = pygame.sprite.Group()
        self.all_super_projectile2 = pygame.sprite.Group()


        self.score = 0
        self.kill = 0
        self.bool_jump = 0
        self.bool_right_or_left = 2

        # couleur de la jauge special (rouge)
        self.x = 49
        self.y = 5
        self.z = 230

        # couleur de la jauge special (vert)
        self.x1 = 123
        self.y1 = 40
        self.z1 = 133



#-------------------------------------------------------------------------------

    def start(self) :
        self.is_playing = True

        if self.first_game == True :
            self.spawn_monstre()
            self.spawn_monstre()
            self.first_game = False


#-------------------------------------------------------------------------------

    def game_over(self) :
        self.all_monstre = pygame.sprite.Group()
        self.all_monstre.remove(self)
        self.player.barre_vie = self.player.barre_vie_max
        self.comet_event.all_comet= pygame.sprite.Group()
        self.comet_event.percent = 0
        self.score = 0
        self.kill = 0
        self.is_playing = False
        self.first_game = True

#-------------------------------------------------------------------------------
    def update(self, screen) :

        # applique le score
        font = pygame.font.SysFont("monospace", 25)
        score_text = font.render(f"Score : {self.score}", 1, (255, 255, 255))
        screen.blit(score_text, (20, 20))

        # applique l'image du personnage
        screen.blit(self.player.image, self.player.rect)
        self.player.barre(screen)

        # actualise la barre de comet et d'arbre
        self.comet_event.update_bar(screen)



#-------------------------------------------------------------------------------

        # mouvement des projectiles à droite
        for Projectile in self.all_projectile :
            Projectile.move()
            if Projectile.rect.x > 990 :
                self.all_projectile.remove(Projectile)

        # mouvement des projectiles à gauche
        for Projectile2 in self.all_projectile2 :
            Projectile2.move()
            if  Projectile2.rect.x < -85 :
                self.all_projectile2.remove(Projectile2)

        for Super_projectile in self.all_super_projectile :
            Super_projectile.move()
            if Super_projectile.rect.x < -85 :
                self.all_super_projectile.remove(Super_projectile)

        for Super_projectile2 in self.all_super_projectile2 :
            Super_projectile2.move()
            if Super_projectile2.rect.x > 990 :
                self.all_super_projectile2.remove(Super_projectile2)

        # récupérer les monstres de notre jeu
        for monstre in self.all_monstre :
            monstre.move_monstre()
            monstre.barre_slime(screen)
            if monstre.rect.x < -300 :
                self.player.damage(10)
                self.all_monstre.remove(monstre)
                self.spawn_monstre()

        # récupérer les comets de notre jeu
        for comet in self.comet_event.all_comet :
            comet.fall()


#-------------------------------------------------------------------------------

        # applique l'ensemble des images de mon groupe de projectiles
        self.all_projectile.draw(screen)
        self.all_projectile2.draw(screen)
        self.all_super_projectile.draw(screen)
        self.all_super_projectile2.draw(screen)

        # applique l'ensemble des images de mon groupe de monstres
        self.all_monstre.draw(screen)

        # applique l'ensemble des images de mon groupe de comet
        self.comet_event.all_comet.draw(screen)

        # applique barre_special
        pygame.draw.rect(screen, (60, 63, 60), [850, 30, 160, 10])
        pygame.draw.rect(screen, (self.x, self.y, self.z), [850, 30, self.kill, 10])


#-------------------------------------------------------------------------------

        # vérifie si le personnage va à droite ou à gauche (au sol)
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x <= 1026 and self.player.rect.y == 625 :
            self.player.move_right()

        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x >= -2 and self.player.rect.y == 625 :
            self.player.move_left()

        # dans les airs
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x <= 1026 and self.player.rect.y < 625 :
            self.player.move_right()
            if self.bool_jump == 1 :
                self.player.jump()

        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x >= -2 and self.player.rect.y < 625 :
            self.player.move_left()
            if self.bool_jump == 1 :
                self.player.jump()

        # lorsque la touche de haut est activé
        elif self.bool_jump == 1 :
            self.player.jump()


#-------------------------------------------------------------------------------

    def lancer(self) :
        projectile = Projectile(self)
        self.all_projectile.add(projectile)


    def lancer2(self) :
        projectile2 = Projectile2(self)
        self.all_projectile2.add(projectile2)

    def lancer_special(self) :
        super_projectile = Super_projectile(self)
        self.all_super_projectile.add(super_projectile)

    def lancer_special2(self) :
        super_projectile2 = Super_projectile2(self)
        self.all_super_projectile2.add(super_projectile2)

    def spawn_monstre(self) :
        monstre = Monstre(self)
        self.all_monstre.add(monstre)


    def collision(self, sprite, group) :
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

