# Mostraremos un mensaje de bienvenida
print('Bienvenido a la calculadora de áreas de circulo')

# Pediremos al usuario qye ingrese el valor
# del radio de interes

# la informacion que ingrese ek usuario con la funcion
# input() siempre sera una cadena de texto

#float() convertir una cadena de texto numerica a un numero (flotante decimales)
r = float(input('Ingrese el valor del radio: '))

# definiremos una variable denominada pi que almacenara el valor aprox de 3.1416
pi = 3.1416

# area de circulo: pi * r ** 2
# roud se redondea al numero de decimales qye elijas
# redondiaremos a 2 decimales
area = round(pi * r ** 2, 2)

# le mostramos el resultado
print('El área del círculo solicitado es de:', area, 'unidades cuadradas')
