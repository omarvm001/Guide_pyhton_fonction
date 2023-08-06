class Personne :
    def __init__(self, nom ="", age=0):
            self.nom=nom
            self.age = age
            if nom =="":
                self.DemanderNom()   # appeler une fonction depuis le constructeur
            print("Le constructeur de la Classe Personne " + str(self.nom))

    def SePresenter(self):
        if self.age ==0 :
            print("le nom de la personne est : " +str(self.nom))
        else:
            print("le nom de la personne est : " +str(self.nom) + " et son age est : " + str(self.age))
            #print("EstMajeur : ", Personne.EstMajeur(self))
            if self.EstMajeur() == True:
                print("La personne est Majeur.")
            else :
                print("La personne est Mineur.")
    def EstMajeur(self):
        if self.age >=18 :
            return True
        return False

    def DemanderNom(self):
        if self.nom == "":
            self.nom = input("Entrer le nom de la personne sans nom : ")

print("========================")
print("Création de l'OBJET")
print("========================")
personne1 = Personne("Omar", 34)
personne2 = Personne("Meyssa", 8)
personne3 = Personne(nom="", age=0)

print("========================")
print("Appel de METHODE")
print("========================")
personne1.SePresenter()
personne2.SePresenter()
personne3.SePresenter()


'''print("EstMajeur : ", personne1.EstMajeur())
print("EstMajeur : ", personne2.EstMajeur())
print("EstMajeur : ", personne3.EstMajeur())
'''
print("END.")
