
class Voiture :
    def __init__(self):
        self.essence = 100

    def afficher_reservoir(self):
        print(f"La voiture contient {self.essence}L d'essence.")

    def roule(self,km):

        if self.essence <= 0 :
            print("Le réservoir est vide :) !! Veuillez le remplir.")
            return
        self.essence -= km * (5 / 100)
        if self.essence < 10 :
            print("Vous n'avez bientôt plus d'essence !" , (self.essence ))
        self.afficher_reservoir()


    def faire_plein(self):
        self.essence =100
        print("Le réservoir est plein ! Vous pouvez repartir ...")

        return






#relation Objet et attribus
voiture1 = Voiture()
print("L'attribus de l'objet est : ", voiture1.essence)
voiture1.afficher_reservoir()
#voiture1.faire_plein()
#voiture1.roule(25)
#voiture1.faire_plein()
voiture1.roule(2000)
voiture1.roule(100)

#voiture1.afficher_reservoir()

#print(dir(voiture1))



