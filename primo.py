n = int(input('Ingrese número: ')) #ingrese el número a evaluar

if n == 2: # se establece el resultado de 2, como un número exceptuado
    print('es primo')
else:
    for i in range(2,n): # se evalua si es divisible por otros números además de 1 y el mismo: no primo
        if n%i == 0:
            print('no es primo')
            break
        if i == n-1: # si no, es divisible
            print('es primo')