# -*-coding:Utf-8 -*

# Créer un nouveau fichier Exercice2.py dans votre projet et configurer le charset en utf-8

# En utilisant des boucles while lorsque le nombre d'itérations n'est pas connu et des boucles for lorsque le nombre d'itérations est connu :
#

#######################################################################################################################
# 1. Écrire un algorithme qui demande un entier positif, et le rejette tant que le nombre saisi n’est pas conforme.
#######################################################################################################################

# a = int(float(input("Partie 1: Tapez un entier svp => ")))
#
# while a<0:
#     a = int(float(input(" ce n'est pas un entier positif \n retapez un entier positif svp => ")))
#
# else:
#     print(a, "est bien un entier positif")

#######################################################################################################################
# 2. Écrire un algorithme qui demande 10 entiers, compte le nombre d’entiers positifs saisis, et affiche ce résultat.
#######################################################################################################################

# cpt = 0
#
# for i in range(10):
#     a = int(float(input("Tapez un entier svp => ")))
#     if a > 0:
#         cpt = cpt + 1
# print("On a", cpt, "entiers positifs")

#######################################################################################################################
# 3. Écrire un algorithme qui demande des entiers positifs à l’utilisateur, les additionne, et qui s’arrête en affichant le
# résultat dès qu’un entier négatif est saisi.
#######################################################################################################################

# a = 0
# add = 0
#
# while a >= 0:
#     a = int(float(input("Tapez un entier svp => ")))
#     if a > 0:
#         add = add + a
#     else:
#         print("La somme des entiers est", add)

#######################################################################################################################
# 4. Modifier ce dernier algorithme pour afficher la moyenne de la série d’entiers positifs saisis.
#######################################################################################################################

a = 0
add = 0
moy = 0
cpt = 0

while a >= 0:
    a = int(float(input("Tapez un entier svp => ")))
    if a > 0:
        add = add + a
        cpt = cpt + 1
    else:
        moy = add / cpt
        print("La moyenne des entiers est", moy)