print("Mas Sobre Funiones")
# Aqui Se Escriben Las Funciones
def suma_ab(a, b):
    s = a + b
    return s
def resta_ab(a, b):
    r = a - b
    return r
def multiplicacion_ab(a, b):
    m = a * b
    return m
def divicion_ab(a, b):
    d = a / b
    return d

#Llamadas a Funciones
print("Calculando Suma")
n1 = int(input("Ingresa El Primer Numero: "))
n2 = int(input("Ingresa El Primer Numero: "))
suma = suma_ab(n1, n2)
print(f"La suma De {n1} + {n2} es: {suma}")

print("Calculando resta")
n3 = int(input("Ingresa El Primer Numero: "))
n4 = int(input("Ingresa El Primer Numero: "))
resta = resta_ab(n3, n4)
print(f"La resta De {n3} - {n4} es: {resta}")

print("Calculando multiplicacion")
n5 = int(input("Ingresa El Primer Numero: "))
n6 = int(input("Ingresa El Primer Numero: "))
multiplicacion = multiplicacion_ab(n1, n2)
print(f"La resta De {n5} * {n6} es: {multiplicacion}")

print("Calculando divicion")
n7 = int(input("Ingresa El Primer Numero: "))
n8 = int(input("Ingresa El Primer Numero: "))
divicion = divicion_ab(n7, n8)
print(f"La divicion De {n7} / {n8} es: {divicion}")