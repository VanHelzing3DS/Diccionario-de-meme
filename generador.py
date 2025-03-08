import random
lista = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""
lon = int(input("Escribe la longitud de la contraseña"))
for i in range(lon):
    password += random.choice(lista)
print("Tu contraseña es",password)
