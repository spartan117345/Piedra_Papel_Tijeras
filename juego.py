import math
print("========================================")
print("=======piedra papel o tijeras===========")
print("========================================")
print("seleccione un numero para escojer el objeto")
print("1. piedra")
print("2. papel")
print("3. tijeras")

n=input("dijite el numero del objeto: ")
z=math.ramdon(1.0,2.0,3.0)

if n==1 and z==2:
    r=perdiste
    print("perdiste el juego")

if n==1 and z==3:
    r=ganaste
print("ganaste el juego")

if n==2 and z==1:
    r=ganaste
print("ganaste el juego")

if n==2 and z==3:
    r=perdiste
print("oerdiste el juego")

if n==3 and z==1:
    r=perdiste
print("perdisyte el juego")

if n==3 and z==2:
    r=ganaste
print("ganaste el juego")

else:
    r=empate
print("empataste el juego")