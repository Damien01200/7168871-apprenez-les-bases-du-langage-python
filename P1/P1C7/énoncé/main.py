#Creation dictionnaire

fruits={"pomme":"rouge",
        "banane":"jaune",
        "orange":"orange"}
fruits["kiwi"]="vert"
print(fruits)

#Valeur cle banane
couleur_banane = fruits["banane"]
print(couleur_banane)

#Valeur associé à la cle pomme pour vert
fruits["pomme"]= "vert" 
print(fruits)
#Supression cle banane du dictionnaire fruits

del fruits["banane"]
print(fruits)
#Afficher cles restante

print(fruits.keys())
