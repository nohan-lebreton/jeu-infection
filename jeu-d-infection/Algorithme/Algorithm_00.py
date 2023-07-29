"""
Cette algorithme permet de faire jouer aléatoire les deux joueurs.
"""
#Importation de la classe State du fichier State.py
from State.State import State
#Importation de la librairie random qui nous permet d'effectuer le random.choice() parmis tous les mouvements possibles
import random

class Algorithm_00 :
    def __init__(self):
        self.board = None
        self.oldBoard = []
        #Le joueur qui commence est le joueur Bleu (2), puis Rouge(1)
        self.player = 2
        #Déclarations qu'il y a 2 pions de chaque couleurs sur le plateau
        self.nbPawn_r = 2
        self.nbPawn_b = 2
        #Mise par défaut des variables hasPassed et oldHasPassed à False
        self.hasPassed = False
        self.oldHasPassed = False

    def launchRandom(self):
        # Création du plateau de jeu
        game = State(self.board, self.oldBoard, self.player, self.nbPawn_r, self.nbPawn_b, self.hasPassed, self.oldHasPassed)
        
        # Juste de l'affichage
        print("Grille 0")
        game.affiche_grille()
        i = 1
        #Boucle infinie tant que la partie n'est pas arrétée
        while game.isOver() != True:
            #On récupère le joueur courrant du plateau en cours
            player = game.getCurrentPlayer()
            # Création de la liste des coups possibles selon le joueur.
            moveList = game.getMoves(player)
            """
                Si la liste n'est pas vide alors move est égale à une action possible
                Si la liste est vide alors on affecte au move None pour dire au programme qu'il n'y a pas d'action possible
                Et que le joueur va devoir passer son tour.
            """
            if moveList != [] :
                move = random.choice(moveList)

            else :
                move = None

            # Le plateau en cours devient un nouveau plateau avec le coup joué    
            game = game.play(move, True)
    
            # Juste de l'affichage
            print("Grille",i)
            game.affiche_grille()
            i = i + 1

            
