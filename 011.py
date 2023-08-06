print("Bienvenue !")
print("Ce programme vous permet de jouer à un jeu question/réponse QCM .")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
def question(pays):
    print("Quelle est la capitale du pays : " +str(pays) + " ?")
def reponse(ville1, ville2, ville3, ville4):
    print("(a)      "  +str(ville1))
    print("(b)      " + str(ville2))
    print("(c)      " + str(ville3))
    print("(d)      " + str(ville4))
    a = ville1
    b = ville2
    c = ville3
    d = ville4
    return a,b,c,d
def choix_user(bonne_reponse):
    rep_user = input("Votre réponse parmis les 4 propositions est : ")
    print("Votre réponse est : " + rep_user)

    if rep_user == bonne_reponse:
        print("Bien joué ! Bonne réponse.")
    else:
        print("MAuvaise réponse")
question("France")
reponse("Marseille", "Nice", "Paris", "Nanates" )
choix_user("c")
print()
question("Italie")
reponse("Rome", "Milan", "Venise", "Florence" )
choix_user("a")
print()
question("Espagne")
reponse("Madrid", "Barcelone", "Grenade", "Valence" )
choix_user("b")
print()
question("Algérie")
reponse("Tlemcen", "Oran", "Setif", "Alger" )
choix_user("d")
