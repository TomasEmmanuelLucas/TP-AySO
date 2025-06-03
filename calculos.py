import time

def es_entero_positivo(texto):
    caracteres_validos = "0123456789"
    if texto == "":
        return False
    for caracter in texto:
        if caracter not in caracteres_validos:
            return False
    return True

def mostrar_menu():
    print("\n--- Menú de opciones ---")
    print("1. Mostrar el número mayor")
    print("2. Mostrar el número menor")
    print("3. Calcular el promedio")
    print("4. Sumar todos los números")
    print("5. Restar todos los números (en orden)")
    print("6. Salir")

def calcular_promedio(lista):
    return sum(lista) / len(lista)

# Recolección de números
numeros = []
seguir = True

print("Ingresá números enteros positivos. Para salir, escribí una letra o un número negativo.")

while seguir:
    entrada = input("Número: ")

    if es_entero_positivo(entrada):
        numero = int(entrada)
        if numero >= 0:
            numeros.append(numero)
        else:
            seguir = False
    else:
        seguir = False

if len(numeros) == 0:
    print("No se ingresaron números válidos.")
else:
    salir = False
    while not salir:
        mostrar_menu()
        opcion = input("Elegí una opción (1-6): ")

        if opcion == "1":
            print("\nNúmero mayor:", max(numeros))
            time.sleep(1.5)
        elif opcion == "2":
            print("\nNúmero menor:", min(numeros))
            time.sleep(1.5)
        elif opcion == "3":
            print("\nPromedio:", calcular_promedio(numeros))
            time.sleep(1.5)
        elif opcion == "4":
            print("\nSuma total:", sum(numeros))
            time.sleep(1.5)
        elif opcion == "5":
            resultado = numeros[0]
            for n in numeros[1:]:
                resultado -= n
            print("\nResultado de restar todos los números:", resultado)
            time.sleep(1.5)
        elif opcion == "6":
            print("\nSaliendo del programa.", end =" ")
            print(".", end=" ")
            time.sleep(1)
            print(".", end=" ")
            time.sleep(1)
            print(".")
            time.sleep(1)
            salir = True
        else:
            print("\nOpción no válida. Intentá de nuevo.")
            time.sleep(1.5)