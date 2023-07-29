from Move.Move import Move
#Classe State qui regroupe la partie non stratégique/dynamique du jeu
class State :
    def __init__(self, board, allBoard, player, nbPawn_r, nbPawn_b, hasPassed, oldHasPassed):
        #Initialisation de la taille de la grille
        self.nbLigne = 7
        self.nbColonne = 7
        #Mise en forme de la grille suivant les dimensions
        self.board = self.__creation_grille(board)
        #Liste qui va nous permettre de stocker toutes les grilles jouées afin de repérer les répétitions
        self.allBoard = allBoard

        self.player = player

        self.nbPawn_r = nbPawn_r
        self.nbPawn_b = nbPawn_b
        #Variable qui nous informe si le joueur passe et si le joueur précedent à aussi passé son tour
        self.hasPassed = hasPassed
        self.oldHasPassed = oldHasPassed
    """
    Méthodes utilitaires
    """
    def getNbPawn_r(self):
        return self.nbPawn_r

    def getNbPawn_b(self):
        return self.nbPawn_b

    def getHasPassed(self):
        return self.hasPassed

    def setHasPassed(self,hasPassed):
        self.hasPassed = hasPassed

    def getOldHasPassed(self):
        return self.oldHasPassed

    def setOldHasPassed(self, oldHasPassed):
        self.oldHasPassed = oldHasPassed

    def getCurrentPlayer(self):
        return self.player
    
    def setCurrentPlayer(self, player):
        self.player = player

    def __creation_grille(self, board):
        grille = []
        if board == None:
            for ligne in range(self.nbLigne):
                liste = []
                for colonne in range(self.nbColonne):
                    liste.append("#")
                grille.append(liste)
            #Mise en place des pions sur les extremités de la grille
            grille[0][0], grille[-1][-1] = 1, 1 # pions rouge
            grille[0][-1], grille[-1][0] = 2, 2 # pions bleu

        else :
            grille = board
        return grille


    """
    La méthode getScore prend un joueur en entrée et retourne l’évaluation de l’état par ce joueur
    """
    def getScore(self, player) :
        if player == 1 :
            return self.nbPawn_r / (self.nbPawn_r + self.nbPawn_b)
        elif player == 2 :
            return self.nbPawn_b / (self.nbPawn_b + self.nbPawn_r)

    """
    La méthode affiche_grille qui permet d'afficher la grille pour une meilleure lisibilité de la partie
    """
    def affiche_grille(self):
        for ligne in range(len(self.board)):
            for colonne in range(len(self.board[ligne])):
                print(self.board[ligne][colonne],end = " ")
            print()
        print()

    
    """
    La méthode isOver retourne un booléen indiquant si la partie est finie ou non
    """
    def isOver(self) :
        
        # 1er cas de nul : Le joueur precedent passe et le joueur actuel passe aussi
        if (self.hasPassed == True and self.oldHasPassed == True) :
            return True
        
        
        # 2eme cas de nul : Il ne reste qu'une couleur sur la grille (rouge ou bleu)
        
        elif (self.nbPawn_r == 0 or self.nbPawn_b == 0) :
            return True

        
        # 3eme cas de nul : Repetition d'une meme grille
        for board in self.allBoard :
            if self.board == board :
                return True
        
        return False

    """
    Cloner un pion consiste à placer un nouveau pion sur 
    une case libre à une distance de un (quelle que soit 
    la direction) du pion choisi.
    """

    # à retravailler rendre plus compact
    def __cloner (self, directionClone,pos_x, pos_y):

        # Case haut
        if directionClone == 0 and self.board[pos_x-1][pos_y] == "#" and pos_x > 0:
            position_x, position_y = pos_x-1, pos_y
            typeClone = "Clone_Haut"
            return position_x, position_y, typeClone

        # Case haut gauche
        elif directionClone == 1 and self.board[pos_x-1][pos_y-1] == "#" and pos_x > 0 and pos_y > 0:
            position_x, position_y = pos_x-1, pos_y-1
            typeClone = "Clone_Haut-Gauche"
            return position_x, position_y, typeClone

        # Case haut droite
        elif directionClone == 2 and pos_x > 0 and pos_y < len(self.board[pos_x])-1:
            if self.board[pos_x-1][pos_y+1] == "#" :
                position_x, position_y = pos_x-1, pos_y+1
                typeClone = "Clone_Haut-Droite"
                return position_x, position_y, typeClone
            else :
                return None, None, None

        # Case bas
        elif directionClone == 3 and pos_x < len(self.board)-1:
            if self.board[pos_x+1][pos_y] == "#" :
                position_x, position_y = pos_x+1, pos_y
                typeClone = "Clone_Bas"
                return position_x, position_y, typeClone
            else :
                return None, None, None

        # Case bas gauche
        elif directionClone == 4 and pos_x < len(self.board)-1 and pos_y > 0:
            if self.board[pos_x+1][pos_y-1] == "#":
                position_x, position_y = pos_x+1, pos_y-1
                typeClone = "Clone_Bas-Gauche"
                return position_x, position_y, typeClone
            else :
                return None, None, None

        # Case bas droite
        elif directionClone == 5 and pos_x < len(self.board)-1 and pos_y < len(self.board[pos_x])-1 :
            if self.board[pos_x+1][pos_y+1] == "#" :
                position_x, position_y = pos_x+1, pos_y+1
                typeClone = "Clone_Bas-Droite"
                return position_x, position_y, typeClone
            else :
                return None, None, None

        # Case gauche
        elif directionClone == 6 and self.board[pos_x][pos_y-1] == "#" and pos_y > 0:
            position_x, position_y = pos_x, pos_y-1
            typeClone = "Clone_Gauche"
            return position_x, position_y, typeClone

        # Case droite
        elif directionClone == 7 and pos_y < len(self.board[pos_x])-1:
            if self.board[pos_x][pos_y+1] == "#" :
                position_x, position_y = pos_x, pos_y+1
                typeClone = "Clone_Droite"
                return position_x, position_y, typeClone
            else :
                return None, None, None

        else :
            return None, None, None

    """
    Sauter consiste à déplacer le pion choisir une case 
    libre à une distance de deux dans une des huit 
    directions possibles, sachant que ce mouvement permet 
    de passer par-dessus un autre pion quel qu’en soit 
    le propriétaire. 
    """

    # à retravailler rendre plus compact
    def __sauter (self, directionSaut,pos_x, pos_y):
        # Case haut
        if directionSaut == 0 and self.board[pos_x-2][pos_y] == "#" and pos_x > 1:
            position_x, position_y = pos_x-2, pos_y
            typeSaut = "Saut_Haut"
            return  position_x, position_y, typeSaut

        # Case haut gauche
        elif directionSaut == 1 and self.board[pos_x-2][pos_y-2] == "#" and pos_x > 1 and pos_y > 1:
            position_x, position_y = pos_x-2, pos_y-2
            typeSaut = "Saut_Haut-Gauche"
            return position_x, position_y, typeSaut

        # Case haut droite
        elif directionSaut == 2 and pos_x > 1 and pos_y < len(self.board[pos_x])-2:
            if self.board[pos_x-2][pos_y+2] == "#" :
                position_x, position_y = pos_x-2, pos_y+2
                typeSaut = "Saut_Haut-Droite"
                return position_x, position_y, typeSaut
            else :
                return None, None, None

        # Case bas
        elif directionSaut == 3 and pos_x < len(self.board)-2:
            if self.board[pos_x+2][pos_y] == "#" :
                position_x, position_y = pos_x+2, pos_y
                typeSaut = "Saut_Bas"
                return position_x, position_y, typeSaut
            else :
                return None, None, None

        # Case bas gauche
        elif directionSaut == 4 and pos_x < len(self.board)-2 and pos_y > 1:
            if self.board[pos_x+2][pos_y-2] == "#" :
                position_x, position_y = pos_x+2, pos_y-2
                typeSaut = "Saut_Bas-Gauche"
                return position_x, position_y, typeSaut
            else :
                return None, None, None

        # Case bas droite
        elif directionSaut == 5 and pos_x < len(self.board)-2 and pos_y < len(self.board[pos_x])-2:
            if self.board[pos_x+2][pos_y+2] == "#":
                position_x, position_y = pos_x+2, pos_y+2
                typeSaut = "Saut_Bas-Droite"
                return position_x, position_y, typeSaut
            else :
                return None, None, None

        # Case gauche
        elif directionSaut == 6 and self.board[pos_x][pos_y-2] == "#" and pos_y > 1:
            position_x, position_y = pos_x, pos_y-2
            typeSaut = "Saut_Gauche"
            return position_x, position_y, typeSaut

        # Case droite
        elif directionSaut == 7 and pos_y < len(self.board[pos_x])-2:
            if self.board[pos_x][pos_y+2] == "#" :
                position_x, position_y = pos_x, pos_y+2
                typeSaut = "Saut_Droite"
                return position_x, position_y, typeSaut
            else :
                return None, None, None
        
        else :
            return None, None, None


    """
    Tous les pions adverses qui sont adjacents au pion 
    déplacé par un saut, ou adjacent au pion nouvellement 
    créé par clonage sont infectés et sont transformés 
    en des pions de la couleur du joueur actif 
    """

    # à retravailler rendre plus compact
    def __infection(self,pos_x, pos_y, player):
        
        x = []
        y = []

        # (0,0)
        if pos_x == 0 and pos_y == 0: 
            x = [0,1]
            y = x

        # (0,-1)
        elif pos_x == 0 and pos_y == len(self.board[pos_x])-1: 
            x = [0,1]
            y = [0,-1]

        # (-1,0)
        elif pos_x == len(self.board)-1 and pos_y == 0: 
            x = [0,-1]
            y = [0,1]


        # (0,1:-2)
        elif pos_x == 0 and pos_y > 0 and pos_y < len(self.board[pos_x])-1: 
            x = [0,1]
            y = [0,1,-1]

        # (1:-2, 0)
        elif pos_x > 0 and pos_x < len(self.board)-1 and pos_y == 0 : 
            x = [0,1,-1]
            y = [0,1]

        
        # (1:-2,1:-2)
        elif pos_x > 0 and pos_x < len(self.board)-1 and pos_y > 0 and pos_y < len(self.board[pos_x])-1 :
            x = [0,1,-1]
            y = x
        
        # (-1,-1)
        elif pos_x == len(self.board)-1 and pos_y == len(self.board[pos_x])-1 :
            x = [0,-1]
            y = x

        # (-1,1:-2)
        elif pos_x == len(self.board)-1 and pos_y > 0 and pos_y < len(self.board[pos_x])-1 :
            x = [0,-1]
            y = [0,1,-1]

         # (1:-2,-1)
        elif pos_x > 0 and pos_x < len(self.board)-1 and pos_y == len(self.board[pos_x])-1 :
            x = [0,1,-1]
            y = [0,-1]
            

        for i in x:
            for j in y:
                if self.board[pos_x+i][pos_y+j] != player and self.board[pos_x+i][pos_y+j] !="#":
                    self.board[pos_x+i][pos_y+j] = player
                    if player == 1 :
                        self.nbPawn_r += 1
                        self.nbPawn_b -= 1
                    elif player == 2 :
                        self.nbPawn_r -= 1
                        self.nbPawn_b += 1

    """
    La méthode getMove prend un joueur en entrée et retour l’ensemble des coups possibles de ce joueur
    """
    def getMoves(self,player):
        listeMove = []
        listeMoveClone = []
        listeMoveSaut = []
        cpt = 0

        for ligne in range(len(self.board)):
            for colonne in range(len(self.board[ligne])):
                if self.board[ligne][colonne] == player :
                    while cpt != 8:

                        # Clonage :
                        pos_x_clone, pos_y_clone, typeClone = self.__cloner(cpt, ligne, colonne)
                        move_clone = Move(ligne, colonne, pos_x_clone, pos_y_clone, typeClone)
                        if pos_x_clone != None and pos_y_clone != None and typeClone != None:
                            listeMoveClone.append(move_clone)

                        # Le saut
                        pos_x_saut, pos_y_saut, typeSaut = self.__sauter(cpt,ligne, colonne)
                        move_saut = Move(ligne, colonne, pos_x_saut, pos_y_saut, typeSaut)
                        if pos_x_saut != None and pos_y_saut != None and typeSaut != None:
                            listeMoveSaut.append(move_saut)

                        cpt += 1

                    listeMove += listeMoveClone + listeMoveSaut
                    listeMoveClone = []
                    listeMoveSaut = []
                    cpt = 0        
        return listeMove


    """
    La méthode play prend un coup en entrée et retourne un nouvel état
    """
    def play(self,move, real):
        oldBoard = []
        for ligne in range(len(self.board)):
            listeOldBoard = []
            for colonne in range(len(self.board[ligne])):
                listeOldBoard.append(self.board[ligne][colonne])
            oldBoard.append(listeOldBoard)

        newBoard = self.board
        newPlayer = 0

        if self.player == 1 :
            newPlayer = 2
        else:
            newPlayer = 1
        
        if move != None :
            # Pour le type clone
            if move.getType() == "Clone_Haut" or move.getType() == "Clone_Haut-Gauche" or move.getType() == "Clone_Haut-Droite" or move.getType() == "Clone_Bas" or move.getType() == "Clone_Bas-Gauche" or move.getType() == "Clone_Bas-Droite" or move.getType() == "Clone_Gauche" or move.getType() == "Clone_Droite":
                newBoard[move.getPosA_x()][move.getPosA_y()] = self.player
                if self.player == 1 :
                    self.nbPawn_r = self.nbPawn_r + 1
                else:
                    self.nbPawn_b = self.nbPawn_b + 1

            # Pour le type saut
            elif move.getType() == "Saut_Haut" or move.getType() == "Saut_Haut-Gauche" or move.getType() == "Saut_Haut-Droite" or move.getType() == "Saut_Bas" or move.getType() == "Saut_Bas-Gauche" or move.getType() == "Saut_Bas-Droite" or move.getType() == "Saut_Gauche" or move.getType() == "Saut_Droite":
                newBoard[move.getPosI_x()][move.getPosI_y()] = "#"
                newBoard[move.getPosA_x()][move.getPosA_y()] = self.player

            #Permet l'infection des pions à côté de la position d'arrivée du pion joué
            self.__infection(move.getPosA_x(), move.getPosA_y(), self.player)
            if real == True:
                #Sauvegarde de la grille afin de repéré des répétitions
                self.allBoard.append(oldBoard)

        else :
            #Si le joueur passe son tour alors oldHasPassed devient l'ancienne valeur d'hasPassed et hasPassed devient True 
            return State(newBoard, self.allBoard, newPlayer, self.nbPawn_r, self.nbPawn_b, True, self.hasPassed)
        #Sinon oldHasPassed devient l'ancienne valeur d'hasPassed et hasPassed devient False
        return State(newBoard, self.allBoard, newPlayer, self.nbPawn_r, self.nbPawn_b, False, self.hasPassed)