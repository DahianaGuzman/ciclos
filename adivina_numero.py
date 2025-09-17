import random #libreria
aleatorio = random.randint(1,100) #rango
print("ADIVINA EL NÚMERO SECRETO")
while True:
    try:
        numUsuario=int(input("ingrese un número: "))
    except:
        print('ERROR: ingrese un número entero')
    else:
        if numUsuario != aleatorio: #establecer número incorrecto
            print("No haz adivinado el número secreto, intenta nuevamente :( ")
            if numUsuario < aleatorio: #pistas para el usuario
                print("El número secreto es mayor")
            else:
                print("El número secreto es menor")
        else:
            numUsuario == aleatorio #aviso de número correcto
            print("¡Felicidades, haz adivinado el número secreto!")
            break
