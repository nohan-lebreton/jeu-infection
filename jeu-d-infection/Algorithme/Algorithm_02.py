"""
Cette algorithme est une méthode d'évaluation permettant de choisir le maximum en utilisant l'opposé du résultat à chaque niveau.
"""

#Importation de la classe State du fichier State.py
from State.State import State
#Importation de la librairie math qui nous permet d'avoir le +infini et le - infini
import math
#Importation de la librairie copy qui nous permet de copier la grille dans une autre grille de façon complète
import copy

class Algorithm_02:
    def __init__(self, playerCourant, profondeurBleu, profondeurRouge, alphabeta):
        self.playerCourant = playerCourant
        #Profondeur d'exploration des noeuds pour le joueur Bleu
        self.profondeurBleu = profondeurBleu
        #Profondeur d'exploration des noeuds pour le joueur Rouge
        self.profondeurRouge = profondeurRouge
        #On récupère la volonté de l'utilisateur d'activer l'élagage avec Alpha Beta
        self.alphabeta = alphabeta
        #Variable qui nous permet de compter le nombre de noeuds explorés dans une partie
        self.compteurNoeudExplores = 0

    """
        si = etat de départ
        d = profondeur maximal
    """
    #Fonction Negamax uniquement
    def negamax(self, si, d):
        self.compteurNoeudExplores += 1
        #Si la profondeur est nulle ou que le noeud exploré terminé alors on renvoi une évaluation de ce noeud
        if d == 0 or si.isOver() == True :
            return si.getScore(self.playerCourant)
        #Sinon
        else:
            #Permet de selectionner une évaluation la plus haute possible
            m = -math.inf
            # Permet de parcourir l'ensemble des états suivants du jeu
            for sj in self.test(si):
                m = max(m, - self.negamax(sj, d-1))
            return m
    #Fonction Negamax avec Alpha Beta
    def negamaxAlphaBeta(self, si,alpha,beta, d):
        self.compteurNoeudExplores += 1
        #Si la profondeur est nulle ou que le noeud exploré terminé alors on renvoi une évaluation de ce noeud
        if d == 0 or si.isOver() == True :
            return si.getScore(self.playerCourant)
        #Sinon
        else:
            for sj in self.test(si):
                alpha = max(alpha, -self.negamaxAlphaBeta(sj,-beta, -alpha, d-1))
                if alpha >= beta:
                    return alpha
            return alpha

    # Retourne une liste contenant tous les plateaux par rapport au plateau de départ et des actions possibles
    def test(self,si):
        liste = []
        for sj in si.getMoves(self.playerCourant):
            liste.append(si.play(sj,False))
        return liste

    # Retourne le meilleur coup à jouer
    def getBestMoveNegamax(self, state, deepness):
        bestAction = None
        bestValue = -math.inf
        #Declaration et d'initialisation d'alpha et de beta
        alpha = -math.inf
        beta  = +math.inf
        for action in state.getMoves(self.playerCourant):
            nextState = state.play(action,False)
            #Si l'utilisateur veut élager avec Alpha Beta
            if(self.alphabeta == True):
                value = self.negamaxAlphaBeta(nextState,alpha,beta,deepness)
            else:
                value = self.negamax(nextState,deepness)
            if value > bestValue :
                bestValue = value
                bestAction = action
        return bestAction




    def launchNegamax(self):

        # plateau où on va jouer les meilleurs actions
        game = State(None, [], self.playerCourant, 2, 2, False, False)
        # plateau où minimax va travailler 
        game2 = State(None, [], self.playerCourant, 2, 2, False, False)

        # Juste de l'affichage
        print("Grille 0")
        game.affiche_grille()
        print("Joueur 1 : " , game.getNbPawn_r())
        print("Joueur 2 : ", game.getNbPawn_b())
        print()
        n = 1
        #Affectation de la profondeur du joueur qui commence
        profondeur = self.profondeurBleu
        #Boucle while qui se termine uniquement si la partie est terminée
        while game.isOver() != True :
            # Le plateau en cours devient un nouveau plateau avec le meilleurs coup joué  
            game = game.play(self.getBestMoveNegamax(game2, profondeur),True)
            
            # Juste de l'affichage
            print("Grille",n)
            game.affiche_grille()
            print("Joueur 1 : " , game.getNbPawn_r())
            print("Joueur 2 : ", game.getNbPawn_b())
            print()
            print(game.getHasPassed())
            print(game.getOldHasPassed())
            
            game2 = copy.deepcopy(game)
            #Changement de joueur et de profondeur si elle n'est pas identique au départ du programme
            if self.playerCourant == 1 :
                self.playerCourant = 2
                profondeur = self.profondeurBleu

            else :
                self.playerCourant = 1
                profondeur = self.profondeurRouge
                
            game.setCurrentPlayer(self.playerCourant)
            n +=1

        print("Nombre de nœuds explorés au cours de la partie : ", self.compteurNoeudExplores)



