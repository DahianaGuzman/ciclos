try:
    n=int(input("ingrese un número: ")) # la tabla de multiplicar deseada
except:
    print('ERROR: ingrese un número entero')
else:
    if n<=0:
        print('Ingrese un número no negativo (>0)')
    else:
        for i in range(1,11):
            print(n,"x",i,"=",n*i) # imprime la tabla