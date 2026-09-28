poids = float(input("enter votre poid en Kg : "))
taille = float(input("entrer votree taille en metre : "))
imc = ( poids / (taille**2) )
print(f"ton imc est : {imc:.2f}")