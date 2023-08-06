

class Personne:
    def __init__(self, nom):
        print("Je m'appelle " + nom)

    def se_presenter(self):
        print("je m'appelle toto")


# le constructeur crée en mémoire un OBJET DANS LE SELF
personne1 = Personne("Omar")  # OBJET 1 crée par le constructeur
#personne2 = Personne()  # OBJET 2 crée par le constructeur
personne1.se_presenter()

