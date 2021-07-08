# -*-coding:Utf-8 -*

# TESTS FICHIERS
#
# from os import getcwd
# rep_cour = getcwd()
#
# print(rep_cour)

f = open('Monfichier.txt', 'r')
lignes = f.readline()
cpt_nb_ligne_with_digit = 0
for ligne_courante in lignes:
    mots_ligne = ligne_courante.split(" ")
    for mot in mots_ligne:
        if mot.isdigit():
            cpt_nb_ligne_with_digit += 1
            break
print("Le nombre de ligne contenant des nombres est de => ", cpt_nb_ligne_with_digit)
