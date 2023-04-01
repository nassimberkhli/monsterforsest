import pygame
import random

#-------------------------------------------------------------------------------
import sqlite3

conn = sqlite3.connect("")
cursor = conn.cursor()



#                    CREATION D'UNE TABLE

cursor.execute("""
CREATE TABLE IF NOT EXISTS Monstre(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     barre_vie_slime INTEGER,
     attaque REAL,
     vitesse INTERGER
)
""")
conn.commit()



#                    INSERTION DES DONNEES

cursor.execute("""
INSERT INTO Monstre (barre_vie_slime, attaque, vitesse)
    VALUES
    (? , ? , ?)
    """,
    (100, 0.3, 1))



#                         EXECUTION

cursor.execute("""SELECT barre_vie_slime, attaque, vitesse FROM Monstre """)

base_donnee_monstre = cursor.fetchone()


#-------------------------------------------------------------------------------

class Monstre(pygame.sprite.Sprite) :

    def __init__(self, game) :
        super().__init__()
        self.game = game

        self.barre_vie_slime = base_donnee_monstre[0]
        self.barre_vie_slime_max = base_donnee_monstre[0]
        self.attaque = base_donnee_monstre[1]
        self.vitesse = random.uniform(base_donnee_monstre[2], 2)
        self.image = pygame.image.load("slime2.png")
        self.image = pygame.transform.scale(self.image, (240, 120))
        self.rect = self.image.get_rect()
        self.rect.x = 800 + random.uniform(100, 500)
        self.rect.y = 609

    def damage(self, degat) :
        self.barre_vie_slime -= degat

        if self.barre_vie_slime <= 0  :
            self.rect.x = 1000 + random.randint(0, 500)
            self.vitesse = random.uniform(0.5, 1.5)
            self.barre_vie_slime = self.barre_vie_slime_max
            self.game.score += 1
            self.game.player.barre_vie += 5

            if self.game.kill < 160 :
                self.game.kill += 20

            if self.game.kill >= 80 :
                self.game.x = 230
                self.game.y = 131
                self.game.z = 5




    # barre de vie
    def barre_slime(self, surface) :
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 140, self.rect.y - 2, self.barre_vie_slime_max, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 140, self.rect.y - 2, self.barre_vie_slime, 5])


    def move_monstre(self) :
        # le deplacemnt se fait que si il n'y a pas de collision (avec le joueur)
        if not(self.game.collision(self, self.game.all_player)) :
                self.rect.x -= self.vitesse
        else :
            self.game.player.damage(self.attaque)
            self.rect.x -= 0.1







