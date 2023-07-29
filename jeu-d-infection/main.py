from Algorithme.Algorithm_00 import Algorithm_00
from Algorithme.Algorithm_01 import Algorithm_01
from Algorithme.Algorithm_02 import Algorithm_02


# ▂▃▅▇█▓▒░ COMMANDES MAIN ░▒▓█▇▅▃▂



print("Bienvenu !!!")
algo = int(input("Veuillez entrer Random(1), Minimax(2) et Negamax(3) : "))
if algo == 1:
    algo0 = Algorithm_00().launchRandom()
elif algo == 2:
    profondeurBleu = int(input("Veuillez entrer la profondeur de bleu : "))
    profondeurRouge = int(input("Veuillez entrer la profondeur de rouge : "))
    alpha = input("Elagage alphabeta : True ou False ")
    print("alpha : " ,alpha)
    algo1 = Algorithm_01(2,profondeurBleu,profondeurRouge,alpha).launchMinimax()

elif algo == 3:

    profondeurBleu = int(input("Veuillez entrer la profondeur de bleu : "))
    profondeurRouge = int(input("Veuillez entrer la profondeur de rouge : "))
    alpha = input("Elagage alphabeta : True ou False ")
    if alpha == "True":
        alpha = True
    else :
        alpha = False
    #print("alpha : " ,alpha)

    algo2 = Algorithm_02(2,profondeurBleu,profondeurRouge,alpha).launchNegamax()