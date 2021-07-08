# -*-coding:Utf-8 -*

# TESTS FICHIERS
#
# from os import getcwd
# rep_cour = getcwd()
#
# print(rep_cour)



# EXERCICE 1.1
#
# f = open('Monfichier.txt', 'r')
# lignes = f.readlines()
# cpt_nb_ligne_with_digit =0
# for ligne_courante in lignes:
#     mots_ligne = ligne_courante.split(" ")
#     for mot in ligne_courante:
#         if mot.isdigit():
#             cpt_nb_ligne_with_digit += 1
#             break
# print("le nb de ligne contenant des nombres est de", cpt_nb_ligne_with_digit)


# EXERCICE 1.2

f = open('MonfichierDoc.txt', 'r')
lignes = f.readlines()
cpt_mot =0
for ligne_courante in lignes:
    mots_lignes = ligne_courante.split(" ")
    cpt_mot += len(mots_lignes)
print("Le nombre de mot dans le texte est de => ", cpt_mot)


# EXERCICE 1.3

f = open('MonfichierDoc.txt', 'r')
fd = open('FichierCap.txt', 'w')
lignes = f.readlines()
for ligne_courante in lignes:
    ligne_courante = ligne_courante.capitalize()
    #print(ligne_courante)
    fd.write(ligne_courante)
fd.close()


# EXERCICE 1.4

f = open('MonfichierDoc.txt', 'r')
fd = open('FichierFusion.txt', 'a')
lignes = f.readlines()
for i in range(len(lignes)):
    mots_lignes = lignes[i].split(" ")
    # print(mots_lignes[0])
    if mots_lignes[0].islower():
        nouvelle_phrase = lignes[i-1] + lignes[i]
        print(nouvelle_phrase)
fd.write(nouvelle_phrase)


