



def age_nom(nom="",age=0):
    #cas 1
    if nom =="":
        print("Vous n'avez pas donné de nom, l'age vaut : " + str(age))
        return
    else:
        # cas 2
        if age == 0:
            print("le nom de la personne est : " +str(nom))
        # cas 3
        else :
            print("le nom de la personne est : "+str(nom)+ " ,son age est : " + str(age))
        if age_mineur(age):
            print("La personn est MAJEUR !")
        else :
            print("La personn est MINEUR !")



def age_mineur(age):
    if age >=18:
        return True
    return False

print("=====cas 1", "pas de nom")
age_nom(age= 20)
age_nom(age= 21)
age_nom(age= 22)
print("=====cas 2", "age =0")
age_nom(nom="Omar",age= 0)
print("=====cas 3", "le nom avec l'age")
age_nom(nom="Omar",age= 10)


'''print("=====cas 4", "Return True")
if age_mineur(19):
    print("Vous etes Majeur !")
else:
    print("Vous etes Mineur ! ")
print("=====cas 5", "Return False")
if age_mineur(10):
    print("Vous etes Majeur !")
else:
    print("Vous etes Mineur ! ")
'''