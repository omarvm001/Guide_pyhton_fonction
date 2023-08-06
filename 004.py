


# 1
'''''print("hello world")

# 2 Attention ici l'espace avant/après la virgule
nom = "Omar"
print ("hello", nom)

# 3 Attention ici l'espace avant/après la virgule
nom = "Omar"
print ("hello " + str(nom))

# 4
nom = "Omar2"
age = 35
print ("hello, je suis " + str(nom) + " mon age est : "+ str(age))

# 5
nom_user = input("Entrez votre nom : ")
age_user = input("Entrez votre age : ")
print("Votre Nom est :", nom_user, ",votre avez : " + str(age_user) + " ans.")
print("END 5")


# 6 nom et age user

nom_user2 = input("Quel est votre nom ? : ")
age_user2 = input("Quel est votre age ? : ")
print("je suis " +str(nom_user2) + " j'ai " +str(age_user2) + " ans." )
'''''
# ++++++++++++++++++++++++++++++++      NOM OPTIONEL
# CETTE FONCTION AFFICHE LES PARAMETRES DE LA FONCTION AVEC AGE ET NOM  OPTIONEL !!!
# pour rendre un parmètre d'une focntion optionnel il faut lui donner une valeur : ex age = 0
def nom_age (nom="",age=0):
    if nom =="":
        print("vous n'avez pas donné de nom, l'age vaut " + str(age))

    else :
        if age == 0 :
            print("je suis " + str(nom))
        else :
            print("je suis " + str(nom) + " j'ai " + str(age) + " ans.")

if __name__ == '__main__':
    nom_age(age="20")
    nom_age("Omar")           # j'affiche juste le nom  !!
    nom_age("Yasmine", 29)    # j'affiche le nom et l'age

