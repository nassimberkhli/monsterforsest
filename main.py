# initialisation du module pygame
import pygame
from classgame import Game
pygame.init()

#-------------------------------------------------------------------------------

# initialisation de la fenêtre
screen = pygame.display.set_mode((1080, 720))

# création du fond d'écran du jeu
fond_ecran = pygame.image.load("fond.png")
fond_ecran = pygame.transform.scale(fond_ecran, (1080, 720))

# bannière
banniere = pygame.image.load("banniere.png")
banniere = pygame.transform.scale(banniere, (1080, 720))

play_button = pygame.image.load("bouton.png")
play_button = pygame.transform.scale(play_button, (250, 225))
play_button_rect = play_button.get_rect()
play_button_rect.x = 700
play_button_rect.y = 400


# charger le jeu
game = Game()

#-------------------------------------------------------------------------------

bool_jump = 0
continu = True
while continu :

#-------------------------------------------------------------------------------

    # applique le fond d'écran sur le jeu
    screen.blit(fond_ecran, (0, 8))

    # vérifie si le jeu a commencé
    if game.is_playing :
        game.update(screen)
    else :
        screen.blit(banniere, (55, 90))
        screen.blit(play_button, play_button_rect)


    # met à jour l'écran
    pygame.display.flip()

#-------------------------------------------------------------------------------

    # lorsque l'utilisateur quitte la fenêtre
    for event in pygame.event.get() :

        if event.type == pygame.QUIT :
            continu = False
            pygame.quit()

#-------------------------------------------------------------------------------

        # lorsque le joueur touche une touche du clavier
        elif event.type == pygame.KEYDOWN :
            game.pressed[event.key] = True

            if event.key == pygame.K_RIGHT :
                game.bool_right_or_left = 2
                game.player.image = pygame.image.load("personnage.png")
                game.player.image = pygame.transform.scale(game.player.image, (60, 60))

            if event.key == pygame.K_LEFT :
                game.bool_right_or_left = 3
                game.player.image = pygame.image.load("personnage2.png")
                game.player.image = pygame.transform.scale(game.player.image, (60, 60))


            # lorsque le joueur touche sur w
            if event.key == pygame.K_w :
                if game.bool_right_or_left == 2 :
                    game.lancer()
                    portee = 0


                elif game.bool_right_or_left == 3 :
                    game.lancer2()


            # touche x, attaque special
            if event.key == pygame.K_x :

                if game.kill >= 80 and game.bool_right_or_left == 3 :
                    # gestion de la jauge special
                    game.kill -= 80
                    if game.kill < 80 :
                        game.x = 49
                        game.y = 5
                        game.z = 230

                    game.lancer_special()

                if game.kill >= 80 and game.bool_right_or_left == 2 :
                    # gestion de la jauge special
                    game.kill -= 80
                    if game.kill < 80 :
                        game.x = 49
                        game.y = 5
                        game.z = 230

                    game.lancer_special2()


            # lorsque la touche de haut est activé
            if event.key == pygame.K_UP and game.player.rect.y == 625 :
                    game.bool_jump = 1
                    game.player.condition = True

            if event.key == pygame.K_SPACE :
                game.start()

        elif event.type == pygame.KEYUP :
            game.pressed[event.key] = False

        # si la souri est en collision
        elif event.type == pygame.MOUSEBUTTONDOWN :
            if play_button_rect.collidepoint(event.pos) :
                game.start()


    if game.kill >= 80 :
        game.x = 229
        game.y = 7
        game.z = 7

#-------------------------------------------------------------------------------

