import numpy as np
import sys
print("Bienvenue !")
print("Ce programme vous permet de jouer à un jeu de création de LISTES .")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

choix = ""
ma_list = []


while choix !=5:
    choix = input(
        "Choisissez parmis les 5 options suivantes : "
        "1/ADD "
        "2/DEL "
        "3/SHOW "
        "4/CLEAR "
        "5/EXIT : ")
    if not (1 <= int(choix) <= 5 and choix.isdigit()):
        print("============================================")
        print("Veuillez choisir un nombre entre 1 et 5 ! ")
        print("============================================")





def my_Liste():
    rep_user = menu()
    ma_liste = ["ma_liste"]
    print("XXXXXXXXXXXXXXXXXX, ", ma_liste)
    if rep_user > "5":
        print("============================================")
        print("Vous ne pouvez pas choisir un nombre > 5 !!!")
        print("============================================")
        #menu()
    if rep_user == "1":
        add_element = input('le nom de élement à ajouter : ')
        print(add_element)
        ma_liste.append(add_element)
        print("Elément ", add_element, " a bien été ajouté à la liste ! ")
        #menu()
    elif rep_user == "2":
        rmv_element = input('le nom de élement à supprimer ')
        if rmv_element in ma_liste:
            ma_liste.remove(rmv_element)
            print("Elément ", rmv_element, " a bien été supprimé à la liste ! ")
        else:
            print("Elément ", rmv_element, "existe pas dans la liste")
        #menu()
    elif rep_user == "3":
        print("Votre liste est la suivante : ", ma_liste)
    elif rep_user == "4":
        ma_liste.clear()
        print("Votre liste a bien été vidé. Elle ne contient aucun élément ! ", ma_liste)
    elif rep_user == "5":
        print("Quiiter")
        sys.exit()
    else :
        print(">>>>>>>>>>>>>>>>>>> ESLE")
        menu()


my_Liste()
#menu()