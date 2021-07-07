# -*-coding:Utf-8 -*

def creer_tableau2d(nb_lignes, nb_colonnes):
    return [[0] * nb_colonnes for _ in range(nb_lignes)]


def initialise_tableau2d(size_x, size_y, tableau):
    for y in range(size_y):
        for x in range(size_x):
            tableau[x][y] = ' '


def affiche_tableau2d(size_x, size_y, tableau):
    for y in range(size_y):
        for x in range(size_x):
            print(tableau[x][y], end='')  # l'option end='' permet d'éviter les retour à la ligne après chaque print
        print("\r")


def ligne(x_start, y_start, x_end, y_end, tableau):
    if x_start > x_end:
        m = x_end
        x_end = x_start
        x_start = m

    if y_start > y_end:
        m = y_end
        y_end = y_start
        y_start = m

    for y in range(y_start, y_end + 1):
        for x in range(x_start, x_end + 1):
            tableau[x][y] = '*'


def rectangle(x, y, l, h, tableau):
    ligne(x, y, x + l, y, tableau)
    ligne(x, y + h, x + l, y + h, tableau)
    ligne(x, y, x, y + h, tableau)
    ligne(x + l, y, x + l, y + h, tableau)

def gere_rectangle(x, y, l, h, tableau):
    a = (x + 5 , y - 5, l - 10 , h + 10)
    return a
######################################################################################################################
# Algorithme principal:
#
# Créer un tableau 2D
# Mise à blanc du tableau
# Tracer des rectangles dans le tableau
# Afficher le tableau à l'écran
######################################################################################################################

nb_colonnes = 71
nb_lignes = 71

x = 10
y = 30
l = 60
h = 20

# 1) mise à blanc du tableau
tableau = creer_tableau2d(nb_lignes, nb_colonnes)
initialise_tableau2d(nb_lignes, nb_colonnes, tableau)

#ligne(0, 0, 0, 5, tableau)
# 2) Dessin des rectangle en mémoire
#rectangle(x, y , l, h, tableau)
# Entre chaque itération, chaque rectangle est décalé de +5 en x, -5 en y, -10 en largeur, +10 en hauteur
for i in range(0, 5):
    rectangle(x + 5 * i, y - 5 * i, l - 10 * i, h + 10 * i, tableau)

# 3) Afficher le tableau
affiche_tableau2d(nb_lignes, nb_colonnes, tableau)