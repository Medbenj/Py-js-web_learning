Temp_C = input("entrer la temperature en Celsius : ")
Temp_F = input("entrer la temperature en Fahrenheit : ")

Temp_C_F = (float(Temp_C) * 9/5) + 32
Temp_F_C = (float(Temp_F) - 32) * 5/9

print("La temperature en Fahrenheit est : " + str(Temp_C_F))
print("La temperature en Celsius est : " + str(Temp_F_C))
