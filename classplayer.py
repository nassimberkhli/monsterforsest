import pygame
from classmonstre import Monstre

#-------------------------------------------------------------------------------
import sqlite3

conn = sqlite3.connect("")
cursor = conn.cursor()



#                    CREATION D'UNE TABLE

cursor.execute("""
CREATE TABLE IF NOT EXISTS Player(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     barre_vie INTEGER,
     attaque INTEGER,
     vitesse INTERGER
)
""")
conn.commit()



#                    INSERTION DES DONNEES

cursor.execute("""
INSERT INTO Player (barre_vie, attaque, vitesse)
    VALUES
    (? , ? , ?)
    """,
    (100, 25, 0.5))



#                         EXECUTION

cursor.execute("""SELECT barre_vie, attaque, vitesse FROM Player """)

base_donnee_player = cursor.fetchone()


#-------------------------------------------------------------------------------

class Player(pygame.sprite.Sprite) :

    def __init__(self, game) :
        super().__init__()
        self.game = game


        # paramètre du personnage
        self.barre_vie = base_donnee_player[0]
        self.barre_vie_max = base_donnee_player[0]
        self.attaque = base_donnee_player[1]
        self.vitesse = base_donnee_player[2]
        self.vitesse_air = 1
        # face graphique du personnage
        self.image = pygame.image.load("personnage.png")
        # taille du personnage
        self.image = pygame.transform.scale(self.image, (60, 60))
        # positionnement du personnage
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 625

        # paramètre du saut
        self.saut = 1
        self.gravite = 0

#-------------------------------------------------------------------------------

# méthode qui permet le déplacement du personnage
    def move_right(self) :
        if not(self.game.collision(self, self.game.all_monstre)) :
            self.rect.x += 1.5


    def move_left(self) :
        if not (self.game.collision(self, self.game.all_monstre)):
            self.rect.x -= self.vitesse

    # barre de vie
    def barre(self, surface) :
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x - 20, self.rect.y - 20, self.barre_vie_max, 5])
        pygame.draw.rect(surface, (201, 73, 207 ), [self.rect.x - 20, self.rect.y - 20, self.barre_vie, 5])

    def damage(self, degat) :
        if self.barre_vie - degat > degat :
            self.barre_vie -= degat
        else :
            self.game.game_over()


#-------------------------------------------------------------------------------

# méthode du saut du personnage
    def jump(self) :


        if self.condition :

            self.vitesse = 0.5

            if self.rect.y > 520 and self.saut == 1 :



                self.vitesse -= 0.031914894
                self.gravite += 0.3
                self.rect.y -= 0.01 + self.gravite


            else :

                self.saut = 0

                if self.rect.y < 625 :

                    self.vitesse += 0.031914894 #0.015957447
                    self.gravite -= 0.3
                    self.rect.y += 0.01 - self.gravite

                else :
                    self.rect.y = 625
                    self.vitesse = base_donnee_player[2]
                    self.gravite = 0
                    self.saut = 1
                    self.condition = False

















