entier = int(input("entrer un entier a trois chiffres : "))
Centaines = int(entier / 100)
Dizaines_C = int(entier % 100)
Dizaines = int(Dizaines_C / 10)
Unite = entier % 10
print(f"Centaines : {Centaines} \nDizaines : {Dizaines} \nunite {Unite} ")