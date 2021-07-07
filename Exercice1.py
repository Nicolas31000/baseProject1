# -*-coding:Utf-8 -*
import datetime

print("Hello")

#1. Écrire un algorithme qui demande un entier à l’utilisateur, teste si ce nombre est positif (>= 0) ou non, et affiche
#“positif” ou “négatif”.

a = input("Partie 1: Tapez un entier svp => ")
if int(a) >= 0:
    print("a est positif")
else:
    print("a est négatif")

#2. Écrire un algorithme qui demande un entier à l’utilisateur, teste si ce nombre est strictement positif, nul ou strictement
#négatif, et affiche ce résultat.

a = input("Partie 2: Tapez un entier svp => ")
if int(a) > 0:
    print("a est strictement positif")
elif int(a) == 0:
    print("a est nul")
else:
    print("a est strictement négatif")


#3. Écrire un algorithme qui demande un réel à l’utilisateur et affiche sa valeur absolue (sans utiliser de fonction
#prédéfinie évidemment).

a = input("Partie 3: Tapez un nombre svp => ")
if float(a) >= 0:
    print(a)
else:
    print(a[1:])

#4. Écrire un algorithme qui demande un réel à l’utilisateur et l’arrondit à l’entier le plus proche (les x,5 seront arrondis
#à l’entier supérieur).

a = input("Partie 4: Tapez un réel svp => ")
arrondi = round(float(a))
print("La valeur arrondie est: ", arrondi)

#5. Écrire un algorithme qui demande le numéro d’un mois et affiche le nombre jours que comporte ce mois (sans tenir
#compte des années bissextiles).

mois = input("Partie 5: Tapez un numéro de mois (entre 0 et 12) svp => ")
if int(mois) < 0:
    print("Le numéro de mois doit être supérieur ou égal à 1")
elif int(mois) > 12:
    print("Le numéro de mois doit être inférieur ou égal à 12")
else:
    if int(mois) == 2:
        print("Le mois", mois, "comporte 28 jours")
    elif (int(mois) == 4) or (int(mois) == 6) or (int(mois) == 9) or (int(mois) == 11):
        print("Le mois", mois, "comporte 30 jours")
    else:
        print("Le mois", mois, "comporte 31 jours")



#6. Écrire un algorithme qui vérifie si une année est bissextile. On rappelle qu’il y a des années bissextiles tous les
#4 ans, mais la première année d’un siècle ne l’est pas (1800, 1900 n’étaient pas bissextiles) sauf tous les 400 ans
#(2000 était une année bissextile).

annee = int(input("Partie 6: Entrez une année à verifier svp => "))
if(annee%4==0 and annee%100!=0) or (annee%400==0):
    print("L'année", annee, "est une année bissextile")
else:
    print("L'année", annee, "n'est pas une année bissextile")

#7. Écrire un algorithme qui demande une date sous la forme de 2 nombres entiers (numéro du jour et numéro du mois)
#et affiche la saison (ex : 12/02; hiver). On supposera que le premier jour de la saison est toujours le 21.

jour = int(input(" Partie 7: \n Tapez un numéro de jour (compris entre 1 et 31) svp => "))
mois = int(input(" Tapez un numéro de mois (compris entre 1 et 12) svp => "))

date = datetime.date(2021, mois, jour)

date_debut_printemps = datetime.date(2021, 3, 21)
date_debut_ete = datetime.date(2021, 6, 21)
date_debut_automne = datetime.date(2021, 9, 21)
date_debut_hiver = datetime.date(2021, 12, 21)

if (date < date_debut_ete and date >= date_debut_printemps):
    print("Le", jour, "/", mois, "nous sommes au printemps")
elif (date < date_debut_automne and  date >= date_debut_ete):
    print("Le", jour, "/", mois, "nous sommes en été")
elif (date < date_debut_hiver and date >= date_debut_automne):
    print("Le", jour, "/", mois, "nous sommes en automne")
else:
    print("Le", jour, "/", mois, "nous sommes en hiver")
