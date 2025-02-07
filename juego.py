import random
print("========================================")
print("=======piedra papel o tijeras===========")
print("========================================")
print("seleccione un numero para escojer el objeto")
print("1. piedra")
print("2. papel")
print("3. tijeras")

n=input("dijite el numero del objeto: ")

num = random.randint(1, 3)  # Genera un número entre 1 y 3
print(num)

if n==1 and num==2:
    r= perdiste
if n==1 and num==3:
    r= ganaste
if n==2 and z==1:
    r= ganaste
if n==2 and num==3:
    r= perdiste
if n==3 and z==2:
    r= ganaste
else:
    r= numero_no_valido

print("el resultado es: "+str(r))