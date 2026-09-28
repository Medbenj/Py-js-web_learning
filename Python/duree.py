Temp=int(input("entrer le temp en seconde : "))

heur = Temp // 3600
min = (Temp % 3600) // 60
sec = Temp % 60
print(f"le temps en heure:minute:seconde est : {heur}:{min}:{sec}")