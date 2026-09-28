montant = int (input("entrer le montant en $: "))
Nbr_billet_200 = montant // 200
rest_200 = montant % 200
Nbr_billet_100 = rest_200 // 100
rest_100 = rest_200 % 100
Nbr_billet_50 = rest_100 // 50
rest_50 = rest_100 % 50
Nbr_billet_20 = rest_50 // 20
rest_20 = rest_50 % 20
Nbr_billet_10 = rest_20 // 10
rest_10 = rest_20 % 10
Nbr_billet_5 = rest_10 // 5
rest_5 = rest_10 % 5
Somme_Billets = Nbr_billet_200*200 + Nbr_billet_100*100 + Nbr_billet_50*50 + Nbr_billet_20*20 + Nbr_billet_10*10 + Nbr_billet_5*5
Rest = montant - Somme_Billets
print(f"le nombre de billets est : {Nbr_billet_200}x200+{Nbr_billet_100}x100+{Nbr_billet_50}x50+{Nbr_billet_20}x20+{Nbr_billet_10}x10+{Nbr_billet_5}x5")
print(f"le reste est : {Rest} ")

