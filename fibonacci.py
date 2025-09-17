try:
    n = int(input('Términos Fibonacci: ')) # solicita la cantidad de términos de la serie de Fibonacci
except:
    print('ERROR: Ingrese un número entero')
else:
    if n<=0:
        print('ERROR: Ingrese un número mayor a 0')
    else:
        # se definen los primeros 2 términos
        a_0 = 0
        a_1 = 1
        if n == 1: # Si la cantidad de términos es igual a 1
            print('1.',a_0)
        elif n==2: # Si la cantidad de términos es igual a 2
            print('1.',a_0)
            print('2.',a_1)
        else:
            print('1.',a_0)
            print('2.',a_1)
            for i in range(1,n-1): # Al ya tener los términos 1 y 2, repetimos el proceso n-2 veces más para alcanzar n términos
                aux = a_0 # Se crea una variable auxiliar para almacenar del primer término
                a_0 = a_1 # El primer término pasa a ser el segundo término
                a_1 = a_1 + aux # Al segundo se le suma el valor del primer término almacenado
                print(f'{i+2}. {a_1}') # Se imprime el término correspondiente