# POO EXERCICE DE MISE EN SITUATION 3

# ---
class Chat:
    def __init__(self, nom):
        self.nom = nom

    def SePresenter(self):

        print("Bonjour, je suis un chat et je m'appelle " + self.nom)

# ---
class Personne:
    def __init__(self, nom):
        self.nom = nom
    def SePresenter2(self):
        print("Bonjour, je suis une personne et je m'appelle " + str(self.nom))

# ---
chat1 = Chat("inconnu")
chat1.SePresenter()  # Bonjour, je suis un chat et je m'appelle inconnu

chat2 = Chat("Garfield")
chat2.SePresenter()  # Bonjour, je suis un chat et je m'appelle Garfield

personne1 = Personne("Jean")
personne1.SePresenter2()  # Bonjour, je suis une personne et je m'appelle Jean