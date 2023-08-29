#Tirage au sort d'un prix entre 1 et 10 (compris)
import random
cible = random.randint(1,10)
essai = None

def verif(cible_param, essai_param):
    if cible_param == essai_param:
        print("Bravo!!!")
        return 0
    #Message "Pas assez" si le prix est trop bas
    elif cible_param>essai_param :
        print("pas assez !!!")
    #"Trop élevé" si le prix est trop haut
    else:
        print("trop eleve")
    return 0
    # Message "Perdu" au bout de 5 essais
print(__name__)

if __name__ == '__main__':

    for i in range(1,6):
        #Choix du joueur
        try:
            essai = int(input(f"essai n°{i}- prix ?"))
        except:
            print("Valeur incorrecte")
            continue #Redémarre à l'itération suivante
        if verif(cible,essai) ==0:
            break

    """#Message "Bravo" si le prix a été trouvé
    if cible == essai:
        print("Bravo!!!")
        break
    #Message "Pas assez" si le prix est trop bas
    elif cible >essai :
        print("pas assez !!!")
    #"Trop^elevé" si le prix est trop haut
    else:
        print("trop eleve")
    # Message "Perdu" au bout de 5 essais"""

    if (cible != essai):
        print ("PERDU")
#Fin au bout de 5 essais ou si le prix est trouvé
