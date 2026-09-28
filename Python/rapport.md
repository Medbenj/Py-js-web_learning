bon_jour.py 
entrer votre Prenom : Ahmed
Bonjour , Ahmed! Bienvennue dans le cour de Python

calcul.py
entrer le premier nombre 8
entrer le deuxieme nombre 3
La somme des duex nombre est :  {11}
la difference des duex nombre :  {5}
le produit des duex nombre est :  {24}
le quottient des duex nombre est :  {2.6666666666666665}
le quotient des deux nombre est :  {2}
le reste des deux nombre est :  {2}

### Trace table
x = 3 y = x + 5 x = y * 2 print(x, y)

| Statement | `x` | `y` | Output |
|---|---:|---:|---|
| `x = 3` | 3 | — | |
| `y = x + 5` | 3 | 8 | |
| `x = y * 2` | 16 | 8 | |
| `print(x, y)` | 16 | 8 | `16 8` |

### A

| Statement | `a` | `b` | Output |
|---|---:|---:|---|
| `a = 4` | 4 | — | |
| `b = a + 2` | 4 | 6 | |
| `a = b * 3` | 18 | 6 | |
| `print(a, b)` | 18 | 6 | `18 6` |

### B

| Statement | `x` | `y` | `z` | Output |
|---|---:|---:|---:|---|
| `x = 10` | 10 | — | — | |
| `y = 3` | 10 | 3 | — | |
| `z = x // y` | 10 | 3 | 3 | |
| `x = x % y` | 1 | 3 | 3 | |
| `print(x, z, x + z)` | 1 | 3 | 3 | `1 3 4` |

### C

| Statement | `prix` | `remise` | Output |
|---|---:|---:|---|
| `prix = 100` | 100 | — | |
| `remise = prix * 0.1` | 100 | 10 | |
| `prix = prix - remise` | 90 | 10 | |
| `print(prix)` | 90 | 10 | `90` |

### A - Name and age input

| Statement | `nom` | `age` | Output |
|---|---|---|---|
| `nom = "Amine"` | `Amine` | — | |
| `print("Bonjour," + nom + " !")` | `Amine` | — | `Bonjour,Amine !` |
| `age = input("Âge : ")` | `Amine` | age entered by user | `Âge : ` |
| `print("Vous avez " + age + " ans.")` | `Amine` | age entered by user | `Vous avez [age] ans.` |

### B - Total price

| Statement | `prix` | `quantite` | `total` | Output |
|---|---:|---:|---:|---|
| `prix = 19.99` | 19.99 | — | — | |
| `quantite = 3` | 19.99 | 3 | — | |
| `total = prix * quantite` | 19.99 | 3 | 59.97 | |
| `print(f"Total : {total:.2f} €")` | 19.99 | 3 | 59.97 | `Total : 59.97 €` |

### C - Division by zero

| Statement | `x` | `y` | Output |
|---|---:|---:|---|
| `x = 10` | 10 | — | |
| `y = 0` | 10 | 0 | |
| `print(x / y)` | 10 | 0 | `ZeroDivisionError` |

