# -*-coding:utf-8 -*

class IPv4:
    "Une classe qui va gérer les IP et les masques"

    # Création du constructeur d'IPv4
    def __init__(self, str_ipv4, str_mask):
        self.str_ipv4 = str_ipv4
        self.str_mask = str_mask
        self.str_ipv4_min = ""
        self.str_ipv4_max = ""

    # Création d'une méthode qui demande de saisir d'une adresse IPv4
    # Sous la forme x3.x2.x1.x0 et qui vérifie que chaque bloc saisie est compris entre 0 et 255
    def saisie_ipv4(self):
        ip = input("Merci d'entrer une ip sous la forme x3.x2.x1.x0 : ")
        ip_split = ip.split(".")
        cpt_erreur = 0
        for i in range(4):
            if int(ip_split[i]) < 0 or int(ip_split[i]) > 255:
                cpt_erreur =+ 1
        if cpt_erreur >= 1:
            print("Le format de l'ip est incorrect ")
        else:
            self.str_ipv4 = ip


    # Création d'une méthode qui de saisir un masque de sous-réseau
    # Sous le forme m3.m2.m1.m0 et qui vérifie que chaque bloc saisie est compris entre 0 et 255
    def saisie_mask(self):
        mask = input("Merci d'entrer un masque de sous réseau sous la forme m3.m2.m1.m0 :")
        mask_split = mask.split(".")
        cpt_erreur = 0
        for i in range(4):
            if int(mask_split[i]) < 0 or int(mask_split[i]) > 255:
                cpt_erreur =+ 1
        if cpt_erreur >= 1:
            print("Le format du masque est incorrect ")
        else:
            self.str_mask = mask

    # Création d'une méthode qui inverse les bits d'un entier fourni en entrée
    def complement_bit_a_bit(self, x):
        x_compl = (~x) & 255
        return x_compl

    # Création d'une méthode qui réalise un ET logique entre deux entiers
    def et_logique_bit_a_bit(self, x, y):
        result_et_logique = x & y
        return result_et_logique

    # Création d'une méthode qui réalise un OU logique entre deux entiers
    def ou_logique_bit_a_bit(self, x, y):
        result_ou_logique = x | y
        return result_ou_logique

    # Création d'une méthode qui met à jour l'attribut self.str_ipv4_min après calcul
    def __calcule_ip_min(self):
        #print(self.str_ipv4)
        ip_split = self.str_ipv4.split(".")
        mask_split = self.str_mask.split(".")
        ip_calcul = []
        for i in range(4):
            if i == 3:
                ip_calcul.append(str((self.et_logique_bit_a_bit(int(ip_split[i]),  int(mask_split[i]))) + 1))
            else:
                ip_calcul.append(str(self.et_logique_bit_a_bit(int(ip_split[i]), int(mask_split[i]))))
        result = ".".join(ip_calcul)
        self.str_ipv4_min = result

    # Création d'une méthode qui va permettre de faire le calcul de self.str_ipv4_min
    # et d'attribuer cette valeur à self.str_ipv4_min
    def get_ipv4_min(self):
        self.__calcule_ip_min()
        return self.str_ipv4_min

    # Création d'une méthode qui met à jour l'attribut self.str_ipv4_max après calcul
    def __calcule_ip_max(self):
        ip_split = self.str_ipv4.split(".")
        mask_split = self.str_mask.split(".")
        mask_compl = []
        for i in range(4):
            mask_compl.append(str((self.complement_bit_a_bit(int(mask_split[i])))))
        ip_calcul = []
        for i in range(4):
            if i == 3:
                ip_calcul.append(str((self.ou_logique_bit_a_bit(int(ip_split[i]), int(mask_compl[i])) - 1)))
            else:
                ip_calcul.append(str(self.ou_logique_bit_a_bit(int(ip_split[i]), int(mask_compl[i]))))
        result = ".".join(ip_calcul)
        self.str_ipv4_max = result

    # Création d'une méthode qui va permettre de faire le calcul de self.str_ipv4_max
    # et d'attribuer cette valeur à self.str_ipv4_max
    def get_ipv4_max(self):
        self.__calcule_ip_max()
        return self.str_ipv4_max




# Instanciation de l'objet
Ip_default = "74.125.43.99"
Mask_default = "255.255.252.0"
newIp = IPv4(Ip_default, Mask_default)


# Exercice 1
newIp.saisie_ipv4()
print(newIp.str_ipv4)

# Exercice 2
newIp.saisie_mask()
print(newIp.str_mask)

# Exercice 3
print(newIp.complement_bit_a_bit(5))
print(newIp.et_logique_bit_a_bit(6, 14))
print(newIp.ou_logique_bit_a_bit(6, 18))

#Exercice 4
print(newIp.get_ipv4_min())
print(newIp.get_ipv4_max())
