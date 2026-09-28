Distance = int(input("entrer la distance en Km : "))
heures = int(input("entrer les heures  : "))
minutes = int(input("entrer les minutes  : "))
secondes = int(input("entrer les seconde  : "))
Duree = heures + minutes / 60 + secondes / 3600
vitesse = Distance / Duree
print(f"Le vitesse est : {vitesse:.2f} Km/h")