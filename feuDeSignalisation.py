# -*-coding:Utf-8 -*
#

# Créer un fichier feuDeSignalisation.py et configurer l'encodage utf-8

# 1) Définir une classe Feu_De_Signalisation pour décrire son fonctionnement.

# 2) Le constructeur de la classe ( méthode __init__() ) initialise son état à "vert" par le biais d'un un index pour suivre cet enregistrement.
# 	Cet index sera initialisé à 0, utiliser une liste ["Vert", "Orange", "Rouge", "Orange Clignotant"]
#

#NOTRE CORRECTION

# class Feu_De_Signalisation:
#     liste_etat = ["Vert", "Orange", "Rouge", "Orange Clignotant"]
#
#     def __init__(self):
#         self.etat = self.liste_etat[0]
#
#
# feu = Feu_De_Signalisation()
#
# print(feu.etat)


#3) La méthode successeur doit faire passer le feu d'une couleur à une autre en incrémentant l'index d'enregistrement modulo 3
# La méthode afficher_etat doit afficher l'état du feu de signalisation


# --coding:Utf-8 -

class FeuDeSignalisation:

    def __init__(self):
        self.couleurs = ["Vert", "Orange", "Rouge", "Orange Clignotant"]
        self.index = 0

    def Afficher_Etat(self):
        return print(self.couleurs[self.index])

    def Successeur(self):
        self.index += 1
        if self.index > 2:
            self.index = 0

feu = FeuDeSignalisation()

feu.Afficher_Etat()
feu.Successeur()
feu.Afficher_Etat()
feu.Successeur()
feu.Afficher_Etat()