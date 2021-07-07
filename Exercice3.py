# -*-coding:Utf-8 -*

# ######################################################################################################################
# Créer un fichier Fonctions.py et configurer l'encodage
# ######################################################################################################################

##########################################################################################################################################
# 1) Créer une fonction qui creer_tableau2d(nb_lignes, nb_colonnes) et renvoi un tableau 2D (liste 2D)
##########################################################################################################################################

def creer_tableau2d(nb_lignes, nb_colonnes):
    tableau = []
    for i in range(nb_lignes):
        ligne = [0] * nb_colonnes
        tableau.append(ligne)
    return tableau

##########################################################################################################################################
# 2) Créer une fonction initialise_tableau2d(nb_lignes, nb_colonnes, tableau) qui initialise le contenu à '*' pour chacun des éléments
##########################################################################################################################################

def initialise_tableau2d(size_x, size_y, tableau):
    for x in range(size_x):
        for y in range(size_y):
            tableau[x][y] = '*'
            print(tableau)

##########################################################################################################################################
# 3) Créer une fonction affiche_tableau2d(nb_lignes, nb_colonnes, tableau) qui affiche le tableau à l'écran
##########################################################################################################################################

def affiche_tableau2d(size_x, size_y, tableau):
    for x in range(size_x):
        for y in range(size_y):
            print(tableau[x][y], end="") #l'option end =''permet d'éviter les retours à la ligne après chaque print
            print("\r")

##########################################################################################################################################
# Utilisation de fonctions
##########################################################################################################################################

nb_colonnes = 5
nb_lignes = 5

tableau = creer_tableau2d(nb_lignes, nb_colonnes)
print(tableau)
print("#######################################################################")
initialise_tableau2d(nb_lignes, nb_colonnes, tableau)
print(tableau)
print("#######################################################################")
affiche_tableau2d(nb_lignes, nb_colonnes, tableau)
print(tableau)
