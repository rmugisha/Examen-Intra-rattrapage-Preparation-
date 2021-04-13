print("Cours 2")


"Question1"
a = input('Entrer un premier nombre:')
b = input('Entrer un deuxieme nombre:')
a = int(a)
b = int(b)

print("Somme:", a + b)
print("Difference:", a - b)
print("Produit: ", a * b)
print("Moyenne: ", (a + b) / 2)
print("Distance: ", abs(a - b))
print("Maximum: ", max(a, b))
print("Minimum: ", min(a, b))

"Question2"
nbre_litres = input('Nombre de litres dans la voiture: ')
consommation = input('Consommation en litres: ')
prix_litres = input('Nombre de litres dans la voiture: ')

nbre_litres = int(nbre_litres)
consommation = float(consommation)
prix_litres = float(prix_litres)

print('Prix pour 100km: ', prix_litres * consommation)
print(' Distance restante : ', 100 * nbre_litres / consommation)

"Question3"
cout_voiture = input("Prix d'une voiture : ")
kilometre_an = input("Nombre kilomètres estimés par an : ")
prix_essence = input("Coût essence par litre : ")
efficacite = input("Consommation essence pour 100km : ")
valeur_revente = input("Valeur estimée revente 5 ans : ")

cout_voiture = int(cout_voiture)
kilometre_an = int(kilometre_an)
prix_essence = float(prix_essence)
efficacite = float(efficacite)
valeur_revente = int(valeur_revente)
cout_total = cout_voiture - valeur_revente + (efficacite * kilometre_an / 100) * prix_essence * 5
print(("Le cout total est de ", cout_total))

"Question4"

"Question5"
# n! = n x (n - 1) x (n - 2) .... 2 x 1
# n! = n x (n - 1)!
#
#
# 0! = 1
# 1! = 1 = 1 x 0!
# 2! = 2 = 2 x 1!
# 3! = 6 = 3 x 2!
# 4! = 24 = 4 x 3!
# 5! = 120 = 5 x 4!
def factorielle(n):
    """
    Implementation d'une factorielle
    y = f(x): y -> x!

    :param n: entier
    :return: resultat de la factorielle de n
    """
    print("Appel factorielle avec parametre: ", n)
    if n > 0:
        y = n * factorielle(n - 1)
        print("Retourne ", y)
        return y

    else:
        print("Retourne 1")
        return 1



#    if n == 0:
#        return 1

#    return n * factorielle(n - 1)


# a = int(input("Entrez une valeur : "))

# print("Factorielle : ", factorielle(a))



def age():
    age_demande = int(input("Quel est votre age ?"))

    if age_demande >= 18:
        print("Vous etes majeur(e)")

    elif age_demande < 0:
        print("Erreur. Vous mentez")

    else:
        print("Vous etes mineur(e)")

    print("Bonne journee")



# age()


def chanson(n):
    while n > 1:
        print("They were {} in the bed and the little one said 'roll over'".format(n))
        n = n - 1

    print("The little one said 'Good night'")


# chanson(10)

# s = "Bonjour"
# for c in s:
#     print(c)



# n! = n x (n - 1) x (n - 2) .... 2 x 1
# y = n! = 1 x 2 x 3 x 4 .... (n - 1) x n
def factorielle2(n):
    y = 1
    cnt = 1

    while cnt <= n:
        y = y * cnt
        cnt += 1

    return y


print(factorielle2(5))




