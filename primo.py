try:
    n = int(input('Ingrese número: ')) # Ingrese el número a evaluar
except:
    print('ERROR: ingrese un número entero')
else:
    if n == 2: # Se establece el resultado de como caso especial
        print('El número es primo')
    elif n<=1:
        print('ERROR: Ingrese un número mayor que 1')
    else:
        for i in range(2,n): # Se evalua si es divisible por otros números además de 1 y el mismo: no primo
            if n%i == 0:
                print('El número no es primo')
                break
            if i == n-1: # Si no, es divisible
                print('El número es primo')