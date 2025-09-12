try:
    n = int(input ('Ingrese un número para calcular su factorial: '))
except:
    print('ERROR: Ingrese un número entero') # si se ingresa un valor no entero salta error.
else:
    if n<0: # Si el número es negativo
        print('ERROR: Ingrese un número positivo')
    else:
        factorial = 1 # Se toma como valor inicial 1
        if n == 0: # si n es igual a 0, entonces 0! = 1
            factorial = 1
        else:
            for i in range(1,n+1): # Multiplica el valor dado de manera sucesiva 1*(n)*(n-1)*...*(1) para calcular el factorial
                factorial *= (n-i+1) 
        print(f'{n}! = {factorial}') # Imprimir resultado final
