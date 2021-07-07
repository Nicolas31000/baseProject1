# -*-coding:Utf-8 -*

class MaClasse:
    __i = "12345"
    def set_i(self, entree):
        self.__i = entree

    def get_i(self):
        return self.__i

r = MaClasse()
print(r.get_i())

r.set_i("1234")
print(r.get_i())

class Point:
    "Définition d'un point mathématique"

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, hauteur, largeur, coin):
        self.largeur = largeur
        self.hauteur = hauteur
        self.coin = coin

    def perimetre(self):
        return self.largeur * 2 +self.hauteur * 2

    def aire(self):
        return self.largeur * self.hauteur

coin = Point(12, 27)
boite = Rectangle(50, 35, coin)
print("Le périmètre est : ", boite.perimetre())
print("L'aire est : ", boite.aire())
