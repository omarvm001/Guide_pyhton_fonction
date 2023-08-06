

def recup_info ():
    min = input ("Entrez un Min : "  )
    max = input ("Entrez un Max : "  )
    n = input("Entrez le nbr n de la table de mutiplication : ")
    n_user =int(n)
    min_ser = int(min)
    max_ser = int(max)
    if min>max:
        print("KO ---- Vous avez entrer un Min > Max")
        return
    else :
        print("Vous avez entrer un Min < Max")

    for i in range(min_ser,max_ser+1):
        print (n_user*i)


def age_majeur(age):
    if age>=18:
        return True
    return False

def affich_info(num_personne,nom,age):
    print("Le nom de la personne  "  + str(num_personne) + " est : "  + nom)
    print("L'age  de la personne  "  + str(num_personne) + " est : "  + str(age))
    print("Le nom de la personne  "  + str(num_personne) + " comporte : "  + str(len(nom))+ " caractères.")
    if age_majeur(age):
        print("il est majeur")
    else:
        print("il est mineur")

def main_recup_affich(num_personne):
    nom1,age1= recup_info(num_personne)
    affich_info(num_personne,nom1,age1)

print("Bienvenue !")
print("Ce programme vous permet d'afficher la table de multiplicaton de n.")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

recup_info()
'''nbr_personne = input("Choisissez le nombre de personne : ")
nbr_personne_int = int(nbr_personne)
print("Le nombre de personne int a remplir  : ", nbr_personne_int)

for i in range(nbr_personne_int):
    main_recup_affich(i+1)
#main_recup_affich(1)
#affcer_nom(1)
#affcer_nom("2")

nom1 = input ("quel est votre nom ? : ")
age1 = input ("quel est votre age ? : ")
print("Vous etes : " +nom1)
print("Vous avez : " +age1 , "ans.")


nom1 = input ("quel est votre nom ? : ")
age1 = input ("quel est votre age ? : ")
print("Vous etes : " +nom1)
print("Vous avez : " +age1 , "ans.")
'''




