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





